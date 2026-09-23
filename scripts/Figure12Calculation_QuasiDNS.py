import os
import numpy as np
from paraview.simple import *
from vtk.util.numpy_support import vtk_to_numpy
from paraview.servermanager import Fetch

# === 設定 ===
input_file = "test.foam"
output_dir = "output_avg_clip"
output_csv = "x_integrated_avg.csv"
x_min = -1.0
x_max_list = np.linspace(0.0, 0.5, 51)
time_range = (0.00001, 10.0)
scalars_to_integrate = ['T', 'Qdot']

# 出力ディレクトリ作成
os.makedirs(output_dir, exist_ok=True)

# === OpenFOAM 読み込み（Reconstructed）===
foam_data = OpenFOAMReader(FileName=input_file)
foam_data.MeshRegions = ['internalMesh']
foam_data.CellArrays = scalars_to_integrate
foam_data.SkipZeroTime = 1
foam_data.CaseType = 'Reconstructed Case'
foam_data.UpdatePipelineInformation()

# 時間ステップ取得
all_times = foam_data.TimestepValues
selected_times = [t for t in all_times if time_range[0] <= t <= time_range[1]]
if not selected_times:
    raise RuntimeError("指定時間範囲に有効な時刻がありません")

# 時間制限
scene = GetAnimationScene()
scene.UpdateAnimationUsingDataTimeSteps()
scene.StartTime = selected_times[0]
scene.EndTime = selected_times[-1]

# TemporalStatisticsで時間平均
temporal_stats = TemporalStatistics(Input=foam_data)
temporal_stats.UpdatePipeline()

# CalculatorでX座標計算
calc = Calculator(Input=temporal_stats)
calc.ResultArrayName = "Xcoord"
calc.Function = "coordsX"
calc.UpdatePipeline()

# === すべてのx_maxについて処理 ===
csv_path = os.path.join(output_dir, output_csv)
with open(csv_path, "w") as f:
    header = ["x_min", "x_max"] + [f"{s}_avg" for s in scalars_to_integrate] + ["Volume"]
    f.write(",".join(header) + "\n")

    for x_max in x_max_list:
        print(f"→ x_max = {x_max:.3f}")

        # 範囲抽出
        thresh = Threshold(Input=calc)
        thresh.Scalars = ["POINTS", "Xcoord"]
        thresh.LowerThreshold = x_min
        thresh.UpperThreshold = x_max
        thresh.UpdatePipeline()

        # 積分
        integrate = IntegrateVariables(Input=thresh)
        integrate.UpdatePipeline()

        result = Fetch(integrate)
        cell_data = result.GetCellData()

        # スカラー値取得
        values = []
        for name in scalars_to_integrate:
            array = cell_data.GetArray(f"{name}_average")
            values.append(vtk_to_numpy(array)[0] if array else np.nan)

        # Volume取得
        vol_array = cell_data.GetArray("Volume")
        volume = vtk_to_numpy(vol_array)[0] if vol_array else np.nan

        # CSV行書き出し
        row = [x_min, x_max] + values + [volume]
        f.write(",".join(map(str, row)) + "\n")

