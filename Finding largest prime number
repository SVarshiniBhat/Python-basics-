from itertools import permutations

num = input("Enter a number: ")  

# Generate all valid numbers using the given digits (without leading zeros)
unique_numbers = sorted(set(int("".join(p)) for p in permutations(num) if p[0] != '0'), reverse=True)

# Find the largest prime number
for number in unique_numbers:
    if number > 1:  # Prime numbers are greater than 1
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break  # Not a prime, move to the next number
        else:  # If no divisors found, it's prime
            print(number)
            break
else:
    print("Error: No prime number can be formed.")
