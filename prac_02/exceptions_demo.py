"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When either of the inputs are not integers hence the int(input)
2. When will a ZeroDivisionError occur?
When the denominator is a Zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could put in a while loop making sure the denominator is not 0

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator (That is not 0): "))

    fraction = numerator / denominator

    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
