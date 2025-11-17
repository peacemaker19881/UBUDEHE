# Program to display student grade using match-case (Python's switch-case)
marks = int(input("Enter student marks: "))
# Determine grade category first
if 80 <= marks <= 100:
    category = "A"
elif 70 <= marks <= 79:
    category = "B"
elif 60 <= marks <= 69:
    category = "C"
elif 55 <= marks <= 59:
    category = "D"
else:
    category = "Invalid"

# Use match-case (switch-case)
match category:
    case "A":
        print("Grade: A")
    case "B":
        print("Grade: B")
    case "C":
        print("Grade: C")
    case "D":
        print("Grade: D")
    case _:
        print("Invalid marks")
