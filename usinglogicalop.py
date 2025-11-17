# Rwanda National Police Admission Program
# With detailed rejection reasons
sex = input("Enter sex (boy/girl): ").lower()
age = int(input("Enter age: "))
size = float(input("Enter size (height in cm): "))
level = input("Enter level of study (A0, A1, A2): ").upper()

allowed = True   # Assume allowed until a condition fails
reasons = []      # Store specific reasons for rejection
officer_level = False
# 1. Validate sex and age
if sex == "girl":
    if not (22 < age < 25):
        allowed = False
        reasons.append("Girls must be older than 22 and younger than 25.")
elif sex == "boy":
    if not (18 <= age <= 21):
        allowed = False
        reasons.append("Boys must be between 18 and 21 years old.")
else:
    allowed = False
    reasons.append("Sex must be 'boy' or 'girl'.")
# 2. Check size requirement
if size < 175.5:
    allowed = False
    reasons.append("Size must be at least 75.5 cm.")
# 3. Officer level check (A0)
if level == "A0":
    officer_level = True
elif level not in ["A0", "A1", "A2"]:
    allowed = False
    reasons.append("Study level must be A0, A1, or A2.")
# 4. Final decision
if allowed:
    print("\n✅ You are allowed to join Rwanda National Police.")

    if officer_level:
        print("You qualify for the OFFICER LEVEL (because you have A0).")
    else:
        print("You do NOT qualify for officer level (you do not have A0).")
else:
    print("\n❌ You are NOT allowed to join Rwanda National Police because:")
    for reason in reasons:
        print(" - " + reason)
