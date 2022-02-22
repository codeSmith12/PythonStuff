class Pizza:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
    def display(self):
        print(f"\n{self.name}: ${self.price}")
        print(f"{self.ingredients}")

class CustomPizza(Pizza):
    BASE_PRICE = 7.99
    PRICE_PER_INGREDIENT = .79
    def __init__(self):
        super().__init__("Custom Pizza", 0, [])
        self.askUserForIngredients()
        self.computePrice()
    def askUserForIngredients(self):
        print("\nIngredients for Custom Pizza:")
        while True:
            ingredient = input("Add an ingredient, press enter when finished.")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s): {', '.join(self.ingredients)}")
            # Try to change the format of self.ingredients so it doesn't show the [''] stuff
            # Use join to do the above!!
            #
    def computePrice(self):
        pass

pizza1 = Pizza("4 cheeses", 6.99, ["fromage blanc", "mozzarella", "cheddar", "pepperjack"])
pizza2 = Pizza("hawaiian", 11.99, ["mozzarella", "canadian bacon", "pineapple"])
pizza3 = Pizza("pepperoni", 7.99, ["pepperoni", "mozzarella"])
pizza4 = Pizza("bbq chicken", 8.99, ["bar-b-que sauce", "chicken strips", "mozzarella", "red onion"])
pizza5 = Pizza("veggie", 10.99, ["mozzarella","tomatoes", "onions", "olives", "artichokes", "spinach", "basil"])

customPizza1 = CustomPizza()

menu = [
    pizza1,
    pizza2,
    pizza3,
    pizza4,
    pizza5
]

def sortByPrice(ele):
    return ele.price


menu.sort(key=sortByPrice)

for item in menu:
    item.display()

# How can i iterate through each menu and print its name and corresponding price?
