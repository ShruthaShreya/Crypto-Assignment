# Function to implement the Extended Euclidean Algorithm
def extended_euclidean(a, b):
    if b == 0:
        # Base case: gcd is a, and coefficients x=1, y=0
        return a, 1, 0
    else:
        # Recursive case
        gcd, x1, y1 = extended_euclidean(b, a % b)
        # Update x and y using results of recursion
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage
if __name__ == "__main__":
    a = 30
    b = 20

    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD of {a} and {b} is {gcd}")
    print(f"Coefficients x and y are: x = {x}, y = {y}")
    print(f"Verification: {a}*{x} + {b}*{y} = {a * x + b * y}")
