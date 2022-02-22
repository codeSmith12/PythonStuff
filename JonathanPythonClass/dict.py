# Part 1
person = {"name": "Paul", "age": 25, "height": 1.75}
print(person["name"])
for key in person:
    print(f"My {key} is {person[key]}")
# Part 2
# name, age, height
persons = [
    ("Alice", 25, 1.6),
    ("Brian", 28, 1.778),
    ("Paul", 35, 1.75),
    ("Martin", 32, 1.3)
]
def getInfo(name, lst):
    for i in lst:
        if i[0] == name:
            return i
    return None
infos = getInfo("Paul", persons) # Must iterate to get to paul
#print(infos)
personsDict = {
    "Alice": (25, 1.6),
    "Brian": (28, 1.8),
    "Paul": (35, 1.3),
    "Martin": (32, 1.8)
}
try:
    name="Jack"
    infos = personsDict[name] # DOESN'T ITERATE, IT GRABS INSTA (DIRECT ACCESS)
    print(infos)
except KeyError:
    print(f"{name} not found...")
