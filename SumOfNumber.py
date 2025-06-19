print(8+5)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(num1+num2)
total = 0
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    total += num

print("Sum of the 5 numbers is:", total)
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")
