name = input("Enter your name: ")
n = int(input("Enter your birthyear: "))

if n > 2000:
    print(f"Hello {name}, you born after the greatest era ever")

elif n < 2000:
    print(f"Hello {name}, you were born during the greatest era ever!!!")

else:
    print(f"Hello {name}, you are in between!!!")
