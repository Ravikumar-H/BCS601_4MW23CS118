from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Function to safely evaluate the math expression
def evaluate_expression(expr):
    # If the user hits equals with nothing typed, return nothing
    if not expr:
        return ""
        
    try:
        # 1. Basic Security: Only allow specific math characters and numbers
        allowed_chars = set("0123456789.+-*/()sincostanloglnsqrtpie^ ")
        if not all(c in allowed_chars for c in expr):
            return "Error: Invalid characters"

        # 2. Format string for Python's math library
        expr = expr.replace('sin', 'math.sin')
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('tan', 'math.tan')
        expr = expr.replace('log', 'math.log10') # Standard log is base 10
        expr = expr.replace('ln', 'math.log')    # Natural log
        expr = expr.replace('sqrt', 'math.sqrt')
        expr = expr.replace('pi', 'math.pi')
        expr = expr.replace('e', 'math.e')
        expr = expr.replace('^', '**')           # Python uses ** for exponents

        # 3. Create a safe environment for eval() to run in
        safe_env = {"math": math, "__builtins__": None}
        
        # 4. Evaluate the expression safely
        result = eval(expr, safe_env)
        
        # 5. Clean up the formatting (e.g., show "5" instead of "5.0")
        if isinstance(result, float) and result.is_integer():
            return int(result)
            
        # Return result rounded to 6 decimal places to keep it clean
        return round(result, 6)
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception:
        return "Error: Invalid math expression"

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    expression = ""
    
    if request.method == 'POST':
        # Get the math expression sent from the HTML frontend
        expression = request.form.get('expression', '')
        # Calculate the result
        result = evaluate_expression(expression)
        
    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)