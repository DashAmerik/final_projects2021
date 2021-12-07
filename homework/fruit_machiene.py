import random
fruit = ['Cherry','Bell','Lemon','Orange','Star','Skull']
money = 100

def roll(credit):
    f1 = fruit[random.randint(0,len(fruit)-1)]
    f2 = fruit[random.randint(0,len(fruit)-1)]
    f3 = fruit[random.randint(0,len(fruit)-1)]
    if f1 == f2 or f2 == f3 or f1 == f3:
        credit += 20
    elif f1 == f2 and f2 == f3:
        credit += 100
    else:
        credit -= 20
    return credit, f1, f2, f3

ask = input("play? y/n: ")
while ask == 'y':
        res = roll(money)
        print(*res)
        money = res[0]
        ask = input("play? y/n: ")

#????
