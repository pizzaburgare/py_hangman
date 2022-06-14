import matplotlib.pyplot as plt
import numpy as np
import scipy
infile_path = "./out.txt"

f = open(infile_path,"r").read().splitlines()
def str_arr_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


length_arr = np.array(str_arr_to_int(f[0].split(" ")))
wrong_arr = np.array(str_arr_to_int(f[1].split(" ")))
over_six_arr = f[2]

# pie charts per length
def pie_charts():
    different_lengths = len(np.unique(length_arr))
    for i in range(different_lengths):
        current_length = np.unique(length_arr)[i]
        temp_wrong_arr = []
        temp_length_arr = []
        for j in range(len(length_arr)):
            if length_arr[j] == np.unique(length_arr)[i]:
                temp_wrong_arr.append(wrong_arr[j])
                temp_length_arr.append(length_arr[j])

        temp_wrong_arr = np.sort(np.array(temp_wrong_arr))
        temp_length_arr = np.sort(np.array(temp_length_arr))

        x = []
        y = []
        for j in range(len(np.unique(temp_wrong_arr))):
            # Add one of each eg 1,2,4,5
            x.append(np.unique(temp_wrong_arr)[j])
            y.append(0)
        for j in range(len(temp_wrong_arr)):
            #x:[2,3,4,5,6,7]
            #y:[0,1,5,1,0,0]
            place = x.index(temp_wrong_arr[j])
            y[place] = y[place] + 1

        print(current_length)
        plt.subplot(5,5,i+1)
        plt.pie(y,labels=x)
        plt.title(np.unique(length_arr)[i])
    plt.show()

pie_charts()

plt.figure()
plt.title("ScatterPlot fails of word length")
plt.scatter(length_arr,wrong_arr, alpha=0.1)
plt.show()