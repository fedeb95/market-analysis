from utils.transform import Transform
from pandas import DataFrame

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
        self.plot.plot(df)
        return df
