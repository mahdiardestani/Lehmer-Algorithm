"""
    Lehmer random number generator  Algorithm
 
"""

"""
formula of lehmer alghorithm

    X(K+1) = a * X[k] mod m
    a , m is constand 
    X[k] is seed to generate next random number
    
    I think this algorithm similar to 
    Linear Congruential Generator
    X[k+1] = (a*X[k]+c) mod m
"""

"""
formula of Run Test algorithm
    Z = (R - R_bar) / S
    R: The number of observed runs
    R_bar: The number of exThe number of expected runs, given as
        R_bar = ((2*n1*n2)/(n1+n2)) + 1
        n1: The number of positive values in the series
        n2: The number of negative values in the series
    S = Standard derivation of the number of runs
        S^2 = ((2*n1*n2)(2*n1*n2 - n1 - n2))/(((n1+n2)^2)(n1+n2-1))
    Compare the value of the calculated Z-statistic with Zcritical  
    for a given level of confidence 
    (Zcritical =1.96 for confidence level of 95%) 
    
"""

#Import Scope
#Import module time for lehmer 
import time
#Import math, statistics for run alghorithm 
import math 
import statistics 
#_______________________

#Define function Scope
def lehmer(num):
    result = []
    #get millis from time of system for initialzie seed
    millis = int(round(time.time()*1000))
    second = millis / 1000      #convert milli to micro
    #Modulo 
    mod = ((2**31) - 1)
    a = 43271       # I choose this value
    #Process
    result.append((a*second) % mod) #Make first seed
    for i in range(1, num):
        result.append((round(a*result[i-1])%mod))
    
    """
     We should create random numbers between 0 to 1
     for this problem I should normalize data
     Formula for normalizing data
     z = (x - min(x))/(max(x) - min(x))
    """
    
    max_num = max(result)
    min_num = min(result)
    print("Random numbers: ",end="\n")
    for i in range(len(result)):
        result[i] = ((result[i] - min_num) / (max_num - min_num))
        print(i+1, ":", result[i])
    return result

def runsTest(l, l_median): 
  
    runs, n1, n2 = 0, 0, 0
      
    # Checking for start of new run 
    for i in range(len(l)): 
          
        # no. of runs 
        if (l[i] >= l_median and l[i-1] < l_median) or  \
            (l[i] < l_median and l[i-1] >= l_median): 
            runs += 1  
          
        # no. of positive values 
        if(l[i]) >= l_median: 
            n1 += 1   
          
        # no. of negative values 
        else: 
            n2 += 1   
  
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/\
                         (((n1+n2)**2)*(n1+n2-1))) 
  
    z = (runs-runs_exp)/stan_dev 
  
    return z 
#______________________

#Input data from user
num = int(input("Enter the many of random numbers you want: "))

#Process
list_check = lehmer(num)
l_median = statistics.median(list_check)
Z = abs(runsTest(list_check, l_median)) 

#Print 
print('Check run test on random numbers: ', Z)
