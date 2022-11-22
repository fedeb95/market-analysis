from utils.transform import Transform
from pandas import DataFrame

class Compose(Transform):
    def __init__(self):
        self.transforms = []

    def then(self, t: Transform):
        self.transforms.append(t)        
        return self

    def clear(self):
        self.transforms = []
        return self

    def apply(self, df: DataFrame) -> DataFrame:
        for t in self.transforms:
            df = t.apply(df)
        return df

class ForkLeft(Transform):
    def __init__(self, t1: Transform, t2: Transform):
        self.t1 = t1
        self.t2 = t2

    def apply(self, df: DataFrame) -> DataFrame:
        self.t2.apply(df)
        return self.t1.apply(df) 
