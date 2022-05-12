def student_result(marks):

    if marks >= 80:
        if marks >= 90:
            if marks >= 95:
                print("Result: Super Golden A+")
            else:
                print("Result: Golden A+")
        else:
            print("Result: A+")
    elif marks >= 70 and marks <= 79:
        print("Result: A")
    elif marks >= 60 and marks <= 69:
        print("Result: A-")
    elif marks >= 50 and marks <= 59:
        print("Result: B")
    elif marks >= 40 and marks <= 49:
        print("Result: C")
    elif marks >= 33 and marks <= 39:
        print("Result: D")
    else:
        print("Result: F")

student_marks = [60, 43, 70, 80, 85, 90, 98]
for mark in student_marks:
    student_result(mark)

    





            
        
    
    
        