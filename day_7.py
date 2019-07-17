# For numbers 1 to N
# if number divisible by 3, print "fizz"
# if number divisible by 5, print "buzz"
# if number divisible by 3 and 5, print "fizzbuzz"
# else print the number

# Input: integer > 0
# Output: print stuff based on rules above

while True:
    number = int(input("Número: "))
    if number >= 1:
        if number%3 == 0 and number%5 == 0:
            print("fizzbuzz")
        elif number%3 == 0:
            print("fizz")
        elif number%5 == 0:
            print("buzz")
        else:
            print(number)
    else:
        print("The number is out of range")