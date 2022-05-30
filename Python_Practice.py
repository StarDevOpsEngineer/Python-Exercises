print("Hello World, I am Learning Python")
length = 10
width = 5
area = length*width
print(f"The area is {area}")

#We are defining a function that computes area
def area(length, width):
    a = length*width
    return a

#Let's call the function
print("AREA:", area(100,5))
print("AREA:", area(1000,5))

# A program that says hi to a user
## we will use the input function#

name = input("Enter your name:")
age = input("Please provide your age:")
print(f"Hello {name}, It's nice to meet you. I am {age} too")