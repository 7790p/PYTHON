from random import randint
c=randint(1,50)
i=0
while i<5:
    a=int(input())
    if a<=50:
        if c==a:
            print("find")
            break;
        elif c>a:
            print("ur no is smaller")
        elif c<a:
            print("ur no is bigger")

        i=i+1
    else:
        print("ur chnce remain")
        i=i
else:
    print("not found",c)
        
    