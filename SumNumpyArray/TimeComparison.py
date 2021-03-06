import numpy as np
from SumArray import SumArray
from SumArrayParallel import SumArrayParallel

Array1 = np.random.rand(int(1e8))
Length1 = len(Array1)

import time

def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return retval
    return wrapper

@time_usage
def SumSpeedTest(Method, Array, Length):
    if Method == "python":
        return sum(Array)
    if Method == "numpy":
        return np.sum(Array)
    if Method == "c++":
        return SumArray.C_SumArray(Array, Length)
    if Method == "c++OpenMP":
        return SumArrayParallel.C_SumArray(Array, Length)

Result = SumSpeedTest("python", Array1, Length1)
print(Result)
Result2 = SumSpeedTest("numpy", Array1, Length1)
print(Result2)
Result3 = SumSpeedTest("c++", Array1, Length1)
print(Result3)
Result4 = SumSpeedTest("c++OpenMP", Array1, Length1)
print(Result4)

#%timeit sum(Array1)
#%timeit np.sum(Array1)
#%timeit SumArray.C_SumArray(Array1, Length1)
