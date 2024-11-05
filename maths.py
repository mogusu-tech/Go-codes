value =True
while value:
    message = input("Do you like to proceed (yes/no)")
    if message == "yes":
        value = True
    else:
        value = False
    var1 = int(input("Enter a number"))
    var2 = int(input("Enter another number: "))
    operations = input("Choose an operation to continue: (+),(-),(/),(*),(**),(%)")
    if operations == "+":
        print("You Have selected an addition Operator")
        addition = var1 + var2
        print(f"The addition is, {addition}")
    elif operations == "-":
        print("You Have selected an subtraction Operator")
        subtraction = var1 - var2
        print(f"The subtraction is, {subtraction}")
    elif operations == "*":
        print("You Have selected an multiplication Operator")
        multiplication = var1 * var2
        print(f"The multiplication is, {multiplication}")
    elif operations == "/":
        print("You Have selected a division Operator")
        division = var1 / var2
        print(f"The division is, {division}")
    elif operations == "**":
        print("You Have selected an exponentiation Operator")
        exponentiation = var1 ** var2
        print(f"The exponentiation is, {exponentiation}")
    elif operations == "%":
        print("You Have selected a modulus Operator")
        modulus = var1 % var2
        print(f"The modulus is, {modulus}")
    else:
        print("You Have selected an invalid operator")