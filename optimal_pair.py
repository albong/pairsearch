#!/usr/bin/python2

#
# Based on the algorithm in Chapter 5 of Graham Kolesnik, for a specific problem
# Initial parts of algorithm checked by hand, only need repetitive part
#

from fractions import Fraction
import itertools
import sys

R = Fraction(829,1000) #approximation to Rankin's constant
EPSILON = Fraction(1,10000)
NUM_ITERATIONS = 100

#class to represent the theta function (ak + bl + c)/(dk + el + f)
class ThetaFunction:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def u(self):
        return (self.b * self.f) - (self.c * self.e)
    
    def v(self):
        return (self.a * self.f) - (self.c * self.d)

    def w(self):
        return (self.a * self.e) - (self.b * self.d)

    def applyA(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        e = self.e
        f = self.f
        return ThetaFunction(a+b+(2*c), b, b+(2*c), d+e+(2*f), e, e+(2*f))

    def applyBA(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        e = self.e
        f = self.f
        half = Fraction(1,2)
        return ThetaFunction(b, a+b+(2*c), b+(2*c)-half*(a+(2*c)), e, e+(2*f), e+(2*f)-half*(d+(2*f)))

    def evaluate(self, k, l):
        return Fraction(self.a*k + self.b*l + self.c, self.d*k + self.e*l + self.f)

def AProcess(k,l):
    return (Fraction(k, 2*k+2), Fraction(k+l+1, 2*k+2))

def BProcess(k,l):
    return (Fraction(2*l-1, 2), Fraction(2*k+1, 2))

def computePair(k, l, processString):
    currentPair = (k,l)
    instructions = processString[::-1] #reverse
    for i in range(0, len(instructions)):
        if instructions[i] == "A":
            currentPair = AProcess(*currentPair)
        elif instructions[i] == "B":
            currentPair = BProcess(*currentPair)
        else:
            return None
    return currentPair

def bruteSearchOptimalPair(kStart, lStart, theta, maxProcesses, pairRequirement):
    minimum = float("inf")
    choicePair = None
    processString = ""
    for j in range(0, maxProcesses + 1):
        allStrings = ["".join(seq) for seq in itertools.product("AB", repeat=j)]
        applicationStrings = [seq for seq in allStrings if "BB" not in seq] #B is an involution
        for i in xrange(0, len(applicationStrings)):
            pair = computePair(kStart, lStart, applicationStrings[i])
            try:
                exponent = theta.evaluate(*pair)
            except ZeroDivisionError:
                continue
            #if exponent < minimum and pair[1] == 2*pair[0]:
            if exponent < minimum and pairRequirement(*pair):
                minimum = exponent
                choicePair = pair
                processString = applicationStrings[i]
    return (minimum, choicePair, processString)

def printFlush(text):
    print text
    sys.stdout.flush()


#################################################
# Script start
#################################################
# (0, 1) #Trivial pair
# (Fraction(13, 84), Fraction(55,84)) #Bourgain's pair
# (Fraction(9, 56), Fraction(37, 56)) #Bombieri and Iwaniec's pair
# (Fraction(89, 560), Fraction(369, 560)) #Watt's pair

#theta = ThetaFunction(-1, 1, 1, -3, 2, 4)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:True)
#print minimum
#print pair
#print process
#
#print ""
#theta = ThetaFunction(-1, 1, 0, -3, 2, 1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:True)
#print minimum
#print pair
#print process

#theta = ThetaFunction(1, 0, 0, 1, 0, 1)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13, 84), Fraction(55,84), theta, 15, lambda k,l:l==2*k)
#print minimum
#print pair
#print process

#theta = ThetaFunction(0, 1, 0, 0, 1, 2)
#theta = ThetaFunction(1, 0, 0, 3, -1, 1)
#theta = ThetaFunction(1, 0, 0, 1, 0, 1)
#theta = ThetaFunction(Fraction(1,2), Fraction(1,4), 0, 1, 0, 1)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13, 84), Fraction(55,84), theta, 15, lambda k,l:l==2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(112455, 393844), Fraction(10231, 17902), theta, 15, lambda k,l:l>2*k)


#alpha = 9
#theta = ThetaFunction(alpha, 0, 1, 3*alpha, 0, alpha+1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:alpha*(l-2*k)==3)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:2*l-4*k-3<0)



#theta = ThetaFunction(Fraction(1,3), Fraction(1,3), 0, Fraction(4,3), -Fraction(2,3), 1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:True)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:True)

#theta = ThetaFunction(10,0,-1, 14,0,4)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l==2*k)
##minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l==2*k)

#GAMMA = Fraction(3,2)
#theta = ThetaFunction(1,0,0, 1+2*GAMMA,-1*GAMMA,1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 10, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l==2*k)

#theta = ThetaFunction(1,0,0, 3,-1,1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:True)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:True)

#x = Fraction(131101, 131083)
#y = Fraction(1, 131083)
#theta = ThetaFunction(1+2*y, -y, 0,  1+2*x, -x, 1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l<2*k)

#theta = ThetaFunction(4,-1,Fraction(3,2),  11,-5,3)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l<2*k)

x = Fraction(97,62)
y = Fraction(174,31)
#theta = ThetaFunction((1-2*x),x,0, (1-2*y),y,1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l>2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l>2*k)

#theta = ThetaFunction(4,1,0,  16,-5,6)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l<2*k)

#theta = ThetaFunction(1,4,0,  1,10,6)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:True)

#theta = ThetaFunction(0,1,0,  0,2,1)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:l<2*k)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:True)

#theta = ThetaFunction(4,-12,6, 9,-15,9)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:-3*k+5*l-3>0)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:-3*k+5*l-3>0)

#theta = ThetaFunction(1,0,Fraction(1,2), 3,-1,3)
#minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 15, lambda k,l:True)
#minimum, pair, process = bruteSearchOptimalPair(Fraction(13,84), Fraction(55,84), theta, 15, lambda k,l:l>2*k)

theta = ThetaFunction(2,0,2, 3,1,3)
theta = ThetaFunction(3,1,3, 2,0,2)
theta = ThetaFunction(Fraction(1,2),Fraction(1,2),-1, 0,0,1)
theta = ThetaFunction(0,2,-2, -1,0,-1)
theta = ThetaFunction(2,0,1, 2,-2,2)
theta = ThetaFunction(4,0,3, 2,-2,2)
theta = ThetaFunction(3,-1,2, 2,-2,2)
minimum, pair, process = bruteSearchOptimalPair(0,1, theta, 5, lambda k,l:True)

print minimum
print float(minimum)
print pair
print process

