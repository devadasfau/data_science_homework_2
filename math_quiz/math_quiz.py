import random

def function_A(minimum, maximum):
    """
    Returns a random integer between 'minimum' and 'maximum' (inclusive).

    Parameters:
    - minimum (int): The minimum value for the random integer.
    - maximum (int): The maximum value for the random integer.

    Returns:
    - int: A random integer within the specified range [minimum, maximum].
    """
    return random.randint(minimum, maximum)

def function_B():
    """
    Returns a random arithmetic operator: '+', '-', or '*'.
    
    Returns:
    - str: A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def function_C(n1, n2, operator):
    """
    Performs a mathematical operation based on the given numbers and operator.

    Parameters:
    - n1 (int): The first operand.
    - n2 (int): The second operand.
    - operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
    - tuple: A tuple containing a string representation of the operation and the result.
      - str: The string representation of the operation, e.g., "2 + 3".
      - int: The result of the mathematical operation.
    """
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:
        result = n1 * n2

    expression = f"{n1} {operator} {n2}"
    return expression, result

def math_quiz():
    s = 0
    t_q = 3.14159265359  # Pi is an unusual choice for the number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):  # Convert t_q to an integer
        n1 = function_A(1, 10)
        n2 = function_A(1, 5)  # Ensure n2 is an integer for subtraction
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{int(t_q)}")

if __name__ == "__main__":
    math_quiz()
