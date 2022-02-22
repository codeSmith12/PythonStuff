# Display pizzas 1 pizza = 1 line
class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian
    def display(self):
        print()
        print(f"{self.name}: ${self.price}")
        for i in self.ingredients:
            print("\t-" + i)
        if self.vegetarian:
            print("\t-vegetarian")
        print()

class CustomPizza(Pizza):
    BASE_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    PIZZA_NUMBER=0

    def __init__(self):
        CustomPizza.PIZZA_NUMBER += 1
        self.number = CustomPizza.PIZZA_NUMBER
        super().__init__("Custom Pizza " + str(self.number), 0, [])
        self.askUserForIngredients()
        self.computePrice()

    def askUserForIngredients(self):
        print(f"\nIngredients for pizza #{CustomPizza.PIZZA_NUMBER}")
        while True:
            ingredient = input("Add an ingredient(or press enter to finish)")
            if ingredient == "":
                return

            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s): {', '.join(self.ingredients)}")

    def computePrice(self):
        self.price = self.BASE_PRICE + self.PRICE_PER_INGREDIENT * len(self.ingredients)


pizzas = [
    Pizza("4 cheeses", 8.99, ("blue cheese", "brie", "emmental", "mozarella"), True),
    Pizza("hawaiian", 12.99, ("canadian ham", "pineapple", "mozarella", "pepperoni")),
    Pizza("calzone", 9.99, ("canadian ham", "mozarella", "pepperoni")),
    Pizza("vegetarian", 11.99, ("mozarella", "olives", "bell peppers", "onions"), True),
    CustomPizza(),
    CustomPizza()
]
def sortByPrice(ele):
    return ele.price

def sortByIngAmt(ele):
    return len(ele.ingredients)

# pizzas.sort()
for pizza in pizzas:
    pizza.display()
def display(pizzas, numDisplay = -1):
    if numDisplay == -1:
        slices = pizzas
    else:
        slices = pizzas[:numDisplay]

    print(f"----- PIZZAS ({len(slices)}) -----\n")
    slices.sort()
    for pizza in slices:
        print(pizza)
    print("\n\n")
    try:
        print(f"First pizza: {slices[0]}")
        print(f"Last pizza: {slices[-1]}")
    except:
        print("There are no pizzas.")

def addPizza(pizzas):
    p = input("Add your pizza: ")
    if p.lower() in pizzas:
        print("Error: This pizza already exists")
    else:
        pizzas.append(p)


testPizza = []

# pizzas = ["4 cheese", "vegetarian", "hawaiian", "calzone", "four seasons"]
