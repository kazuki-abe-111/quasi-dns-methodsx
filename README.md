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


Restart field archives
----------------------

The final stored solution fields for the RANS and Quasi-DNS calculations are
provided as compressed restart archives in the GitHub Release associated with
this repository:

- `RANS_restart_2.63s.tar.gz`: final stored RANS fields at t = 2.63 s.
- `QuasiDNS_restart_0.0261s.tar.gz`: final stored Quasi-DNS fields at
  t = 0.0261 s.

Download and extract each archive in the corresponding OpenFOAM case directory
before use. The archives create the `2.63/` and `0.0261/` time directories,
respectively. The cases are configured to restart from the latest available
time directory.


Scope
-----

This repository provides the numerical materials associated with the MethodsX
manuscript, including the final OpenFOAM computational meshes, boundary
conditions, operating conditions, chemical mechanism, and numerical settings.
It also provides processed data for the principal and supplementary figures,
together with scripts for data processing and figure generation.

The complete time-resolved three-dimensional production-simulation histories
are not included because of their storage size. Instead, the final restart
fields are provided through the GitHub Release, and the repository includes
the processed data required to reproduce the reported diagnostics.


Citation
--------

If you use materials from this repository, please cite the associated
MethodsX manuscript listed above.
