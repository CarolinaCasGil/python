favorite_foods = ["pizza", "ice cream", "cheeseburgers"]
favorite_foods.insert(0, "pasta")
favorite_foods.append("sushi")

print("Ej 3 " + str(favorite_foods))
print("Ej 4 " + str(favorite_foods[1]))
print("Ej 5 " + str(favorite_foods[-1]))

favorite_foods[1] = "Lasania"
print("Ej 6 " + str(favorite_foods))

favorite_foods.__delitem__(-1)
print("Ej 7 " + str(favorite_foods))


numbers = list(range(1, 11))
print( "Ej 8 " + str(numbers))
print( "Ej 9 " + str(numbers[:5]))
print( "Ej 10 ")
for number in numbers:
    if number % 2 == 0:
        print(number)
print( "Ej 11 ")
for number in numbers:
    if number % 2 != 0:
        print(number)
print( "Ej 12 ")
for number in numbers:
    if number % 5 == 0:
        print(number)




# #################################################################################################################

