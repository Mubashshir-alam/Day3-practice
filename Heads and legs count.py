"""Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?"""


def solve(heads, legs):
    error_msg = "No solution"

    # Check for impossible cases
    if legs % 2 != 0 or heads > legs // 2 or heads * 4 < legs:
        print(error_msg)
        return

    # Calculate number of rabbits and chickens
    rabbit_count = (legs - 2 * heads) // 2
    chicken_count = heads - rabbit_count

    # Final validation
    if rabbit_count < 0 or chicken_count < 0:
        print(error_msg)
    else:
        print(f"chicken_count = {chicken_count} \nrabbit_count = {rabbit_count}")


# Test cases
solve(38, 130)  # Expected: 23 15
