import random
import sys
#print ("test program")

def main ():
    print ("hello world")
    randomNum = 35
    found = False
    GuessNum = input ("input random number: ")
    while not found :
    if GuessNum == randomNum :
        print ("you are right")
        found = True
    else if GuessNum > randomNum :
        print ("you have big num")
    else if GuessNum < randomNum :
        print ("you have small num")

if __name__ == "__main__":
    main()


def myabs(x) :
    if x < 0 :
        x = -x
        return x

def mysum(a ,b) :
    sum = a+b
    return sum

def mymin(a ,b) :
    min = a-b
    return min

def mymulti(a ,b) :
    multi = a*b
    return multi

abs_data = myabs(-10)
