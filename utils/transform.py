from pandas import DataFrame
import numpy as np

class Transform:
    def apply(self, df: DataFrame) -> DataFrame:
        raise NotImplementedError("this is just an interface")

class DropNa(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.dropna()

    def __str__(self):
        return "Drop nulls"
    
class LogDiff(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return np.log(df).diff()

    def __str__(self):
        return "Log Difference"

class Rolling(Transform):
    def __init__(self, window_length=250):
        self.window_length = window_length

    def __str__(self):
        return f"Rolling window of {self.window_length}"        

    def apply(self, df: DataFrame) -> DataFrame:
        return df.rolling(self.window_length)

class Mean(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.mean()

    def __str__(self):
        return "Mean"

class Variance(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.var()

    def __str__(self):
        return "Variance"
    
class StandardDeviation(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.std()
    
    def __str__(self):
        return "Std. Dev."
