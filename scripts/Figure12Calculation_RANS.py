import os
from paraview.simple import *
import numpy as np
from vtk.util.numpy_support import vtk_to_numpy

# === 設定 ===
input_file = "test.foam"  # OpenFOAM のケースファイル
output_dir = "output_csv"  # 出力ディレクトリ
output_csv = os.path.join(output_dir, "integrated_by_time.csv")  # 出力CSVファイル名

x_min = -1.0  # x方向の最小値
x_max_list = np.linspace(0.0, 0.5, 51)  # xの最大値の範囲
scalars_to_integrate = ['T', 'Qdot']  # 積分対象のスカラー名

# === 出力ディレクトリ作成 ===
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# === ヘッダー付きでCSVファイル初期化 ===
with open(output_csv, "w") as f:
    headers = ["Time", "x_min", "x_max"] + [f"{s}_integral" for s in scalars_to_integrate] + ["Volume"]
    f.write(",".join(headers) + "\n")

# === OpenFOAM データ読み込み ===
foam_data = OpenFOAMReader(FileName=input_file)
foam_data.MeshRegions = ['internalMesh']
foam_data.CellArrays = scalars_to_integrate
foam_data.SkipZeroTime = 1
foam_data.CaseType = 'Reconstructed Case'  # または 'Decomposed Case'

# === 時刻ステップの取得 ===
time_steps = foam_data.TimestepValues

for time in time_steps:
    print(f"\n=== Processing time = {time:.6f} ===")

    # 時刻をアニメーションシーンに適用
    animationScene = GetAnimationScene()
    animationScene.UpdateAnimationUsingDataTimeSteps()
    animationScene.TimeKeeper.Time = time

    for x_max in x_max_list:
        print(f"  - x_max = {x_max:.3f}")

        # Calculator で x座標をスカラーとして作成
        calc = Calculator(Input=foam_data)
        calc.ResultArrayName = "Xcoord"
        calc.Function = "coordsX"

        # Threshold フィルターで範囲指定（x_min から x_max）
        thresh = Threshold(Input=calc)
        thresh.Scalars = ["POINTS", "Xcoord"]
        thresh.LowerThreshold = x_min  # x_minの設定
        thresh.UpperThreshold = x_max  # x_maxの設定

        # 積分計算
        integrate = IntegrateVariables(Input=thresh)
        UpdatePipeline(time)

        # 結果データ取得
        result = servermanager.Fetch(integrate)
        cell_data = result.GetCellData()

        # 各スカラーの積分値を取得
        values = []
        for name in scalars_to_integrate:
            array = cell_data.GetArray(name)
            value = vtk_to_numpy(array)[0] if array else np.nan
            values.append(value)

        # 体積の取得
        vol_array = cell_data.GetArray("Volume")
        volume = vtk_to_numpy(vol_array)[0] if vol_array else np.nan

        # CSVに1行追加
        with open(output_csv, "a") as f:
            row = [time, x_min, x_max] + values + [volume]
            f.write(",".join(map(str, row)) + "\n")
