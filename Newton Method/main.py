
import sympy as sp
#Define the symbolic variable
x = sp.symbols('x')
#Defiene the function
f = (x) ** 3 - 3 * (x) ** 2
#first and second derivative
f_derivative = sp.diff(f, x)
f_second_derivative = sp.diff(f_derivative, x)
#Initial values
x_value = 3
iteration = 5
for i in range(1,iteration+1):
    first_derivative = f_derivative.subs(x, x_value)
    second_derivative = f_second_derivative.subs(x, x_value)
    if second_derivative != 0:
        x_value = x_value - (first_derivative / second_derivative)
        decimal_x=sp.N(x_value)
        print(f"new x_{i} value: {decimal_x}")
    else:
        print("Division by zero. Choose a different initial value.")
        break