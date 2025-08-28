'''
Python Level 3 - Lesson 3 - File I/O & String Manipulation

Objectives:
    - Learn the tools provided by Python to open files in read, write and append modes
    - Discuss different methods for retreiving information from files, readline, readlines, ect
    - Show students how easily Python can manipulate strings (strip, split, slice)
    - Demonstrate the method they will be using for our game
    - (optional) Show how to write to a file (most of our stuff is being read from, only writing at the very end)

Tasks:
    - Discussion about files. Why is it useful to be able to read and write to files?
    - I/O Methods in Python
    - Practice splitting strings by ','s
    - Create a text file and add some data in it. Name and Score (add it to the same folder the python code is in)
    - Talk about why we need to be very careful about the path to our text file, show proper steps of safety
    - Read lines in, print them. Then challenge students to split the data
    - Have students add data into objects
    - Objects should be displayed just like they were in the previous lesson, just now they come from a file
    
Homework:
   Students will be given 1-3 text files with data in them. The goal of the student is 2 part:
   1. Read in the data, making sure to split at every ','
   2. Create their own custom class that will hold each bit of data
   
   For example:
   
   data.txt - Name and Scores
   Brian, 1020223
   Ashima, 2034455
   
   class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
'''