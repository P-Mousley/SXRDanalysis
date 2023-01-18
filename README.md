# SXRD analysis GUIs
This project contains GUIs to help with analysis of surface x-ray diffraction data, for use alongside the analysis software <a href="https://www.esrf.fr/computing/scientific/joint_projects/ANA-ROD/index.html"> ROD </a>

To load up GUI, download the structureplot.py file and structuregui.ui and then change line 25 in structureplot.py with hardcoded filepath for UI file <br />
e.g. self.ui = uic.loadUi(r"######\structuregui.ui", self)   <br />
where ##### is the directory the ui file is saved.<br />
Then run the structureplot.py file in python. <br />
If you are using anaconda package and there is a clash of module versions, you can try creating a new environment called 'plotting' for running the GUI by entering the following commands:

conda create --name plotting python=3.7<br />
conda activate plotting<br />
conda install numpy<br />
conda install pandas<br />
conda install matplotlib<br />


currently works with module version:<br />
<br />
#pandas                    1.5.2           py311hf63dbb6_2    conda-forge<br />
#numpy                     1.24.1          py311h95d790f_0    conda-forge<br />
#matplotlib                3.6.2           py311h1ea47a8_0    conda-forge<br />


## screenshot of GUI as of 14-01-2023
![Alt text](/sxrdstructgui.png?raw=true "Optional Title")
