print("a_module Initiated")

def get_factorial(n):
    if n == 0:
        return 1
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def get_sum(a, b):
    return a + b



if __name__ == "__main__":
    # this part only exicute, when this file is calling directly, not as a module to other file
    # By using this part, you can use this file as a module to use any function/class/variables
    # Or use it separately by calling it directly
    print('Factorial of 5:', get_factorial(5))
