import random
# A rat chooses randomly between 3 ways. Route 1 lasts 3 minute. Route 2 lasts 5 minutes. Route 3 lasts 7 minutes and leaves the cage (correct option).

def rat(time):
    route = random.randrange(1,4)
    if route == 1:
        print("Route 1. +3 minutes")
        return rat(time + 3)
    elif route == 2:
        print("Route 2. +5 minutes")
        return rat(time + 5)
    else:
        print("Route 3. +7 minutes")
        return (time + 7)


print("Total: ", rat(0))