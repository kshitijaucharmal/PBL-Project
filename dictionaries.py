num_dict={1:'one',2:'two',3:'three'}
print(num_dict)
N = int(input("Enter a binary number: "))
def binary_to_decimal(binary):
    decimal = 0
    i = 0
    while binary != 0:
        remainder = binary % 10
        decimal = decimal + remainder*pow(2,i)
        binary = binary//10
        i = i + 1
    return decimal
print(binary_to_decimal(N),"is the binary number")

# Create a list of number inputs

Marks_list = []
x = 0
for x in range(5):
    m = int(input("Enter your marks: "))
    if m > 100 or m < 0:
        break
    elif m < 40:
        print("Sorry you've failed the test, your marks won't get added further in the list")
        break
    else:
        Marks_list.append(m)
if len(Marks_list) > 4:
    print(Marks_list)
    Sum = 0
    for i in Marks_list:
        Sum += i
    average = Sum/5
    print("Sum =",Sum,"and Average =",average)
        
 

    if average >= 75:
        print('Distiction!')
    elif average < 75 and average >= 60:
        print("First class!")
    elif average < 60 and average >= 50:
        print("Second class")
    elif average < 50 and average >= 40:
        print("Third class")
    else:
        print(" ")
     