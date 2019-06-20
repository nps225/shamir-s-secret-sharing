# Nikhil Sheth
# ID: 1577698
# CS42A
from fractions import Fraction
from random import shuffle
from random import randint;

def generateRandom(n): #generates a psuedo random number via a list
    list = [];
    for i in range(1,n):
        r = 0;
        while r == 0:
            r = randint(-1,1);

        list.append(i*r);

    shuffle(list);
    return list;

def split(val, n, k):
    random = generateRandom(1000);
    list = [];#this will contain ourlist of n random points
    poly = [];#this will contain the polynomial
    poly.append((0,val));
    for i in range(1,k):#iterate through generating random polynomial
        poly.append((i,random[i]));


    random = generateRandom(1000);
    for j in range(1,n+1):#this will ask for random points to find in poly
        total = 0;
        num = random[j];
        for (k,v) in poly:
            total += (num ** k) * v;#replace j with a random number
        list.append((num,total));
    return list;#return the list of tuples


def interpolate(points, x):
    secret = 0;# this will be our secret number
    for a,b in points: #iterate through points
        total = 1; #total will be our lgrange calc
        for a1, b1 in points:
            if a1 != a:#as long as it isn't the same point
                f = Fraction(x - a1,a - a1);
                total = total * f;

        total *= b;#multiply it by the coeff
        secret += total;#sum it all

    #print secret;
    return secret;
