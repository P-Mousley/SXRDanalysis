# SXRD analysis GUIs
This project contains GUIs to help with analysis of surface x-ray diffraction data, for use alongside the analysis software ROD

To load up GUI, download the structureplot.py file and then run in python. 
If there is a clash of module versions, try creating a new environment called 'plotting' for running the GUI by entering the following commands:

conda create --name plotting <br />
conda activate plotting<br />
conda install numpy<br />
conda install pandas<br />
conda install matplotlib"<br />


currently works with module version:<br />
<br />
#pandas                    1.5.2           py311hf63dbb6_2    conda-forge<br />
#numpy                     1.24.1          py311h95d790f_0    conda-forge<br />
#matplotlib                3.6.2           py311h1ea47a8_0    conda-forge<br />


screenshot of GUI as of 14-01-2023
![Alt text](/sxrdstructgui.png?raw=true "Optional Title")
