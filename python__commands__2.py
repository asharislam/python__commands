#####################################################
############## Numbers ###########################
################################################

######## Integers
#print(2+4)
#message = 4+5
#print(message)
############# Floats
#print(0.1 + 0.3)

#Underscore in number
#universe_age = 14_000_000_000
#print(universe_age)

#Multiple Assignment
#x, y, z = 4, 5, 6
#print(x)
#print(y)
#print(z)
#x, y, z = "hello world", "hello Bangladesh", "Hello Python Bangladesh"
#print("Result of x:", x)
#print("Result of y:", y)
#print("Result of z:", z)
#print(f"x: {x}, y: {y}, z: {z}")
#print("{} {} {}".format(x, y, z))
#print("{}{}{}".format(y, z, x))

###CONSTANTS
#Use all capital letters for using constrant
#MAX_CONNECTIONS = 500

######Comment
# this is comment writing systen
"""This also comment writing system"""

##########################################################
###################### List ############################
#######################################################

#The symbol of list writing system like []
#bicycles = ["trek", "connondale", "redline", "specialized"]
#print(bicycles)
#this is a list of bicycle

###Index ##
#Index position start at 0, not 1
#print(bicycles[1])
#print(bicycles[0])
#print(bicycles[2])
#print("list First item is: ", bicycles[0])
#here we can use also title(), upper()
#print("The second item is : ", bicycles[1].upper())
# This method we can use for accessing any data from list
#we can also find a string value from a list
#name = "Ashar Islam"
#print(name[1])
#you can use also insex from reverse
#print(name[-1])

########### using individual values from list
#bicycles = ["trek", "connondale", "redline", "specialized"]
#message = f"My first bicycle was a {bicycles[0].title()}."
#print(message)

#motorcycles = ["honda", "yamaha", "suzuki"]
#print(motorcycles)
#replace item using index
#motorcycles[0] = "ducati" 
#print(motorcycles)

#add any item to the list using append
#motorcycles = ["honda", "yamaha", "suzuki"]
#motorcycles.append("ducati")
#print(motorcycles)

#also we can use a empty list for append somethings
#motorcycles = []
#motorcycles.append("honda")
#motorcycles.append("yamaha")
#motorcycles.append("suzuki")
#print(motorcycles)

#Insert ing element into a list using append with index
#motorcycles = ["honda", "yamaha", "suzuki"]
#motorcycles.insert(0, "ducati")
#print(motorcycles)
#motorcycles.insert(2, "royal")
#print(motorcycles)

####Remove element from a list using delete method(del)
#motorcycles = ["honda", "yamaha", "suzuki"]
#print(motorcycles)
#del motorcycles[0]
#print(motorcycles)
#del motorcycles[1]
#print(motorcycles)

#Remove item using pop() method
#motorcycles = ["honda", "yamaha", "suzuki"]
#print(motorcycles)
#print(motorcycles.pop())
#poped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(poped_motorcycle)

#poping items from any position in a list
#motorcycles = ["honda", "yamaha", "suzuki"]
#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle i owned was a {first_owned.title()}.")

#Removing an item by value
#motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
#print(motorcycles)
#motorcycles.remove("ducati")
#print(motorcycles)

#motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
#print(motorcycles)
#too_expensive = "ducati"
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print(f"\n {too_expensive.title()} is too expensive for me.")

#organizing a list
#sort is use for serial by alphabet abcdefg
#cars = ["bmw", "audi", "toyota", "subaru"]
#cars.sort()
#print(cars)

#sort a list Temporarily
#cars = ["bmw", "audi", "toyota", "subaru"]
#print(f"print here the orginal list{cars}")
#print(f"print here the sorted list{sorted(cars)}")

#printing a list using reverse order
#reverse order completly reverse your list
#cars = ["bmw", "audi", "toyota", "subaru"]
#print(cars)
#cars.reverse()
#print(cars)

#Finding a length of a list
#cars = ["bmw", "audi", "toyota", "subaru"]
#print(len(cars))
#name = "Ashar Islam"
#print(len(name))
#print(name[1])




#####################################################
########### working with list####################
#####################################################
#page - 49

### lopping an entire list by individual
### using for loop
#magicians = ["alice", "david", "carolina"]
#for magician in magicians:
#    print(magician)
# mostlu use that:
# for cat in cats:
# for dag in dogs:
# for item in list_of_items:

#### Doing more work by for loop
# for this list , printing output will be in individual line for all items.
#magicians = ["alice", "david", "carolina"]
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
    
#magicians = ["alice", "david", "carolina"]
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#doing something agter a for loop
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#print("Thank you, everyone. That was a great magic show!") 
#this line we using in first line because
#when finished first condition then printing last condition.

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#print(f"I can't wait to see your next trick, {magician.title()}.\n")
#in last print there will be use carolina because
#python use last update here last magician is carolina
#54 page

 ########
 ######### Making Numerical list
 #########  57
###range() function############

#for value in range(1, 5):
#    print(value)
#for num in range(1, 4):
#    print(num)
#numbers = list(range(1, 6))
#print(numbers)
#this system is not for fictionary because
# dictionary have value but there have no value
#print(even_numbers)
#odd_numbers = list(range(1, 10, 2))
#print(odd_numbers)

#squares = []
#for value in range(1, 11):
#    square = value ** 2
#    squares.append(square)
#print(squares)
### page 58

#cubes = []
#for cube in range(1, 11):
#    cube = cube ** 3
#    cubes.append(cube)
#print(cubes)

#powers_four = []
#for power_four in range(1, 11):
#    power_four = power_four ** 4
#    powers_four.append(power_four)
#print(powers_four)

#powers_five = []
#for power_five in range(1, 11):
#    power_five = power_five ** 5
#    powers_five.append(power_five)
#print(powers_five)

###### simple statistics with a numbers
#digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#print(min(digits))
#print(max(digits))
#print(sum(digits))

################# List Comprehensions ###
#comprehensions means in one line situate all value
#squares = [value ** 2 for value in range(1, 11)]
#print(squares)

################### Working  with part of a list
###########
#page - 61
### Slicing a list
#players = ["charles", "martina", "michael", "florence", "eli"]
#print(players[0:3]) 
#here 0,1,2 is slicing in the list 
#print(players[1:4])
#here 1,2,3 is slicing
#print(players[2:])
#index 2 to all index
#print(players[:3])
#print(players[-3:])

#lopping through a slice
#players = ["charles", "martina", "michael", "florence", "eli"]
#print("Here are the first three players on my team:")
#for player in players[:3]:
#    print(player.title())

#copying a list
#my_foods = ["pizza", "falafel", "carrot cake"]
#friend_foods = my_foods[:]
#print(friend_foods)
#print(my_foods)
#print(f"my favorite foods are:{my_foods}")
#print(f"my friend's favorite foods are : {friend_foods}")
#my_foods.append("cannoli")
#friend_foods.append("ice cream")
#print(my_foods)
#print(friend_foods)



########## Tuples
#tuple is define over the first braket
#dimentions = (200, 50)
#print(dimentions[0])
#print(dimentions[1])
# first braket, 
#output show in the first braket

# applying loop ing tuple
#dimentions = (200, 50)
#for dimention in dimentions:
#    print(dimention)
#    printing values without first braket by for loop
#print(dimentions)

#writing over a tuple
#dimensions =(200, 50)
#print("Orginal dimensions: ")
#for dimension in dimensions:
#    print(dimension)
#
#dimensions = (400, 100)
#print("\nModified dimension: ")
#for dimension in dimensions:
#    print(dimension) 


####################################################
############# IF Statements ######################
################################################
#page - 71
# FOR IF ELSE 
#cars = ["audi", "bmw", "subaru", "toyota"]
#for car in cars:
#    if car == "bmw":
#        print(car.upper())
#    else:
#        print(car.title())

#cars = ["audi", "bmw", "subaru", "toyota"]
#for car in cars:
#    if car == "bmw":
#        car = car.upper()
#        print(car)
#    else:
#        car = car.title()
#        print(car)
    
#### checking for inequality
#requested_topping = "mushrooms"
#if requested_topping != "anchovies":
#    print("Hold the anchovies")

###############################################input
### input system
# input("write here something")
#name = input("plese enter your name : ")
#print(name)

#name = input("what is your name: ")
#age = int(input("you age please: ")) 
#if age >= 18:
#    print(f"Hello {name}! your age is {age} and you are adult to enter the club.")
#else:
#    print(f"Hello {name}! your age id {age} and you are not adult for get entry to the club")


###numerical comparisons
#answer = 17
#if answer != 42:
#    print("That is not the correct answer. please try again!")

####################################
### checking multiple condition
### and
#and meanse plus that meanse when satisfy all condition the ipesific result willbe printing
#age = int(input("please enter your age: "))
#if age<18 and age<10 and age<5:
#    print("hey baby")
#else:
#    print("Hello sir")

### or
# if one codition is satisfied then output will be print
#age = int(input("please enter your age: "))
#if age<18 or age<10 or age<5:
#    print("hey baby")
#else:
#    print("Hello sir")

# checking whether a value is in a list or not using input method
#aviable_product = ["pant", "shirt", "tshirt"]
#user = input("Hello what kind of product you what: ")

#if user in aviable_product:
#    print("Hello sir your producr is aviable")
#else:
#    print("sorry sir your product is not aviable in our stock")
#    print("sir our aviable product list is given: ")
#    for aviable_products in aviable_product:
#        print(aviable_products)


############################################
######### IF STATEMENT ###################
#page - 78
#if conditional_test
#   do something or pass
# page 79
### if statements
#age = int(input("please enter your age: "))
#if age>=18:
#    print(f"your age is {age}!, which is old enough to vote!")

#if-else statement
#if age is under 18 then we will use else
#age = int(input("please enter your age: "))
#if age>=18:
#    print(f"your age is {age}!, which is old enough to vote!")
#else:
#    print(f"your age is {age}!, which is not enough to vote")

#if-elif-else chain
# there will be more then 2 different condition situate 
#age = int(input("please enter your age: "))
#if age<4:
#    print("need't your admission cost.")
#elif age>4 and age<10:
#    print("print your admision cost is 10taka")
#elif age>10 and age<=18:
#    print("your admision cost is 20 taka")
#else:
#    print(f"your age is {age}, we do not take admision upto 18")

#omiting the else block
#age = int(input("please enter your age: "))
#if age<4:
#    print("need't your admission cost.")
#elif age>4 and age<10:
#    print("print your admision cost is 10taka")
#elif age>10 and age<=18:
#    print("your admision cost is 20 taka")
#elif age>18 and age<100:
#    print("sorry")

#using if statements with lists
#requested_toppings = ["mushrooms", "green pepers", "extra cheese"]
#for requested_topping in requested_toppings:
#    print(f"adding {requested_topping}")
#print("\nFinished making your pizza")

#checking that a list is not empty
#requested_toppings = []
#if requested_toppings:    
#    for requested_topping in requested_toppings:
#        print(f"adding {requested_topping}")
#    print("\nFinished making your pizza")
#else:
#    print("are you sure you want a plain pizza")

#########################################################
############### DICTIONARIES ###########################
#########################################################
####### page -91
#dictionary must have key and value
#without key value this will not be define as dictionary

#a simple dictionary
#print(alien_0["color"])
#print(alien_0["points"])
#here color is key and green is value 
#and points is key and 5 is value

##Accessing value in a dictionary
##page - 93
#alien_0 = {"color": "green"}
#print(alien_0["color"])
#x = alien_0["color"]
#print(f"your selected color is {x}")

#colors = {"color_1":"green", "color_2": "red", "color": "blur"}
#print(colors)
#for color in colors:
#   print(color)
#

#Adding new key_value pairs
#alien_0 = {"color": "green", "points": 5}
#print(alien_0)
#alien_0["x_position"] = 0
#alien_0["y_position"] = 25
#print(alien_0)

#adding using input
#details ={}
#name_s  = input("please give me your name: ")
#class_s = input("what class do you read: ")
#id_s    = input("give me your ID please: ")
#details["name"] = name_s
#details["class"] = name_s
#details["id"] = name_s
#print(details)

#modifying values in a dictionary
#alien_0 = {"color": "green"}
#print(f"The alien is {alien_0['color']}")
#here uses 'color' because in "" under use '' not ""
#alien_0["color"] = "yellow"
#print(f"The alien is now {alien_0['color']}")

##removing key-value pairs
#alien_0 = {"color": "green", "points": 5}
#print(alien_0)
#del alien_0["points"]
#print(alien_0)
# page -96

#page- 97
#dictionary of similar object
#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
#language = favorite_language["sarah"].title()
#print(f"sarah's favorite language is {language}")

#usig get() to access values
#alien_0 = {"color": "green", "speed": "slow"}
#point_value = alien_0.get("points", "No point value assigned")
#print(point_value)

#Looping through a dictionary
#page -99
#user_0 = {
#    "username": "efermi",
#    "first": "enrico",
#    "last": "fermi"
#}
#for key, value in user_0.items():
#    print(f"\nKey: {key}")
#    print(f"value: {value}")

#favorite_language = {
#    "jen": "python",
#    "sarah": "c",
#    "edward": "ruby",
#    "phil": "python"
#}
#for name, language in favorite_language.items():
#    print(f"{name.title()}'s favorite language is {language.title()}")

#Looping through all the key in a dictionary
#page- 101
#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
#for name in favorite_language.keys():
#    print(name.title())
#for name in favorite_language.values():
#    print(name.title())
#here keys and values are reserved keywords

#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
#friends = ["phil", "sarah"]
#for name in favorite_language.keys():
#    print(name.title())
#    if name in friends:
#        language = favorite_language[name].title()
#        print(f"\n{name.title()}, I see you love {language}!")

#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
# 
#if "erin" not in favorite_language.keys():
#    print("Erin, please take our poll!")

#Looping through a dictionary's keys in a particular order
#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
#for name in sorted(favorite_language.keys()):
#    print(f"{name.title()}, thank you for taking the poll.")

#looping through all values in a dictionary
#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
#print("The following language have been mentioned")
#for language in favorite_language.values():
#    print(language.title())

# uses of set(if two values are same then printing one value in set)
#favorite_language = {
#    "jen": "python",
#    "sarah": "C",
#    "edward": "ruby",
#    "phil": "python"
#}
#print("The following language have been mentioned")
#for language in set(favorite_language.values()):
#    print(language.title())

############ NESTING
# a list of dictionary
#alien_0 = {"color": "green", "points": 5}
#alien_1 = {"color": "yellow", "points": 10}
#alien_2 = {"color": "red", "points": 15}
#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#    print(alien)

#aliens = []
#for alien in range(30):
#    new_alien = {"color": "green", "points": 5, "speed": "slow"}
#    aliens.append(new_alien)
#for alien in aliens[:5]:
#    print(alien)
#print("...")
#print(f"Total number of aliens: {len(aliens)}")

#aliens = []
#for alien in range(30):
#    new_alien = {"color": "green", "points": 5, "speed": "slow"}
#    aliens.append(new_alien)
#for alien in aliens[:3]:
#    if alien["color"] == "green":
#        alien["color"] = "yellow"
#        alien["speed"] = "medium"
#        alien["points"] = 10 
#for alien in aliens[:5]:
#    print(alien)
#print("...")
#print(f"Total number of aliens: {len(aliens)}")

#a list in a dictionary
#pizza = {
#    "crust": "thick",
#    "toppings": ["mushrooms", "extra cheese"]
#}
#print(f"you ordered a {pizza['crust']}-crusht pizza"
#    "with the following toppings:")
#for topping in pizza["toppings"]:
#    print("\t" + topping)

# favorite_languages = {
#     "jen": ["python", "ruby"],
#     "sarah": ["C"],
#     "edward": ["ruby", "go"],
#     "phil": ["python", "haskell"]
# }
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

#a dictionary in a dictionary
# users = {
#     "aeinstein": {
#         "first": "albert",
#         "last": "einstein",
#         "location": "princeton"
#     },
#     "mcurie": {
#         "first": "marie",
#         "last": "curie",
#         "location": "paris"
#     },
# }
# for username, user_info in users.items():
    
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\nUsername: {username}")
#     print(f"\tFullName: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

#user input and while loops
#page - 113

#input()
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

#writing clear prompts
# name = input("please enter your name: ")
# print(f"\n Hello, {name}!")

#using int() to accept numerical input
# age = input("How old are you?")
# age = int(age)
# print(age)

# age = input("How old are you?")
# print(type(age))
# age = int(age)
# print(type(age))

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYOu'll be able to ride when you're a little older.")

#the modulo operator
# number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
# if number%2==0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

##########While loops########
#page - 118

#This system will be continiusly running
#until you use any condition end of the programm in this type of programm

# current_number = 1
# while current_number == 1:
#     print(current_number)

# message =input("say something: ")
# while message != "quit":
#     print(message)

#while end side programme given

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# number = 1
# while number <= 100:
#     print(number)
#     number += 1

#letting the user choose when to quit
# message = ""
# while message != "quit":
#     message = input("please write something: ")
#     print(message)

# message =input("say something: ")
# while message != "quit":
#     print(message)
#     break # this is as like if_loop

# message = ""
# while message != "quit":
#     print(message)
#     message = input("Hello sir please say something: ")

# message = ""
# while message != "quit":
#     message = input("Hello sir please say something: ")
#     print(message)
# upper both are simillar

###using a Flag
# mainly flag is 
# there have condition for true and false
# active = True
# while active:
#     message = input("say something: ")
#     if message == "quit":
#         active = False
#     else:
#         print(message)

#using break to exit a loop
# while True:
#     city = input("please enter your city name: ")
#     if city == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

#using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

#break for programme stop
#continue = 
#pass = condition dont care


# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         pass
#     print(current_number)

### Avoiding infinirte loops
# x = 1
# while x <= 5:
#     print(x)

# x = 1
# while x <= 5:
#     print(x)
#     x += 1
   
#using a while loop with lists and dictionary
# page- 124  
#moving items from one list to Another
#unconfirmed_users = ["alice", "brian", "candace"]
#confirmed_users = []
#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#    print(f"verifying users: {current_user.title()}")
#    confirmed_users.append(current_user)
#like
# x = ["a", "b", "c"]
# y = []
# while x:
#     z = x.pop()
#     print(z)
#     y.append(z)

#ramoving all instance of specific values from a list
# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
# print(pets)
# while "cat" in pets:
#     pets.remove("cat")
# print(pets)

# lets make a problem 
#if list ve cat then remove dog and dog present remove cat
# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
# print(pets)
# while "cat" in pets:
#     pets.remove("cat")
# while "dog" in pets:
#     pets.remove("dog")
# print(pets)

######## Filing a dictionary with users input
### page - 126
#Interesting toppics**********
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\n What is your name?: ")
#     response = input("which mountain would you like to climb someday?: ")
#     responses[name] = response
#     repeat = input("would you like to let another person respond? (yes/no)")
#     if repeat == "no":
#         polling_active = False
# print("\n----poll Result ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

# a = {}
# b = True
# while b:
#     name = input("\nNAME: ")
#     response = input("mountain: ")
#     a[name] = response
#     repeat = input("\n(yes,no)")
#     if repeat == "no":
#         b = False
# print("\n--- poll---")
# for name, response in a.items():
#     print(name, response)


###############################################################
#################### FUNCTION ########################
#########page129##################################

#defining a function
# def greet_user():
#     print("Hello!")
# greet_user()

#passing information to a function
# def greet_user(username):
#     print(f"Hello, {username.title()}!")
# greet_user("ashar")
# greet_user("jesseka")

#argument and parameters
#passing arguments
#positional arguments
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("dog", "harry")

# multiple function calls
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("dog", "harry")
# describe_pet("hamster", "willie")  

# keyword arguments
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type = "hamster", pet_name = "harry")
# describe_pet(pet_name = "parry", animal_type = "cat")

##default values
# def describe_pet(pet_name, animal_type = "dog"):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name = "harry")
# describe_pet("comma")
# describe_pet("hammam", "fox")

##### Return values
#Returning a simple values
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# print(get_formatted_name("jimi", "hendrix"))
# #or
# musician = get_formatted_name("jimi", "hendrix")
# print(musician)

#making an argument optional
# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name("john", "lee", "hooker")
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=""):#double cotosion is not clear
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# Reterning Dictionary
# def build_person(first_name, last_name):
#     person = {"first": first_name, "last": last_name}
#     return person
# musician = build_person("jimi", "hendrix")
# print(musician)

# def build_person(first_name, last_name, age = None):
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person
# musician = build_person("jimi", "hendrix", age= 27)
# print(musician)

# using a function with a while loop
# page - 141
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# q for quit
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name or 'q' to quit: ")
#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Last name: ")
#     if l_name == "q":
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

##passing a list
# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
# usernames = ["hannah", "ty", "margot"]
# greet_users(usernames)

#modifying a list in a function
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"printing model: {current_design}")
#     completed_models.append(current_design)
# print("\nThe following models heve been printed:")
# for completed_model in completed_models:
#     print(completed_model)

#passing an arbitrary number of arguments
# def make_pizza(*toppings):
#     print(toppings)
# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")

# Mixing positional and arbitraty arguments## page -148
# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")

#using arbitrary keyword arguments
# def build_profile(first, last, **user_info):
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info
# user_profile = build_profile("albert", "einstein",
#                              location = "princeton",
#                              field = "pysics")
# print(user_profile)

#storing your function in mosules
#page - 150

# import pizza
# pizza.make_pizza(16, "pepperoni")
# pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

##### import specific function
# from pizza import make_pizza
# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")

#using as to give a function an alias
# from pizza import make_pizza as mp
# mp(16, "pepperoni")
# mp(12, "mushrooms", "green peppers", "extra cheese")

#using as to give a module an alias
# import pizza as p
# p.make_pizza(16, "peperoni")
# p.make_pizza(12, "mushrooms", "green pepers", "extra cheese")

#importing all function in a module
# from pizza import *
# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")

#################################################################
################### CLASSESE ##########################
######## page - 157 ###########################################
#creating and using a class
#creating the dog class
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
# my_dog = Dog("Willie", 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

#calling methods
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
# my_dog = Dog("Willie", 6)
# my_dog.sit()
# my_dog.roll_over()

#creating multiple instances
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

#working with classes and instances
#The car class
# class Car:
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# setting a default value for an attribute
# page - 163
# class Car:
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# modifying arrtibute value directly
# class Car:
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#modifying on attribute's value through a method
# class Car:
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#     def update_odometer(self, mileage):
#         self.odometer_reading = mileage
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

############
############ Inheritance #######
# __init__() method for a child class
# class Car:
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#     def update_odometer(self, mileage):
#         self.odometer_reading = mileage
# class ElectrickCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
# my_tesla = ElectrickCar("tesla", "model", 2019)
# print(my_tesla.get_descriptive_name())

#defining attribute and mothods for child class
# class Car:
#     def __init__(self, manufacturer, model, year):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#     def update_odometer(self, mileage):
#         self.odometer_reading = mileage
# class ElectrickCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 75
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kwh battery.")
# my_tesla = ElectrickCar("tesla", "model", 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

########################
############### importing classes
#page- 174
# importing a single class
# from car import Car
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# storing multiple classes in a module
# page - 176
#not solved
# from car import ElectricCar
# my_tesla = ElectricCar("tesla", "models", 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# importing multiple classes from a module
"""from car import Car, ElectricCar
my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())"""

# importing an entire module
# import car
# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())


##########################################################
############# FILES AND EXCEPTIONS #####################
### page - 183 ########################################

# reading an entire file
# with open("pi_digits.txt") as f:
#     content = f.read()
# print(content)

## strip
# with open("pi_digits.txt") as f:
#     content = f.read()
# print(content.rstrip())

#fiel paths
#with open("text_file/filename.txt") as f:
#file_path = "/home/ehmatthes/other_files/txt_files/filename.txt"
#with open(file_path) as f:

## Reading line by line
# filename = "pi_digits.txt"
# with open(filename) as f:
#     for line in f:
#         print(line)

# filename = "pi_digits.txt"
# with open(filename) as f:
#     for line in f:
#         print(line.rstrip())

# Making a list of lines from a file
# filename = "pi_digits.txt"
# with open(filename) as f:
#     lines = f.readlines()
# for line in lines:
#     print(line.rstrip())

# Working with a files contetns
# filename = "pi_digits.txt"
# with open(filename) as f:
#     lines = f.readlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))

# Large files One million digits
# filename = "pi_million_digits.txt"
# with open(filename) as f:
#     lines = f.readlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# is your birthday contained in pi
#page - 190
# filename = "pi_million_digits.txt"
# with open(filename) as f:
#     lines = f.readlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("your birthday does not appear in the first million digits of pi.")

# Writing to a file
# writing to an empty file
# filename = "programming.txt"
# with open(filename, "w") as f:
#     f.write("Hello world")
# here automaticaly create a programming.txt file
# if there not exit this file and write the text otherwise write the text

# writing multiple lines
# filename = "programming.txt"
# with open(filename, "w") as f:
#     f.write("Hello world")
#     f.write("\nI love to coding")

# appending to a file
# filename = "programming.txt"
# with open(filename, "a") as f:
#     f.write("\nI also love finding meaning in large datasets.")

# Exceptions
# Handling the zeroDivisionError exception
# using try-except block
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# using exception to prevent crashes
# print("Give me two numbers for devide or 'q' to quit: ")
# while True:
#     x = input("\nFirst number: ")
#     if x == "q":
#         break
#     y = input("\nSecond number: ")
#     if y == "q":
#         break
#     try:
#         z = int(x)/int(y)
#     except ZeroDivisionError:
#         print("You cant devide by 0!")
#     else:
#         print(z)

# Handling the FileNotFoundError exception
# filename = "alice.txt"
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} dose not exit.")

# Analyzing text using input methods
# x = input("plese give me file name for txt format: ")
# y = x + ".txt"
# filename = y
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} dose not exit.")
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words.")
    
# working with def for count words
# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} dose not exit.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
# filename = "alice.txt"
# count_words(filename)

# working witn def for counting many file words
# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} dose not exit.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
# filenames = ["alice.txt", "programming.txt", "ba.txt"]
# for filename in filenames:
#     count_words(filename)

# Failing silently For file not found using Pass
# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
# filenames = ["alice.txt", "programming.txt", "ba.txt"]
# for filename in filenames:
#     count_words(filename)

## storing Data
# using json.dump() and json.load()
# page -203
# import json
# number = [2, 3, 4, 7]
# filename = "numbers.json"
# with open(filename, "w") as f:
#     json.dump(number, f)

# import json
# filename = "numbers.json"
# with open(filename) as f:
#     numbers = json.load(f)
# print(numbers)

# saving and reading user-generated data
# import json
# username = input("what is your name?: ")
# filename = "username.json"
# with open(filename, "w") as f:
#     json.dump(username, f)
#     print(f"we ll remember you when you come back, {username}!")

# import json
# filename = "username.json"
# with open(filename) as f:
#     username = json.load(f)
#     print(f"welcome back, {username}!")

# import json
# filename = "username.json"
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("what is your name: ")
#     with open(filename, "w") as f:
#         json.dump(username, f)
#         print(f"we ll rember you when you come back, {username}!")
# else:
#     print(f"welcome back, {username}!")

# Regactoring
# import json
# def greet_user():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("what is your name: ")
#         with open(filename, "w") as f:
#             json.dump(username, f)
#             print(f"we ll rember you when you come back, {username}!")
#     else:
#         print(f"welcome back, {username}!")
# greet_user()

# import json
# def get_stored_username():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def greet_user():
#     username = get_stored_username()
#     if username:
#         print(f"welcome back, {username}!")
#     else:
#         username = input("what is your name?: ")
#         filename = "username.json"
#         with open(filename, "w") as f:
#             json.dump(username, f)
#             print(f"we ll remember you when you come back, {username}!")
# greet_user()

# import json
# def get_stored_username():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def greet_user():
#     username = get_stored_username()
#     if username:
#         print(f"welcome back, {username}!")
#     else:
#         username = input("what is your name?: ")
#         filename = "username.json"
#         with open(filename, "w") as f:
#             json.dump(username, f)
#             print(f"we ll remember you when you come back, {username}!")
# greet_user()

# import json
# def get_stored_username():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def get_new_username():
#     username = input("what is your name?: ")
#     filename = "username.json"
#     with open(filename, "w") as f:
#         json.dump(username, f)
#     return username

# def greet_user():
#     username = get_stored_username()
#     if username:
#         print(f"welcome back, {username}!")
#     else:
#         username = get_new_username()
#         print(f"we ll remember you when you come back, {username}!")
# greet_user()

# Testing your code