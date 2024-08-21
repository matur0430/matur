import random
def rolling_dice(pip,reapt):
    for r in range(reapt):
        n=random.randint(1,pip)
        print(r,n)

rolling_dice(6,5)

