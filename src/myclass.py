
import pandas as pd
import sys

sys.path.append('/usr/local/lib/python3.10/dist-packages/')
from pycompss.api.task import task
from pycompss.api.parameter import INOUT, FILE_IN
from pycompss.api.api import compss_wait_on


class MyClass:
    def __init__(self):
        self.name = "MyClass"

    @task(returns=1, filepath=FILE_IN, target_direction=INOUT)
    def task1(self, filepath):
        data = pd.read_csv(filepath)
        data.dropna()
        return data
