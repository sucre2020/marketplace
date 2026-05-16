
def helloworld():
    firstName = input("Please enter first name: ")
    lastName = input("Please enter last name: ")

    greeting = firstName + " " + lastName

    print(f"Hello! {greeting}, \n Welcome to my Hello World Program")

    num1 = int(input("Please pick first number: "))

    num2 = int(input("Please pick second number: "))

    if num1 < num2:
        print(f"{num2} is greater than {num1}")

    elif num1 > num2:
        print(f"{num1} is greater than {num2}")

    else:
        print(f"{num1} and {num2} are equal")


helloworld()