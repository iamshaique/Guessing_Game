import random
fruits=["apple","banana","orange","grape","mango","pineapple","strawberry","blueberry", "kiwi","watermelon"]
print(fruits)
print()
print("Guess one fruits from the above")
g=random.choice(fruits)
c=0
while c<4:
    f=input("Enter a fruit name: ")
    if g==f:
        print("You Won!")
        break
    else:
        if c==0:
            print(f"Hint1:The Fruit Contains {len(g)} characters")
        elif c==1:
            n=""
            for i in range(len(g)-1):
                n+="*"
            n+=g[-1]
            print(n)
        elif c==2:
            n=""
            n+=g[0]
            for i in range(1,len(g)):
                n+="*"
            print("Hint3:"+n)
        else:
            print("All attempts lost!")
            print(f"The fruit name was {g}")
        c+=1