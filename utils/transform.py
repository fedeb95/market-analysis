from pandas import DataFrame
import numpy as np

class Transform:
    def apply(self, df: DataFrame) -> DataFrame:
        raise NotImplementedError("this is just an interface")

class DropNa(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.dropna()
    
class LogDiff(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return np.log(df).diff()

class Rolling(Transform):
    def __init__(self, window_length=250):
        self.window_length = window_length

    def apply(self, df: DataFrame) -> DataFrame:
        return df.rolling(self.window_length)

class Mean(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.mean()

class Variance(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.var()
    
class StandardDeviation(Transform):
    def apply(self, df: DataFrame) -> DataFrame:
        return df.std()
    
