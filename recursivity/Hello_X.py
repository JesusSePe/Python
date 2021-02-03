# Repeats X times a text given by user
def hello(text, counter):
    if counter == 0:
        return
    else:
        print(text)
        return hello(text, counter - 1)


txt = input("Which text do you want to repeat? ")
times = int(input("How many times? "))
hello(txt, times)
