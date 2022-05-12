"""number_input = input("please enter a number: ")# int here not possible"""

"""try:
    print("Divided by 2:", int(number_input/2))
except:
    print("en error occurd, pls enter another number")"""

"""try:
    print("Divided by 2: ", int(number_input)/2)
except Exception as e:
    print("Error:", str(e))
    print("En error occurd, please enter another number.")
finally:
    print("calculation done.")
"""

"""try:
    print("Divided by 2:", int(number_input)/2)
except Exception as e:
    raise Exception("you have entered a string, please a number")
finally:
    print("calculation done")"""




#another

try:
    print("y")
except NameError:
    print("Variable is not defined")
except ValueError:
    print("Can't convert a string to an integers")
else:
    print("there is no erroe.")