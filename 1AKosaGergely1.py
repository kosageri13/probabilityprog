# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:48:58 2022

@author: User
"""
# Task A. Risk.

# In the board game called Risk, during one round of combat, a player can attack with a maximum of three soldiers while the defending player can defend with a maximum of two soldiers. When there are three attackers and two defenders, the battle takes place as follows: The attacking player rolls three red dice, while the defending player rolls two blue dice. Then, we compare the highest roll of the attacker with the highest roll of the defender. The player with the lower value loses one soldier. In the case of a tie, the defender wins, and the attacker loses one soldier. Then, we compare the second-highest rolls of each player in the same way. Thus, there are three possible outcomes of the battle: the attacker loses two soldiers, there is a tie (each player loses one soldier), or the defender loses two soldiers.

# Simulate the experiment 1000 times and determine the relative frequency of the three outcomes.
# Simulate the experiment 1000000 times and determine the relative frequency of the three outcomes.
# Calculate the exact probabilities of the three outcomes by examining all possible cases. The probability is the ratio of favorable cases to all cases.
# Display these results with an accuracy of 5 decimal places, separated by 3 spaces. The output of the program should look like this (with different numbers, of course):

# yaml
# Copy code
#                                Attacker Tie Defender
#   1000 experiments:      0.35200   0.44400   0.20400
#   1000000 experiments:   0.33988   0.43011   0.23001
#   Probability:           0.34000   0.43000   0.23000
import random

def simulate(N):
    T=0
    V=0
    D=0
    for i in range(0,N):
        Piros=3
        Kék=2
        p1=random.randint(1,6)
        p2=random.randint(1,6)
        p3=random.randint(1,6)
        v1=random.randint(1,6)
        v2=random.randint(1,6)
        P=sorted((p1,p2,p3))
        t1=P[2]
        t2=P[1]
        K=sorted((v1,v2))
        k1=K[1]
        k2=K[0]
        if t1>k1:
            Kék-=1
        elif t1==k1:
            Piros-=1
        elif k1>t1:
            Piros-=1
        if t2>k2:
            Kék-=1
        elif t2==k2:
            Piros-=1
        elif k2>t2:
            Piros-=1
        
        if Piros==3 and Kék==0:
            T+=1
        elif Piros==2 and Kék==1:
            D+=1
        elif Piros==1 and Kék==2:
            V+=1
            
    return (T/N,D/N,V/N)

from itertools import product
def probability():
    T=0
    V=0
    D=0
    piros=product([1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6])  
    for i in list(piros):   
        t1=sorted(i)[2]
        t2=sorted(i)[1]
        kek=product([1,2,3,4,5,6],[1,2,3,4,5,6])
        for j in list(kek):
            k1=sorted(j)[1]
            k2=sorted(j)[0]
            P=3
            K=2
            if t1>k1:
                K-=1
            elif t1==k1:
                P-=1
            elif k1>t1:
                P-=1
            if t2>k2:
                K-=1
            elif t2==k2:
                P-=1
            elif k2>t2:
                P-=1
            if P==3 and K==0:
                T+=1
            elif P==2 and K==1:
                D+=1
            elif P==1 and K==2:
                V+=1
    
    return (T/6**5,D/6**5,V/6**5) #az esetek számát T,D,V -t kiírva és a darabszámokat összeadva kaptam meg
            
    
def main():
    print(f"                                       Támadó     Döntetlen  Védő")
    s = simulate(1000)
    print(f"Relatív gyakoriság 1000 kísérletből:   {s[0]:.5f}    {s[1]:.5f}    {s[2]:.5f}")
    z = simulate(100000)
    print(f"Relatív gyakoriság 100000 kísérletből: {z[0]:.5f}    {z[1]:.5f}    {z[2]:.5f}")
    print(f"Valószínűség:                          {probability()[0]:.5f}    {probability()[1]:.5f}    {probability()[2]:.5f}")
            
if __name__ == "__main__":
    main()
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
 
            
            
        
            
      
    
    


            
        
            
            
    
        
        
        
        
    
    