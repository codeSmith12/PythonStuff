'''
splitit, a program designed to do the math for you when wondering who pays
what of a bill.

'''
from os import system

class Item:
    def __init__(self, name, cost, amount, people):
        self.name = name
        self.cost = cost
        self.amount = amount
        self.people = people
        self.itemStr = []

    def __str__(self):
        self.itemStr = []
        topBar = "\n"+ "-"*width + "\n"
        botBar =  "-"*width+"\n"
        self.itemStr.append(topBar) # Top Bar
        costStr = str(self.cost)
        self.itemStr.append("|" + self.name.center(width-2) + "|\n")
        self.itemStr.append(botBar) # Top Bar
        self.itemStr.append("|" + str("Cost: $" + str(self.cost)).center(width-2) + "|")
        self.itemStr.append("\n|"+ str("Amount: "+ str(self.amount)).center(width-2) + "|")
        self.itemStr.append("\n|"+ str("Total: $"+ str(self.amount*self.cost)).center(width-2) + "|")
        self.itemStr.append(topBar) # Top Bar
        self.itemStr.append("|" + str("People sharing: " + str(len(self.people))).center(width-2) + "|")
        pricePerPerson = (self.amount*self.cost) / len(self.people)
        for person in self.people:
            self.itemStr.append("\n|" + person.center(width-2) + "|")
            persons[person] += pricePerPerson
        self.itemStr.append(topBar) # Top Bar

        self.itemStr.append("|" + str("Cost per: $" + str("{:.2f}".format(pricePerPerson))).center(width-2) + "|")
        self.itemStr.append(topBar) # Top Bar

        return "".join(self.itemStr)

width=35
items = []
moreItems = "y"
persons = {} # List with all people, may need for printing easily
bar = "-" * width
# Take in items, with their costs and amounts
while moreItems == 'y':
    morePeople = 'y'
    itemName = input("Item name: ")
    itemCost = float(input("Item cost: "))
    itemAmount = int(input("Amount of items:"))
    print("Enter names of those who had", itemName + ", seperated by commas: ")
    people = input()
    people = people.split() # Remove whitespace,
    people = "".join(people).split(',') # split into names into list, removing ','

    item = Item(itemName, itemCost, itemAmount, people)
    items.append(item)
    moreItems = input("Add another item? (y/n) ")
    # Make a list of each unique name entered.
    for person in people:
        if person not in persons:
            persons[person] = 0.0
taxAmount = float(input("Enter tax amount: $"))
taxPer = taxAmount / len(persons)
tipAmount = float(input("Enter tip amount: $"))
tipPer = tipAmount / len(persons)
discount = float(input("Enter any discount amount: $"))
print("Enter names of those who had received this discount, seperated by commas: ")
discountPeople = input()
discountPeople = discountPeople.split() # Remove whitespace,
discountPeople = "".join(discountPeople).split(',') # split into names into list, removing ','
discountPer = discount / len(persons)
for person in persons:
    if person in discountPeople:
        persons[person] -= discountPer
system('cls')
for item in items:
    print(item)

totalBill = 0
for item in items:
    totalBill += item.cost * item.amount

print(bar)
print("|"+ "Subtotal:".center(width-2) + "|")
print("|" + "${:.2f}".format(totalBill).center(width-2) + "|")
print(bar)

print(bar)
print("|"+ "Discounts:".center(width-2) + "|")
print("|" + "${:.2f}".format(discount).center(width-2) + "|")
for person in persons:
    if person in discountPeople:
        print("|" + "{}: ${:.2f}".format(person, discount).center(width-2) + "|")

print(bar)
print("|"+ "Tax Amount:".center(width-2) + "|")
print("|" + "${:.2f} / {} = {:.2f}".format(taxAmount, len(persons), taxPer).center(width-2) + "|")
print(bar)

print("|"+ "Tip Amount:".center(width-2) + "|")
print("|" + "${:.2f} / {} = {:.2f}".format(tipAmount, len(persons), tipPer).center(width-2) + "|")
print(bar)

totalBill += taxAmount + tipAmount - discount
print(bar)
print("|"+ "Total Bill:".center(width-2) + "|")
print("|" + "${:.2f}".format(totalBill).center(width-2) + "|")
print(bar)


print(bar)
print("|" + "Personal Totals".center(width-2) + "|")
print(bar)

for person in sorted(persons):
    personalTotal = str(person + " = " + str(persons[person]))
    print("|" +"{}: ${:.2f}".format(person, persons[person] + taxPer + tipPer).center(width-2) +"|")
print(bar)
exit = input("Press enter to exit.")
