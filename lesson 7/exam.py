medical_cause = input("did you have medical cause? y or n")
if medical_cause == "y":
    print("you are alloued")
else:
    atten = int(input(" enter your attendance:"))
    if atten >=75:
        print("allowed")
    else:
        print("not allowed")
