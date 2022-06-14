import matplotlib.pyplot as plt
import numpy as np
infile_path = "./out.txt"

f = open(infile_path,"r").read().splitlines()
def str_arr_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


length_arr = np.array(str_arr_to_int(f[0].split(" ")))
wrong_arr = np.array(str_arr_to_int(f[1].split(" ")))
over_six_arr = f[2]

plt.scatter(length_arr,wrong_arr, alpha=0.1)
plt.show()