import os
import sys
import pandas as pd
from myclass import MyClass

sys.path.append('/usr/local/lib/python3.10/dist-packages/')
from pycompss.api.task import task
from pycompss.api.parameter import FILE_IN
from pycompss.api.api import compss_wait_on


@task()
def main():
    print(os.getcwd())
    filepath = '/home/eiraola/projects/tutorials/agents_delete_file/data/' \
               'res_mode1000_IDV0_9002.csv'
    instance = MyClass()
    data = instance.task1(filepath)
    data = compss_wait_on(data)
    print(data.head(), flush=True)


def read_file(filepath):
    """ Using this instead of a class method works normally. """
    data = pd.read_csv(filepath)
    data.dropna()
    return data


if __name__ == '__main__':
    main()
