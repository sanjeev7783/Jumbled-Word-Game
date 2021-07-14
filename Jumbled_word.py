import random as r
print("\t\t\tWelcome to Jumble Word !\n\n1. Easy\n2. Medium\n3. Hard\n")
choice=int(input("Select Level : "))
def fun(s1,s2,s3,s4,s5):
    correct=0
    d1=""
    d2=""
    d3=""
    d4=""
    d5=""
    l1=list(s1)
    l2=list(s2)
    l3=list(s3)
    l4=list(s4)
    l5=list(s5)
    r.shuffle(l1)
    r.shuffle(l2)
    r.shuffle(l3)
    r.shuffle(l4)
    r.shuffle(l5)
    print("The jumble is : ",d1.join(l1))
    guess=input("Your Guess : ")
    if s1==guess:
        print("Good Job!")
        correct=correct+1
            
    else:
        print("Wrong ")
    print("The jumble is : ",d2.join(l2))
    guess=input("Your Guess : ")
    if s2==guess:
        correct=correct+1
        print("Good Job!")
    else:
        print("Wrong ")
    print("The jumble is : ",d3.join(l3))
    guess=input("Your Guess : ")
    if s3==guess:
        correct=correct+1
        print("Good Job!")
    else:
        print("Wrong ")
    print("The jumble is : ",d4.join(l4))
    guess=input("Your Guess : ")
    if s4==guess:
        correct=correct+1
        print("Good Job!")
    else:
        print("Wrong ")
    print("The jumble is : ",d5.join(l5))
    guess=input("Your Guess : ")
    if s5==guess:
        correct=correct+1
        print("Good Job!")
    else:
        print("Wrong ")
    print("Your score is ",correct,"out of 5") 
if choice==1:
    print("\t\tEasy Level Chosen")
    fun(s1="rat",s2="mat",s3="pad",s4="dad",s5="mom")
elif choice==2:
    print("\t\tMedium Level Chosen")
    fun(s1="ready",s2="matrix",s3="papaya",s4="dumb",s5="mouse")
elif choice==3:
    print("\t\tHard Level Chosen")
    fun(s1="rabbit",s2="mathematics",s3="cauliflower",s4="hippopotamus",s5="arithmetic")    
else:
    print("Invalid Choice")
