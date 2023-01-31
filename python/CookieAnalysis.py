#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
import MySort as mys

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = mys.MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    times = Sorter.InsertionSort(times)
    times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    #ADD CODE TO SORT THE ARRAY
    #ADD CODE TO CALCULATE QUANTILES 
    length = len(times)
    length_avg = len(times_avg)
print(length)
print(length_avg) 
arr= np.array(times)
arr_avg=np.array(times_avg) 
newarr= np.array_split(arr, 4)
newarr_avg=np.array_split(arr_avg, 4) 
print(newarr)
print(newarr_avg)
    #ADD CODE TO PLOT THE DATA FROM cookiedata.txt (matplotlib, uhhhh)
n, bins, patches = plt.hist(times_avg, 100, density=True, facecolor='b', alpha=0.80)
plt.xlabel('time')
plt.ylabel('num of trials')
plt.title('probability distribution')
plt.show()
plt.savefig('timerAvg.png')
    # ADD YOUR CODE TO PLOT times AND times_avg HERE


