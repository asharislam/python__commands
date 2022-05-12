"""class person:
    hands = 2
    legs = 2
    mouth = 1
    def speak(self):
        print("Hi, Welcome to python")


hasan = person()
ijhar = person()
print(hasan.legs)
print(hasan.mouth)"""

"""class person:
    hands = 2
    legs = 2
    mouth = 1
    def speak(self):
        print("Hi, Welcome to python")

hasan = person()
ijhar = person()


hasan.speak()
ijhar.speak()"""


"""class person:
    hands = 2
    legs = 2
    mouth = 1
    def speak(self, msg):
        print("Hi", msg)

hasan = person()
ijhar = person()

hasan.speak("Hello python")
ijhar.speak("Hello Bangladesh")"""


"""class person:
    hends = 2
    legs = 2
    mouth = 1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def speak(myself, msg):
        print("Hello python", msg)

hasan = person("Hasan", "Ahmed")
ijhar = person("Ijharul", "Islam")
mahmud = person("mahmudul", "Islam")
margub = person("margubur", "Islam")

print(mahmud.first_name, mahmud.last_name)
print(mahmud.first_name, hasan.last_name)"""


#amazon product

class product:
    def __init__(self, incoming_name, incoming_price, incoming_color):
        self.name = incoming_name
        self.price = incoming_price
        self.color = incoming_color

pen = product("Econo", 10, "white")
print(pen.name, pen.price, pen.color)
print(pen.price)

computer = product("mackbook pro", 100000, "gray")
print(computer.name, computer.price, computer.color)



