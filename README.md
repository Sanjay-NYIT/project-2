# Group-15
EXTENDED EUCLIDEAN ALGORITHM IMPLEMENTATION
# Extended Euclidean Algorithm in Python

This project implements the **Extended Euclidean Algorithm** in Python. The algorithm computes the greatest common divisor (GCD) of two integers `a` and `b`, along with the coefficients `x` and `y` that satisfy the equation:

\[
a \cdot x + b \cdot y = \text{gcd}(a, b)
\]

If `gcd(a, b) = 1`, the script also calculates the **modular inverse** of `b` modulo `a`.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example Output](#example-output)
- [How It Works](#how-it-works)
- [License](#license)

## Features

- Computes the GCD of two integers using the Extended Euclidean Algorithm.
- Determines the coefficients `x` and `y` that satisfy Bézout's identity.
- Checks if the modular inverse of `b` modulo `a` exists and calculates it if possible.

## Requirements

- Python 3.x

No external libraries are required for this script.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Sanjay-NYIT/project-2.git
   cd untitled-2
2. Run the python script
   ```bash
   `python code.py`

## Example output

C:\Users\sanja\Desktop\Cryptography>docker run -it my-python-app

Enter a positive integer (modulus a): 1790

Enter a non-negative integer (b) less than a: 550

Verification: 1790 * 4 + 550 * -13 = 10

Coefficients: x = 4, y = -13

GCD(1790, 550) = 10

modular multiplicative inverse doesn't exist because gcd is not 1

## How it works
- The Extended Euclidean Algorithm is used to compute not only the greatest common divisor (GCD) of two integers but also the coefficients x and y that satisfy the
  equation:
`a⋅x+b⋅y=gcd(a,b)`
- If the GCD is 1, y provides the modular multiplicative inverse of b modulo a. This means:`b⋅y≡1 mod(a)`
- This inverse is important in number theory, particularly in cryptography.

## License
[MIT](https://github.com/Sanjay-NYIT/project-2/blob/main/Untitled-2.py)



