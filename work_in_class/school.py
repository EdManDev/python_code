print('\x1bc')


name = str(input("\nENTER YOUR NAME: "))
while True:
    print("-Are you busy", name, "? ")
    response = str(input())
    if response == "yes":
        print("-ok you should take a break", name)
    else:
        print("ok good bye", name)
    name = str(input("\nWELCOME AGAIN ENTER YOUR NAME: "))
