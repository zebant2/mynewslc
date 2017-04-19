__author__ = 'HP'


def breakfast(meal, *ingridients):
    """Function to make breakfast"""
    print("Gather ingredients")
    print("Mix the ingredients")
    print("Pour into the heated pan")
    print("Flip to the other side")
    available_ingredients = ""
    for argument in ingridients:
        available_ingredients += " "+ argument
        breakfast = "---Yummy " + meal + " with" + available_ingredients + "---"
    return breakfast

print(breakfast("Eggs", "Spinach", "Mustard"))
print(breakfast("Pancakes", "Syrup"))