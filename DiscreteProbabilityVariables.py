# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""
# A. task. Discrete Probability Variables

# Create a class called Drv (discrete random variable) whose constructor expects two identical length lists: the first contains the monotonically increasing list of X probability variable xk values, the second contains the probabilities pk=P(X=xk). The following methods should be included:

# init: constructor with two member variables (xk and pk lists).

# pdf(x): X probability distribution (probability density function), returns the pk value if hax=xk, otherwise 0.

# cdf(x): X distribution function (cumulative distribution function), returns P(X<xk).

# e(): X expected value, i.e., E(X).

# is_nonneg(): returns True if X is non-negative, otherwise False.

# reweight(): returns a "reweighted" Y probability variable from X according to the formula P(Y=xk)=xk*pk/E(X) if X is non-negative and has at least one non-zero value.

# Binomial: a class derived from Drv for handling binomial distribution, which has two parameters, n and p. Override the e and is_nonneg methods.

# Uniform: a class derived from Drv for uniform distribution variables, with a single parameter n and a list of values [1,2,...,n]. Override the above methods.
import math

class Drv:
    """
    Define a class for discrete random variables

    xk is a list of monoton increasing values
    pk is the list of probabilities belonging to xk
    """

    name = "Discrete random variable"    # class variable

    def __init__(self, xk=[0], pk=[1]):
        self.xk = xk              # instant variable
        self.pk = pk                  # instant variable

    def pdf(self, x):
        """
        Return the value of the probability density function at x.
        x:: any real number
        """
        # TODO
        for i in range(len(self.xk)):
            if self.xk[i]==x:
                return self.pk[i]
        return 0
        pass 

    def cdf(self, x):
        """
        Return the value of the cumulative distribution function at x.
        x:: any real number
        """
        # TODO
        #P(X<xk)
        P=0
        for i in range(len(self.xk)):
            if self.xk[i]<x:
                P+=self.pk[i]
        return P
        pass

    def e(self):
        """
        Return the expected value of the discrete random variable.
        """
        # TODO
        l = len(self.xk)
        ex=0
        for i in range(l):
            a=self.xk[i]*self.pk[i]
            ex+=a
        return ex
            
        pass

    def is_nonneg(self):
        """
        Return True if the random variable is non negative.
        Otherwise False.
        """
        # TODO
        N=[]
        l=len(self.xk)
        for i in range(l):
            if self.xk[i]<0:
                N.append(1)
        if len(N)>0:
            return False
        else:
            return True
        pass # return here True or False

    def reweight(self):
        """
        Reweighting a random variable using the expected 
        value of the random variable. 
        """
        # TODO
        #P(Y=xk)=xk*pk/E(X)
        l = len(self.xk)
        ex=0
        for i in range(l):
            a=self.xk[i]*self.pk[i]
            ex+=a
        for i in range(len(self.xk)):
            self.pk[i]=(self.xk[i]*self.pk[i])/ex
        pass

    def __repr__(self):
        xk = self.xk
        pk = self.pk
        n = len(xk)
        x = '' . join(['('+str(xk[i]) + ', ' + str(pk[i]) + ') '
                      for i in range(min(n, 10))])
        if n > 10:
            x += '...'
        return self.name + ": " + x


class Binomial(Drv):
    """
    Class for binomial random variable derives from Drv.
    Parameters needed: n, p.
    """

    name = "Binomial random variable"

    def __init__(self, n=1, p=1):
        self.n = n
        self.p = p
        # TODO define the list of values and probabilities
        values=[]
        probabilities=[]
        for k in range(n+1):
            values.append(k)
            probabilities.append(abs(float(math.factorial(n)/(math.factorial(n-k)*math.factorial(k))*(p**k)*((p-1)**(n-k)))))
        # of the binomial variable
        super().__init__(values, probabilities) # inheritance

    def e(self):
        # TODO rewrite this function, as it can be calculated easier
        ex=self.n*self.p
        return ex
        pass # return the value here

    def is_nonneg(self):
        return True


class Uniform(Drv):
    """
    Class for a uniform random variable derives from Drv.
    n is the number a values (which are 1,2,...,n).
    """

    name = "Uniform random variable"

    def __init__(self, n=1):
        self.n = n
        # TODO
        values=[]
        probabilities=[1/self.n]*self.n
        for i in range(1,self.n+1):
            values.append(i)
        super().__init__(values, probabilities) # inheritance    
            
        # define the values and probabilities of the uniform variable here
        # and complete the code

    def e(self):
        """
        Return the expected value of the uniform random variable.
        """
        # TODO
        a=0
        for i in range(1,self.n+1):
            a+=i
        ex=a/(self.n)
        return ex
        pass # return the value here

    def is_nonneg(self):
        return True
    
    
