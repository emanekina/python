numb = int(input("Enter a positive integer, please:"))
while numb <= 0:
    numb = int(input("The value must be a positive integer. Please try again:"))

num_max = numb % 10

while numb > 0:
    num_compare = numb % 10
    numb = numb // 10
    if num_compare == 9:
        num_max = num_compare
        break
    elif num_compare > num_max:
        num_max = num_compare

print(f"The biggest number is {num_max}")
