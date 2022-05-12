#nums = [2, 4, 6, 8, 9]              #[list]
#                                     #{dictionary:value}
#for num in (nums):                  #(tuple) #{set}
#    print("nums Item is:", num ** 100)


student ={
    "username": "ashar134",
    "firstname": "Ashar",
    "lasrname": "Islam",
    "phonenum": "013",
    "location": "mirpur-1",
}
for keys, value in student.items():
    print(keys + ": " + value)