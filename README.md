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
provided as compressed archives in the GitHub Release associated with this
repository:

- `2.63.tar.gz`: final solution fields from the RANS calculation.
- `0.0261.tar.gz`: final solution fields from the Quasi-DNS calculation.

After extraction in the corresponding OpenFOAM case directory, the archives
provide the final-time directories `2.63/` and `0.0261/`, respectively.


Scope
-----

This repository provides the numerical materials associated with the MethodsX
manuscript, including the final OpenFOAM computational meshes, boundary
conditions, operating conditions, chemical mechanism, and numerical settings.
It also provides processed data for the principal and supplementary figures,
together with scripts for data processing and figure generation.

The complete time-resolved three-dimensional production-simulation histories
are not included because of their storage size. Instead, the final solution
fields are provided through the GitHub Release, and the repository includes
the processed data required to reproduce the reported diagnostics.


Citation
--------

If you use materials from this repository, please cite the associated
MethodsX manuscript listed above.
