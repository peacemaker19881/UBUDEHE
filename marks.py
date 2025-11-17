marks = int(input("Enter student marks: "))
if 80 <= marks <= 100:
    print("Grade: A")
elif 70 <= marks <= 79:
    print("Grade: B")
elif 60 <= marks <= 69:
    print("Grade: C")
elif 55 <= marks <= 59:
    print("Grade: D")
elif 50 <= marks <= 54:
    print("Grade: E")
elif 0 <= marks <= 49:
    print("Grade: F")
else:
    print("Invalid Entered marks")