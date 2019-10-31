name=input("What is your name? ")
age=int(input("What is your age? "))

year=(2019 + (100 - age))

print(name ,",you will turn 100 years old in", year)


num=int(input("Give me a number: "))
mod=num % 2

if mod == 0:
    print("This number is even.")
else:
    print("This number is odd.")
