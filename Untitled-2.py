def extended_euclidean(a, b):
    if a < 1 or b < 0 or b >= a:
        raise ValueError("Input must be a non-negative integer b less than a, and a must be positive.")
    
    # Initialize variables
    x0, x1, y0, y1 = 1, 0, 0, 1
    
    while b != 0:
        q, r = divmod(a, b)  # q is the quotient, r is the remainder
        a, b = b, r
        
        # Update x and y using the Extended Euclidean relation
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    return a, x0, y0

# Get user input
try:
    a = int(input("Enter a positive integer (modulus a): "))
    b = int(input("Enter a non-negative integer (b) less than a: "))
    
    gcd, x, y = extended_euclidean(a, b)
    print(f"Verification: {a} * {x} + {b} * {y} = {gcd}")
    print(f"Coefficients: x = {x}, y = {y}")
    if y < 0:
      y=y+a
    print(f"GCD({a}, {b}) = {gcd}")
    
    if gcd != 1:
      print("modular multiplicative inverse doesn't exist because gcd is not 1")
    else:
      print("modular multiplicative inverse is " ,y)
    
except ValueError as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)