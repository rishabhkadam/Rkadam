import random
name = input("waht is you name :")

lst = ["snake", "water", "gun"]
var = 1
userp = 0
decinap = 0

print(f"Hi! {name} i am Denica Let's Play Game\nyou have 10 chance\n Choose the word :\nsnake\nwater\ngun")
while var <= 10:
    var = var + 1
    user = input("choose one : ")
    choice = random.choice(lst)
    print(choice)
    if user == choice:
        print("both got a 0 point")

    if user == "snake" and choice == "water":
        print("you win!")
        userp += 1
        print(userp)
        print("point")


    if user == "snake" and choice == "gun":
        print("Denica win!")
        decinap += 1
        print(decinap)
        print("point")

    if user == "water" and choice == "snake":
        print("denina win!")
        decinap += 1
        print(decinap)
        print("point")

    if user == "water" and choice == "gun":
        print("you win!")
        userp += 1
        print(userp)
        print("point")

    if user == "gun" and choice == "snake":
        print("you win!")
        userp += 1
        print(userp)
        print("point")

    if user == "gun" and choice == "water":
        print("Denica win!")
        decinap += 1
        print(decinap)
        print("point")

print(f"your point {userp} and Denica point {decinap}")

if userp > decinap:
    print(f"YOU WIN WELL DONE! {name}")
else:
    print("DENICA WIN!")
