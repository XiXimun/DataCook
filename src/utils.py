

class Quantity:
    def __init__(self, name, unity):
            self.name = name
            self.unity = unity

   # def __init__(self, name_unity):
 #           [int(s) for s in str.split() if s.isdigit()]
            # self.name = name
            # self.unity = unity


class Ingredient:
    def __init__(self, name, quantity):
            self.name = name
            self.quantity = quantity


class Dish:
    def __init__(self, name):
            self.name = name
            self.ingredients = []
    
    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

class ShoppingList:
    def __init__(self, name):
            self.name = name
            
   # def addDish(self, ingredient):
