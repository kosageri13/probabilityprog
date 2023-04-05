# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""
# Task A. Convolution of a cube with weight function "U".

# A die is weighted in such a way that the probabilities of rolling 1, 2, 3, 4, 5, and 6 are 0.40, 0.15, 0.10, 0.05, 0.05, and 0.25, respectively. Calculate (using a program, but not by simulation, rather by using the convolution formula) the distribution of the sums of one, two, three, four, ten, and twenty die rolls, and then plot the weight functions. On the graph corresponding to the sum of twenty die rolls, draw the density function of a normal distribution that approximates the sum with a different color. Display these 6 graphs in a single window in a 2x3 arrangement.

# Hint: The convolution of k weight functions of dice can be determined from a dataset of size 6ᵏ, but a program written this way will not be able to run in time. I suggest calculating the convolution of the weight function recursively: for two dice, it can be obtained from the diagonally summed values of a 6x6 matrix, where the probability distribution has 11 elements. For three dice, convolve this weight function with the weight function of one die, which can be done using the diagonally summed values of a 6x11 matrix, and so on.
import matplotlib.pyplot as plt
def ufunc():
    p=[0.4, 0.15, 0.10, 0.05, 0.05, 0.25]
    one=[]
    a=0
    for i in p:
        a+=i
        one.append(a)
    # print(one)
    plt.subplot(2,3,1)
    plt.step(range(6), one)
    plt.title("1")
    two = []
    for i in p:
    	x = []
    	for j in p:
    		x.append(round(i*j,4))
    	two.append(x)
    d = [0]*11
    for i in range(6):
    	for j in range(len(two[i])):
    		d[i+j] += two[i][j]
    y = []
    b=0
    for i in d:
        b+=i
        y.append(b)
    plt.subplot(2,3,2)
    plt.step(range(11), y)
    plt.title("2")   
    three = []
    for i in p:
        x = []
        for j in d:
            x.append(round(i*j,4))
        three.append(x)
    d = [0]*16
    for i in range(len(three)):
    	for j in range(len(three[i])):
    		d[i+j] += three[i][j]
    y = []
    c=0
    for i in d:
        c+=i
        y.append(c)
    plt.subplot(2,3,3)
    plt.step(range(16), y)
    plt.title("3")
    four = []
    for i in p:
    	x = []
    	for j in d:
    		x.append(round(i*j,4))
    	four.append(x)
    d = [0]*21
    for i in range(len(four)):
    	for j in range(len(four[i])):
    		d[i+j] += four[i][j]
    u = []
    e=0
    for i in d:
        e+=i
        u.append(e)
    plt.subplot(2,3,4)
    plt.step(range(21), u)
    plt.title("4")
    for i in range(9):
    	ten = []
    	for j in p:
    		x = []
    		for k in p:
    			x.append(round(j*k,4))
    		ten.append(x)
    	d = [0]*(6+5*(i+1))
    for z in range(9):
        for i in range(len(ten)):
            for j in range(len(ten[i])):
                d[i+j] += ten[i][j]
        y=[]
        f=0
        for i in d:
            f+=i
            y.append(f)
    plt.subplot(2,3,5)
    plt.step(range(51), y)
    plt.title("10")   
    
    
    for i in range(19):
    	twenty = []
    	for j in p:
    		x = []
    		for k in p:
    			x.append(round(j*k,4))
    		twenty.append(x)
    	d = [0]*(6+5*(i+1))
    for z in range(19):
        for z in range(len(twenty)):
        	for s in range(len(twenty[z])):
        		d[z+s] += twenty[z][s]
    y=[]
    g=0
    for i in d:
        g+=i
        y.append(g)
    plt.subplot(2,3,6)
    plt.step(range(101), y)
    plt.title("20")
    plt.show()
        
