# Program to display student grade using nested if
marks = int(input("Enter student marks: "))
if 0 <= marks <= 100:  # First check for valid range
    if marks >= 80:
        print("Grade: A")
    else:
        if marks >= 70:
            print("Grade: B")
        else:
            if marks >= 60:
                print("Grade: C")
            else:
                if marks >= 55:
                    print("Grade: D")
                else:
                    if marks >= 50:
                        print("Grade: E")
                    else:
                        print("Grade: F")
else:
    print("Invalid marks")
