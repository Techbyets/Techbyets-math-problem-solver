import time
import re
from fractions import Fraction
from sympy import symbols, diff

# List to store solved problems
solved_problems = []

# Function to display the main menu
def display_menu():
    print("\n=== Math Problem Solver ===")
    print("1. Arithmetic")
    print("2. Algebra")
    print("3. Calculus")
    print("4. Word Problems")
    print("5. Fractions")
    print("6. Normal Mathematics")
    print("7. Problems Solved")
    print("8. Exit")

# Function to solve arithmetic problems
def solve_arithmetic():
    print("\n=== Arithmetic Solver ===")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operation!")
        return
    
    print("Result:", result)
    solved_problems.append(f"Arithmetic: {num1} {operation} {num2} = {result}")

# Function to solve algebra problems
def solve_algebra():
    print("\n=== Algebra Solver ===")
    print("Solve equations of the form 'ax + b = c'")
    a = float(input("Enter the coefficient of x (a): "))
    b = float(input("Enter the constant term (b): "))
    c = float(input("Enter the result (c): "))
    
    if a == 0:
        if b == c:
            print("Infinite solutions: 0x + {} = {}".format(b, c))
        else:
            print("No solution: 0x + {} != {}".format(b, c))
    else:
        x = (c - b) / a
        print("Solution: x = {:.2f}".format(x))
        solved_problems.append(f"Algebra: {a}x + {b} = {c}, x = {x}")

# Function to solve calculus problems
def solve_calculus():
    print("\n=== Calculus Solver ===")
    print("Enter the expression to differentiate:")
    expression = input()

    # Define the symbol
    x = symbols('x')

    try:
        # Differentiate the expression with respect to x
        diff_expression = diff(expression, x)
        print("Differentiated expression:")
        print(diff_expression)
        solved_problems.append(f"Calculus: Differentiated expression: {diff_expression}")
    except Exception as e:
        print("Error:", e)

# Function to solve word problems
def solve_word_problems():
    print("\n=== Word Problems Solver ===")
    print("Enter your word problem:")
    problem = input()

    # Extract numbers and operators from the problem using regular expressions
    numbers = [int(num) for num in re.findall(r'\d+', problem)]
    operators = re.findall(r'[\+\-\*/]', problem)

    # Check if the number of operators is one less than the number of numbers
    if len(numbers) != len(operators) + 1:
        print("Invalid word problem format.")
        return

    # Perform calculations based on the operators
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '-':
            result -= numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '/':
            if numbers[i + 1] == 0:
                print("Error: Division by zero!")
                return
            result /= numbers[i + 1]
    
    print("Solution:", result)
    solved_problems.append(f"Word Problem: {problem} = {result}")

# Function to solve fractions problems
def solve_fractions():
    print("\n=== Fractions Solver ===")
    print("Enter your fraction problem:")
    problem = input()

    try:
        # Evaluate the fraction expression
        result = eval(problem)
        print("Solution:", result)
        solved_problems.append(f"Fractions: {problem} = {result}")
    except Exception as e:
        print("Error:", e)

# Function to solve normal mathematics problems
def solve_normal_mathematics():
    print("\n=== Normal Mathematics Solver ===")
    print("Select the type of problem to solve:")
    print("1. Prime Numbers")
    print("2. Factors of a Number")
    print("3. Fibonacci Sequence")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        solve_prime_numbers()
    elif choice == '2':
        solve_factors()
    elif choice == '3':
        solve_fibonacci()
    else:
        print("Invalid choice!")

# Function to solve prime numbers
def solve_prime_numbers():
    print("\n=== Prime Numbers Solver ===")
    n = int(input("Enter a number: "))
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    print("Prime numbers up to", n, ":", primes)
    solved_problems.append(f"Normal Mathematics: Prime numbers up to {n} : {primes}")

# Function to solve factors of a number
def solve_factors():
    print("\n=== Factors of a Number Solver ===")
    num = int(input("Enter a number: "))
    factors = [i for i in range(1, num + 1) if num % i == 0]
    print("Factors of", num, ":", factors)
    solved_problems.append(f"Normal Mathematics: Factors of {num} : {factors}")

# Function to solve the Fibonacci sequence
def solve_fibonacci():
    print("\n=== Fibonacci Sequence Solver ===")
    n = int(input("Enter the number of terms: "))
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    print("Fibonacci Sequence:", fibonacci_sequence)
    solved_problems.append(f"Normal Mathematics: Fibonacci Sequence with {n} terms : {fibonacci_sequence}")

# Function to display the list of problems solved
def display_problems_solved():
    print("\n=== Problems Solved ===")
    if solved_problems:
        for problem in solved_problems:
            print(problem)
    else:
        print("No problems solved yet.")

# Function to display a loading screen
def loading_screen():
    print("Processing...")
    time.sleep(1)  # Simulate processing time

# Function to display the header
def display_header():
    print("===========================")
    print("=== Math Problem Solver ===")
    print("===========================")

# Function to display the welcome message
def display_welcome_message():
    print("Welcome to Math Problem Solver!")

# Function to display the goodbye message
def display_goodbye_message():
    print("Thank you for using Math Problem Solver. Goodbye!")

# Main function to run the program
def main():
    display_header()
    display_welcome_message()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            loading_screen()
            solve_arithmetic()
        elif choice == '2':
            loading_screen()
            solve_algebra()
        elif choice == '3':
            loading_screen()
            solve_calculus()
        elif choice == '4':
            loading_screen()
            solve_word_problems()
        elif choice == '5':
            loading_screen()
            solve_fractions()
        elif choice == '6':
            loading_screen()
            solve_normal_mathematics()
        elif choice == '7':
            loading_screen()
            display_problems_solved()
        elif choice == '8':
            display_goodbye_message()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()