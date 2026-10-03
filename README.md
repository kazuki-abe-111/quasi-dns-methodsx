Quasi-DNS with chemical kinetics for a single multiple-injection burner element
under stable lean conditions for future gas turbine applications
===============================================================================

Supporting materials for the MethodsX manuscript:

Kazuki Abe, Youhi Morii, and Kaoru Maruta,
"Quasi-DNS with chemical kinetics for a single multiple-injection burner
element under stable lean conditions for future gas turbine applications,"
MethodsX, submitted.


Contents
--------

case/
    OpenFOAM case files, including the final computational meshes,
    boundary-condition definitions, operating conditions, chemical-mechanism
    files, and numerical settings.

data/
    Processed data used to generate the principal and supplementary figures.

scripts/
    Scripts for data processing and figure generation.


Final solution fields
---------------------

The final solution fields obtained from the RANS and Quasi-DNS calculations are
provided as compressed archives with this research-data package:

- `2.63.tar.gz`: final solution fields from the RANS calculation.
- `0.0261.tar.gz`: final solution fields from the Quasi-DNS calculation.

After extraction in the corresponding OpenFOAM case directory, the archives
provide the final-time directories `2.63/` and `0.0261/`, respectively.


Software versions
-----------------

The simulations were performed using OpenFOAM v1706. Post-processing and
visualization were conducted using ParaView 5.12. The data-processing and
figure-generation scripts are provided in the `scripts/` directory.


Reproducibility
---------------

1. Use OpenFOAM v1706 and copy or extract the files in `case/` to an OpenFOAM
   working directory.
2. Run the calculation using the mesh, boundary conditions, operating
   conditions, chemical-mechanism files, and numerical settings supplied in
   the corresponding case directory.
3. Extract `2.63.tar.gz` or `0.0261.tar.gz` in the corresponding case
   directory when the final RANS or Quasi-DNS solution fields are required.
4. Reproduce the reported figures and diagnostics using the processed data in
   `data/` and the scripts in `scripts/`. The supplied fields may be visualized
   using ParaView 5.12.


Scope
-----

This repository provides the numerical materials associated with the MethodsX
manuscript, including the final OpenFOAM computational meshes, boundary
conditions, operating conditions, chemical mechanism, and numerical settings.
It also provides processed data for the principal and supplementary figures,
together with scripts for data processing and figure generation.

The complete time-resolved three-dimensional production-simulation histories
are not included because of their storage size. Instead, the final solution
fields are provided as compressed archives, and the repository includes the
processed data required to reproduce the reported diagnostics.


Citation
--------

If you use materials from this repository, please cite the associated
MethodsX manuscript listed above.