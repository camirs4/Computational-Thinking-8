import os

#Beginning 

# # Mula_points = input
# Mario_points = input

# print("mula or mario quiz")
# input(" Do you go for personality put 1 or if you go for looks press 2")
# if 1:
#     Mula_points += 1 
#     if 2:
#         Mario_points += 1
cat_points = 0
dog_points = 0

os. system('clear')
answer = input("On a weekend would you rather A) nap all day,or B) go on a hike?\n")
if answer == "A":
    cat_points += 1
elif answer == "B":
    dog_points += 1

os. system('clear')
answer = input("On a weekend would you rather A) Watch tv or B) exercise\n")
if answer == "A":
    cat_points += 1
elif answer == "B":
    dog_points += 1

os. system('clear')
answer = input("what do you feel like more A) tired,or B) hyper?\n")
if answer == "a":
    cat_points += 1
elif answer == "B":
    dog_points += 1

os. system('clear')
answer = input("Is the glass A) half empty,or B)half full?\n")
if answer == "b":
    cat_points += 1
elif answer == "B":
    dog_points += 1

os. system('clear')
if cat_points > dog_points:
        print("You are a cat person")
elif dog_points > cat_points:
    print("You are a dog person")
elif cat_points == dog_points:
    print("You like cats and dogs the same")