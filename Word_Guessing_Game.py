import random
lst=["health", "random", "colture", "beer", "friend", "people", "family", "home", "apple", "school", "music", "game", "computer", "water", "night"]
lst2=[]
lst3=[]
lst4=[]
turns=0
correct_answers=0
wrong_answers=0



def get_word():
    print("In Each line Enter A word And When You Done Enter 0")
    i=None
    while i!= "0":
        i=input("Please Enter One Word: ")
        lst4.append(i)
    lst.clear()
    for i in lst4:
        lst.append(i)
        
        
def start():
    global turns
    a=random.randint(0,len(lst)-1)
    turns+=1
    b=lst[a]
    for i in range(len(b)):
        lst2.append("-")
    print()
    return b
    
def guess():
    global correct_answers, wrong_answers, correct_answers, w_answers
    print("Lets start the Game!!!")
    print(f"The Choosen Word has {len(b)} letter")
    if len(b)<=5:
        print("You Have 10 Chance To Guess")
        for i in range(10):
            w=9-i
            if "-" in lst2:
                n=input("Please Inter A Word: ")
                for j in range(len(b)):
                    if b[j] == n.lower():
                        lst2.pop(j)
                        lst2.insert(j,n)
                for t in lst2:
                    print(t,end="")
                print()
                if "-" in lst2:
                    print(f"You Have {w} Guesses To reach the limit (So buy premium)")
            else:
                lst3.append(i)
                break
    elif 5<len(b)<=10:
        print("You Have 20 Chance To Guess")
        for i in range(20):
            w=19-i
            if "-" in lst2:
                n=input("Please Inter A Word: ")
                for j in range(len(b)):
                    if b[j] == n.lower():
                        lst2.pop(j)
                        lst2.insert(j,n)
                for t in lst2:
                    print(t,end="")
                print()
                if "-" in lst2:
                    print(f"You Have {w} Guesses To reach the limit (So buy premium)")
            else:
                lst3.append(i)
                break
    elif 10<len(b)<=15:
        print("You Have 30 Chance To Guess")
        for i in range(30):
            w=29-i
            if "-" in lst2:
                n=input("Please Inter A Word: ")
                for j in range(len(b)):
                    if b[j] == n.lower():
                        lst2.pop(j)
                        lst2.insert(j,n)
                for t in lst2:
                    print(t,end="")
                print()
                if "-" in lst2:
                    print(f"You Have {w} Guesses To reach the limit (So buy premium)")
            else:
                lst3.append(i)
                break
    else:
        print("You Have 50 Chance To Guess")
        for i in range(50):
            w=49-i
            if "-" in lst2:
                n=input("Please Inter A Word: ")
                for j in range(len(b)):
                    if b[j] == n.lower():
                        lst2.pop(j)
                        lst2.insert(j,n)
                for t in lst2:
                    print(t,end="")
                print()
                if "-" in lst2:
                    print(f"You Have {w} Guesses To reach the limit (So buy premium)")
            else:
                lst3.append(i)
                break
            

def check():
    global correct_answers, wrong_answers, q
    if "-" in lst2:
        print("Your guess limit has expired, buy premium to dont have limit in gusses ")
        print(f"The Choosen Word Was '{b}'")
        wrong_answers+=1
    else:
        print(f"congratulations, You won!!! The Choosen Word Was '{b}' ")
        print(f"and you guessed it in just {lst3[0]} Times, now you can by a premium")
        correct_answers+=1
    lst2.clear()
        
def ask_continue():
    r=input("Do You Want To Continue? (Y/N) ")
    if r.lower() == "y":
        print("OK Lets Go Again")
        return True
    elif r.lower() == "n":
        print("Gotcha, Lets see the resault!")
        return False
    else:
        print("The Input Is Not Correct <-_-> correct your input and buy premium")
        return ask_continue()
s=0
p=0   
while s==0:        
    print("welcome To WGG, Here We Have default List Of Words That You Should Guess The Desired Word")
    h=input("if You Want To Have Your Own List Of Words Enter number 1 or if You Want To Play With Default List Enter 0: ")
    if h == "0":
        b=start()
        guess()
        check()
        s+=1
        if not ask_continue():
            p+=1
    elif h == "1":
        get_word()
        b=start()
        guess()
        check()
        s+=1
        if not ask_continue():
            p+=1

if p == 0:
        b=start()
        guess()
        check()
        if not ask_continue():
            p+=1

while True:
    if p == 0:
        b=start()
        guess()
        check()
        if not ask_continue():
            break
    else:
        break
print(f"Your played {turns} times and bought 0 times premium (-_-)")
print(f"Your guess correct {correct_answers} Times")
print(f"Your guess wrong {wrong_answers} times")
