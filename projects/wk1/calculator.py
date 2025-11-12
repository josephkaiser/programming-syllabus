'''
Calculator

This is the first weekly project! It is a simple CLI calculator that allows users to input a number, an operation and another number then prints the result. No it doesn't replicate the native operators from scratch, but it does use flow control to apply the correct operation which is taken as string input.

Original Author: Joseph Kaiser
Creation Date: 10/31/2025
'''

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() == 'q':
            return None
        try:
            return float(s)
        except ValueError:
            print("Please enter a valid number to proceed or 'q' to quit.")

def get_operator(prompt):
    valid_oper = {'+', '-', '*', '/'}
    while True:
        ops = input(prompt).strip()
        if ops.lower() == 'q':
            return None
        if ops in valid_oper:
            return ops
        print("enter a valid operator + - * / or 'q' to quit.")

def safe_operation_dispatcher(operation, x, y):
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    try:
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        func = operations[operation]
        result = func(x, y)
        return {"success": True, "result": result}
    
    except Exception as e:
        return {"success": False, "error": str(e)}

# Examples
print(safe_operation_dispatcher('add', 5, 3))      
# Output: {'success': True, 'result': 8}

print(safe_operation_dispatcher('divide', 10, 0))  
# Output: {'success': False, 'error': 'Cannot divide by zero'}

print(safe_operation_dispatcher('modulo', 10, 3))  
# Output: {'success': False, 'error': 'Unknown operation: modulo'}
def main():
    while True:
        print("this program takes input in three steps. First, enter a number and hit the 'enter' key. Second an operation (+, -, *, /) and hit 'enter' again. Third a number and hit 'enter' one more time.")
        a = get_number("Enter a number > ")
        if a is None:
            break

        op = get_operator(f"Enter an operation (i.e., +, -, *, /) for {a} > ")
        if op is None:
            break
        
        b = get_number(f"Enter a number to complete the expression {a} {op} > ")
        if b is None:
            break

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Cannot divide by zero.")
                continue
            result = a / b
        else:
            "error"
            continue

        print(f"{a} {op} {b} = {result}")

if __name__ == "__main__":
    main()
