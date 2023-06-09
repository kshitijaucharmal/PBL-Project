def binary_to_decimal():
    num = (input("Enter a binary number :  ")) # Enter a number 
    binary = str(num) # convert the num to string
    bin_list = binary.split() # convert it into list
    bin_list.reverse() # sort the lsit in the ascending order
    print(bin_list)
    Sum = 0
    for i in range(len(bin_list)):
        if bin_list[i] == "1":
            Sum = Sum + 1*2**(i)
    print(f"Binary to decimal conversion of {num} is : {Sum}")
binary_to_decimal() # calling the function

def decimal_to_bianry():
    decimal = int(input("Enter a decimal number: "))
    binary = bin(decimal)
    print(f"Conversion of decimal number {decimal} is {binary} ")
decimal_to_bianry()

def reverse_number():
    reversed_num = 0
    number = int(input("Enter a number: " ))
    
    while number != 0:
        digit = number % 10
        reversed_num = reversed_num*10 + digit
        number = number // 10
    print(f"Reversed number of {number} is {reversed_num}  ")
reverse_number()
    