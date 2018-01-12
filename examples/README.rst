
FLORIS
------

The inputs to the Floirs model are provided in floris.json and use the NREL 5MW turbine as a reference.  The model parameters used have been published in previous work.  All inputs to the FLORIS model can be changed in the floris.json file.  Note that changing these parameters may result in an unphysical solution.  For questions regarding FLORIS, please contact `Jen Annoni <mailto:jennifer.annoni@nrel.gov>`_, `Paul Fleming <mailto:paul.fleming@nrel.gov>`_, or `Rafael Mudafort <mailto:rafael.mudafort@nrel.gov>`_.


FLORIS_Run_Notebook.ipynb is an interactive python notebook that details the execution of Floris in normal operating conditions.  It also demonstrates how to perform an example optimization for wake steering with Floris.  The results of the optimization are based on pre-tuned parameters and the NREL 5MW turbine.  There is no warranty on the optimization results.      


example_script.py
=================

This script provides an example of how to execute Floris.  In particular, this script:

	1. Loads the input file "floris.json" and initializes Floris
		``floris = Floris("floris.json")``

	2. Computes the local power coefficient, thrust coefficients, power, axial induction, and wind speeds at each turbine.  Here is an example of how to get the local wind speeds at a turbine.
		``turbine.get_average_velocity())``

	3. Plot the flow field at a horizontal slice.  In this example, the flow field is plotted at 50% (0.5) of the total z domain, which is 2x the hub height.  
		``floris.farm.flow_field.plot_z_planes([0.2, 0.5, 0.8])``


example_optimization.py
=======================



Future work
===========
Coming soon

License
=======

Copyright 2017 NREL

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
