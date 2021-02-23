import random

# Aquesta funció calcula el resultat de la lluita final depenent del poder de cada exércit.
def lluita(power1, power2):
    mult1 = random.randint(0, 10)
    mult2 = random.randint(0, 10)
    total1 = power1 * mult1
    total2 = power2 * mult2
    if total1 > total2:
        print("L'exercit d'hispania ha derrotat a l'exercit de Roma")
    elif total1 < total2:
        print("L'exercit de Roma ha derrotat a l'exercit d'Hispania")
    else:
        print("Bad ending. Un meteorit ha derrotat ambdós exercits (empat)")