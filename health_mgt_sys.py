print("Welcome to Health Management System\n")
print("Patient name : \nharry\nrohan\nhammed")

patient = input("Enter the name of Patient : ")

if patient == "harry" :
    har_d = input("what you want to know about harry diet or exercise : ")
    if har_d == "diet" :
        print("vegetable , oats , soyabean , brown bread , brown rice")
    else :
        print("Squats , Lunges , Push-ups , Abdominal Crunches , Bent-over Row")


if patient == "rohan":
    r_d = input("what you want to know about rohan diet or exercise : ")
    if r_d == "diet" :
        print("  soyabean , brown bread , vegetable , brown rice , oats ")
    else :
        print("Squats , Lunges , Push-ups , Abdominal Crunches , Bent-over Row")


if patient == "hammed":
    h_d = input("what you want to know about hammed diet or exercise : ")
    if h_d == "diet" :
        print("vegetable , oats , soyabean , brown bread , brown rice")
    else :
        print("Squats , Lunges , Push-ups , Abdominal Crunches , Bent-over Row")