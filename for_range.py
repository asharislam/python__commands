#for num in range(10):
#    print("number:", num)

#for number in range(5, 20):
#    print("number:", number)

#for number in range(5, 20, 3):
#    print("number:", number)

#for num in range(5, 20):
#    print("number:", num)
#    if num == 10:
#        break

student_result = [60, 70, 20, 90, 50]
for mark in student_result:
    if mark < 33:
        continue
    print("passed!", mark)
