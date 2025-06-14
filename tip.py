"""
Tip Calculator
This program calculates the tip amount for a meal based on the cost, desired tip percentage and number of people.
It handles input parsing for dollar amounts and percentages.
"""
def main():
    """
    Calculate and display tip amount based on meal cost and tip percentage.
    Prompts user for meal cost, tip percentage and number of people, then displays the tip amount per person.
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    if dollars is None:
        return
    
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    if percent is None:
        return
    
    tip = dollars * percent
    try:
        dividing = int(input("How many people are there? ").strip())
        check_per_person = tip / dividing
        print(f"Leave ${check_per_person:.2f} each.")
    except (ValueError, ZeroDivisionError):
        print("Please enter a valid number of people!")

def dollars_to_float(d):
    """
    Convert dollar string to float value
    Args: d (str): Dollar amount as string (e.g., "$15.50")
    Returns: float: Numeric value without dollar sign
    """
    try:
        return float(d.replace("$", ""))
    except ValueError:
        print("Please enter a valid meal cost!")
        return None

def percent_to_float(p):
    """
    Convert percentage string to decimal value
    Args: p (str): Percentage as string (e.g., "15%")
    Returns: float: Decimal equivalent without % (e.g., 0.15)
    """
    try:
        return float(p.replace("%", "")) / 100
    except ValueError:
        print("Please enter a valid percentage!")
        return None
        
main()