import random, time
myStudents = ["Caleb", "Ahrom", "Naoto", "Owen"]


for i in range(50):
    print(f"Is it going to be.... {random.choice(myStudents)}")
    time.sleep(.1)

print(f"I've chosen {random.choice(myStudents)}!!")

