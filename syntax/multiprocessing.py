#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  usr/bin/Geany/Multiprocess.py  
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Attributions :
# https://www.geeksforgeeks.org/python-absolute-value-of-list-elements/
# https://www.skillsyouneed.com/num/positive-negative.html
# https://kite.com/python/answers/how-to-subtract-a-value-from-every-number-in-a-list-in-python
# https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print

## My IO ## Visit https://www.youtube.com/watch?v=3llnfHGN9HM to Download Fast IO template ##

## Fast IO Section ##
import sys
import time

def inp():  # Single Input
    return(int(sys.stdin.readline()))
def invr():  # Multi Input Integers
    return(map(int,sys.stdin.readline().split()))
def stp():  # Multi Input Strings
	return(map(str,sys.stdin.readline().split()))
def fprint(x):  # Fast Print
	sys.stdout.write(str(x))
	sys.stdout.flush()

## Code Section ##	

def tx1():
	print("Thread 1 Completed")  # Write Your Heavy Calcuations Here
def tx2():	
	print("Thread 2 Completed")  # Write Your Heavy Calcuations Here
	
## Threading Section ##	

if __name__ == "__main__":
	import multiprocessing
	print("Available Threads :",multiprocessing.cpu_count())
	p1 = multiprocessing.Process(target=tx1, args=()) 
	p2 = multiprocessing.Process(target=tx2, args=()) 
	p1.start()
	p2.start() 
	p1.join() 
	p2.join()
	print("Main Calculations Done Parallelly, Now Continue Program")

## Code Section ##

if __name__ == "__main__":   # You can erase this line, but continue with indentation
	print("Continuing....")