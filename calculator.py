# Defining variables x and y
# Then print the selected operation between the two numbers if they're valid

operation =  input("What's the operation? (Addition, Subtraction, Multiplication, Division): ").strip().title()
if operation not in ["Addition", "Subtraction", "Multiplication", "Division"]: 
    print("Please enter valid operations only!")
else:
    try:
        x = float(input("What's x? "))
        y = float(input("What's y? "))
        r = int(input("How many decimal places do you want? (Remember that precision isn't infinite.) (Please enter a non-negative number!): "))
        if r >= 0:
            if operation == "Division":
                result = x / y
            elif operation == "Multiplication":
                result = x * y
            elif operation == "Addition":
                result = x + y
            elif operation == "Subtraction":
                result = x - y
            print(f"Result: {result:.{r}f}")
        else:
            print("Invalid decimal places! Please enter a valid number.")
            


# If they aren't, print an error message

    except ValueError:
        print("Please enter valid numbers only!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")