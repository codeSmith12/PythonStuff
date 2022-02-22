
# name, price, ingredients, vegeterian


class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = " - VEGETARIAN"
        print(f"PIZZA {self.name} : {self.price}$" + veg_str)
        print(", ".join(self.ingredients))
        print()


class CustomPizza(Pizza):
    BASE_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    last_number = 0

    def __init__(self):
        CustomPizza.last_number += 1
        self.number = CustomPizza.last_number
        super().__init__("Custom " + str(self.number), 0, [])
        self.ask_user_for_ingredient()
        self.compute_price()

    def ask_user_for_ingredient(self):
        print()
        print(f"Ingredients for pizza number {self.number}")
        while True:
            ingredient = input("Add an ingredient (or press ENTER to finish) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def compute_price(self):
        self.price = self.BASE_PRICE + len(self.ingredients) * self.PRICE_PER_INGREDIENT


pizzas = [
    Pizza("4 cheeses", 8.99, ("blue cheese", "brie", "emmental", "mozarella"), True),
    Pizza("Hawai", 9.5, ("tomato", "pineapple", "oignon")),
    Pizza("4 seasons", 11, ("eggs", "tomato", "emmental", "ham", "olive")),
    Pizza("Vegetarian", 7.8, ("mushrooms", "tomato", "oignons", "bell pepper"), True),
    CustomPizza(),
    CustomPizza()
]


def pizza_sort(e):
    return len(e.ingredients)


# pizzas.sort(key=pizza_sort)

for i in pizzas:
    i.display()
