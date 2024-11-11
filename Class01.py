# Class01.py - Python Basics

def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    # Greet the user
    greet_user("Satwik")
    
    # Perform a simple addition
    num1 = 10
    num2 = 5
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")