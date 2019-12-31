import sys
from operator import itemgetter
# AIM : You are given a set of jobs. Each job i has a start time si and a  finish time fi. It also has a weight wi.
# Two jobs are compatible if their start-finish intervals don't overlap. The goal is to find the maximum weight
# subset of mutually compatible jobs (a subset with the maximum sum of weights).
# Run your program on the two inputs provided. You have to output only the maximum weight, not the
# actual subset. Each input file contains multiple lines, where each line contains three numbers describing a
# job: si; fi;wi. Each of these numbers is an integer between 1 and 200.
# Returns a list of list 
# input test file is a list with 
# start time (s(i)), finish time (f(i)) 
# and weight (w(i)).
# job = [job[s(1),f(1),w(1)],job[s(2),f(2),w(2)],
# .....job[s(n),f(n),w(n)]]

def load_inputtxt(filename):
    job = []
    with open(filename, "r") as file:
        for line in file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                job.append(line)
    return job

# Binary search will return  most optimal job
# that has start time less than the previous 
# jobs finish time
def binarySearch(job, start): 
  
    lo = 0
    hi = start - 1
    while lo <= hi: 

        mid = (lo + hi) // 2
        if job[mid][1] <= job[start][0]: 

            if job[mid + 1][1] <= job[start][0]: 
                lo = mid + 1
            else: 
                return mid 
        else: 
            hi = mid - 1
    # If optimal job not found
    return -1
  
# Return_max will return the most optimal job 
# from around its neighbours 
def return_max(job): 
    # Itemgetter imported from operations that returns 
    # the sorted jobs array according to the least finish time
    job= sorted(job, key=itemgetter(1))

    # Array weight_table[i] will store the weights of the ith job 
    
    n = len(job)  
    weight_table = [0 for _ in range(n)] 
    # adding job with the least finish time into 
    # the weight_table array  
    weight_table[0] = job[0][2]; 
   
    for i in range(1, n): 
  
        # If current job is included
        with_prof = job[i][2]
        l = binarySearch(job, i) 
        # If optimal job is not found
        if (l != -1): 
            with_prof += weight_table[l]; 
  
        # Find max weight from when a job is included and not included.
        weight_table[i] = max(with_prof, weight_table[i - 1]) 
    
    return weight_table[n-1] 
  

if __name__ == "__main__":

    job=load_inputtxt(sys.argv[1])
    print(return_max(job))

 