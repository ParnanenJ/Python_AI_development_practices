italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagne"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals:")
    for name in italian_food:
      print(name)
  elif food_type == "Indian":
    print("Available Indian Meals:")
    for name in indian_food:
      print(name)
  else:
    print("Invalid food type")
  
def create_summary(name, amount, food_type):
  order = select_meal(name, type_input)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input = input("What type of food you like to order: ")
display_available_meals(type_input)
name_input = input("Choose your meal: ")
amount_input= input("quantity: ")

result = create_summary(name_input, amount_input, type_input)
print(result)