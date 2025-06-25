num = input("\nEnter a number to check Palindrome: ")

# Reverse the number using string slicing
reversed_num = num[::-1]

# Check if palindrome
if num == reversed_num:
    print("Yes, it is a Palindrome Number.")
else:
    print("No, it is not a Palindrome Number.")