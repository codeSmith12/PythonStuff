import random

secret = random.randint(50, 100)

ages = []

numStudents = int(input("How many students are participating?"))

for i in range(numStudents):
    age = int(input("How old are you?"))
    