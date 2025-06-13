# Ask the user for their name, remove extra spaces, and capitalize each word
name = " ".join(input("What's your name? ").split()).title()

# If you want, you can call the user only by their first name by doing e.g: first, last = name.split()  
# And then print("Hello, ", first) or print(f"hello, {first}")

# If input value is valuable, say hello to the user
# If not, greet in a standard manner
if name:
    print(f"Hello, {name}")
else:
    print("Hello, there!")