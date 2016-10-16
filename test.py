##import sys*
##
##  print ("test")
##print('test' 'program')
##
##access ("test.txt")
##
##x = int(input("Please enter an integer: "))
##
##if x < 100
##    print ('this value 'x' is less than 1')
##else
##    print ('this value 'x' is less than 1')
##

import sys
import os
import time

print("test2");
data = input ("test : ")
file = open("read.txt" , "r")

#input data
if dc == "test" :
    print ("test abc")
else if dc != "abc" :
    print

##print ("test")
##print ("test2")
##
##voltage = [ 0.9 ,1.0 ,1.1]
##temperature = [ -40 ,25, 125]
##process =['ss' ,'nn', 'ff' ]
##
##for x in voltage :
##    for y in temperature :
##        for z in process :
##            print (voltage temperature 'process')
##
##
##marks = [90, 25, 67, 45, 80]
##
##number = 0
##for mark in marks:
##    number = number +1
##    if mark < 60: continue
##    print("%d번 학생 축하합니다. 합격입니다. " % number)
##
##    a = range (10)
##    a

##
##for i in range (1,9) :
##      for j in range (1,9) :
##        print ('%d * %d =' %i ,%j , i*j)
##
##        print ("")
##
##for i in range (1,10) :
##    sum = sum+i
##
##    print(sum)

##test = 0
##while test < 10 :
##    #print (test + '.' + 'test' )
##    print ('%d test' % test)
##    #print ('test')
##    test = test + 1


##i = int (input ("please insert 1 or 0)")
##if i  0 :
##    exit()
##elif i == 1 :
##    print ("this is operation")


##m = int(input("total count(m) : "))
##n = int(input("total title(m) : "))
##q = m//n
##p = m%n
##if p == 0 :
##    r = q
##else :
##    total_page = q + 1
##
##print ("total page" , total_page )

import math ,sys

def page (m ,n ) :
    if m%n != 0 :
        page_data =(m//n)+1
    else :
        page_data = m//n
    print(page_data)

page(int(sys.argv[1]),int(sys.argv[2]))

## file 입출력에 대한 전반적인 것
filename=input("Enter your file name : ")
tempfile=open(filename)
tempfile=tempfile.read()
temp_str=tempfile.replace("\t","    ")
tempfile=open(filename,'w')
tempfile.write(temp_str)
tempfile.close()

import re
import sys

def tab_to_space (file_name):
    source_code = file_name.read()
    change_code = source_code.replace("\t","    ")
    change_code = source_code.replace("\t","    ")
    source_code = open(file_name,'w')
    source_code.write(change.code)
    source_code.close()

    file_name.close()


##CLASS expression
    import unittest

def method1(str):
    return str.replace('\t', '    ')


class TestTab2Space(unittest.TestCase):
    def test_method1(self):
        str = "Hello\tMy Friend."
        self.assertEqual(method1(str), "Hello    My Friend.")

if __name__ == "__main__":
    unittest.main()

### Simple change

 댓 글  |  수 정  |  삭 제












0

 추천


def tab_to_space(text):
    return text.replace("\t", " " * 4)
