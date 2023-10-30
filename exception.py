Basic code for exception handling

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

try:
  d=int(input("Enter anything:"))
  c=a/b
  print("The Result is",c)
except ZeroDivisionError:
  print("Any number is not divisible by zero")
except ValueError:
  print("Value Error is occured")
except FileNotFoundError:
  print("File is not found")
else:
  print("There are no such exceptions, Else block is printed when the code has no exceptions")
finally:
  print("Finally block is executed always")
