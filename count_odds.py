# Add the odd numbers between 0 to 5000 (purpose of my program)

# Setup
result = 0


# Work!
# Let's look at the numbers from 0 to 5000
num = 0
while num <= 20:
    is_odd = num % 2 != 0
    if is_odd:
        print(num)
        result += num
    # print('I am inside the loop')
    # print(num)
    num = num + 1 #(longer version)
    # num += 1 #(shorter version/ choose whichever makes more sense)



# Return/print the result
print(result)