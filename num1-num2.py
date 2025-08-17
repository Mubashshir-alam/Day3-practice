"""Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
      a. Sum of the digits of the number is a multiple of 3
      b. Number has only two digits
      c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1."""


# lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num = -1
    def sum_of_digits(number):
        sum_digit = 0
        while number > 0:
            rem = number % 10
            sum_digit += rem
            number //= 10
        return sum_digit

    valid_numbers = []  # List to store numbers satisfying conditions
    if num1 < num2:
        # Iterate from num1 to num2 (inclusive)
        for num in range(num1, num2 + 1):
            # Check if the number has two digits
            if 10 <= num <= 99:
                # Check if sum of digits is a multiple of 3
                if sum_of_digits(num) % 3 == 0:
                    # Check if number is a multiple of 5
                    if num % 5 == 0:
                        valid_numbers.append(num)

    # Return the maximum valid number or -1 if no valid number exists
    if valid_numbers:
        max_num = max(valid_numbers)
    return max_num


# Provide different values for num1 and num2 and test your program.
max_num = find_max(10, 15)
print(max_num)