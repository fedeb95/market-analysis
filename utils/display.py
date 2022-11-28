from utils.transform import Transform
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

class Display(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        """
        Interface that represents a displaying of a DataFrame.
        Calling apply results in some side effect: plotting, saving on disk, etc.
        The input DataFrame is always returned as passed.
        
        Parameters
        ----------
        df : DataFrame
            Input DataFrame
            
        Returns
        -------
        pandas.DataFrame

        """
        raise NotImplementedError

class Plot(Display):

    def __init__(self, plot):
        self.plot = plot

    def apply(self, df: DataFrame) -> DataFrame:
        colormap = plt.cm.nipy_spectral
        colors = colormap(np.linspace(0, 1, len(df.columns)))
        self.plot.set_prop_cycle('color', colors)

        self.plot.plot(df)
        self.plot.legend(df.columns)
        return df
