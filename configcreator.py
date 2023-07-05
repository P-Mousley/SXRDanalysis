# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:12:16 2022

@author: rpy65944
"""

from PyQt5 import QtWidgets, uic
import sys
import pandas as pd
import numpy as np
import os, fnmatch
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.patches import Circle, Wedge, Polygon
#import SXRDplot as sxrdplot
#import SXRDfunction as sfunc



class StructurePlot(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(StructurePlot, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi(r"C:\\Users\\rpy65944\Documents\\GitHub\SXRDanalysis\configcreator.ui", self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = StructurePlot()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()