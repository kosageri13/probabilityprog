# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Aláírás Teljes Névvel
"""
# Task A. Binomial distribution.

# In this task, you need to draw three column diagrams on one chart, each with its own title.
# The first chart shows the probability distribution of a binomial distribution with parameters (n,p) (title: "Binomial distribution").
# The second chart shows the empirical probability distribution of simulating this binomial distribution (title: "Simulation of binomial distribution").
# The simulation of the binomial distribution can be done by performing n experiments for the number of times an event with a probability of p occurs. The value of the probability variable is m if the event occurs m times out of n experiments. We repeat these n experiments k times, so we get k values for the probability variable. The m-th column of the second diagram should be i/k high if the probability variable took on the value of m i times.
# The third diagram shows the first n+1 columns of the probability distribution of a Poisson distribution with parameter λ=np, which approximates the binomial distribution (title: "Approximation with Poisson distribution"). The probability distribution of a Poisson distribution with parameter λ is

# The input of the program is n, p, k, where n and p are the parameters of the binomial distribution, and k is the number of simulations.

import math
import random 
import matplotlib.pyplot as plt
import sys  
def comb(n, m):
    return math.factorial(n)//math.factorial(m)//math.factorial(n-m)


n=int(sys.argv[1])
p=float(sys.argv[2])
K=int(sys.argv[3])
A=[]
B=[]
C=[]
N=[]
for i in range(n+1):
    N.append(i)
    a=comb(n, i)*(p**(i))*((1-p)**(n-i))
    A.append(a)
M=[]
for j in range(K):
    m=0
    for _ in range(n):
        e=p
        f=1-p
        v=[1,2]
        b=random.choices(v, weights=(e,f),k=1)
        if b==[1]:
            m+=1
    M.append(m)
for s in range(n+1):
    g=0
    for z in M:
        if s==z:
            g+=1
    B.append(g)
for r in range(n+1):
    c=(((n*p)**r)*(math.exp(n*p)))/(math.factorial(r))
    C.append(c)
    #return M,B,C
#return len(A),len(B),len(C),len(N)
#return A,B,C
# if 4==len(sys.argv):
#     n = int(sys.argv[1])
#     p = float(sys.argv[2])
#     K = int(sys.argv[3])
print(plt.figure(figsize=(12, 3)),

         plt.subplot(131), # 1 sorból és 3 oszlopból álló ábra első részábrája
         plt.bar(N,A),
         plt.title('Binomilális eloszlás'),
         plt.subplot(132), # 1 sorból és 3 oszlopból álló ábra második részábrája
         plt.bar(N,B),
         plt.title('Binomiális eloszlás szimulációja'),
         plt.subplot(133), # 1 sorból és 3 oszlopból álló ábra második részábrája
         plt.bar(N,C),
         plt.title('Közelítés Poisson eloszlással'),
        
         plt.tight_layout(),
         plt.show())

    
        
    
        
            
                
            
                
                
                              
    
    
                
            
            