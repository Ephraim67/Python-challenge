# Division and Square-root
#  returns the square root of the number 
# if it is divisible by 5, returns its remainder if it is not divisible by 
# 5. 
def divide_or_square(number):
    if number % 5 == 0:
        sq_root = number ** 0.5
        return sq_root
    else:
        remainder = number % 5
        return remainder
    
print(divide_or_square(10))  # Output: 5.0