def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def main():
    a = int(input("Enter the modulus (a): "))
    b = int(input("Enter a non-negative integer (b) less than a: "))
    if b >= a:
        print("Error: b should be less than a.")
        return
    gcd, x, y = extended_gcd(a, b)
    print(f"gcd({a}, {b}) = {gcd}, x = {x}, y = {y}")

if __name__ == "__main__":
    main()
