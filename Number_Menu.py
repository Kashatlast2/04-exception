number1 = int(input('Enter Number1: '))
number2 = int(input('Enter Number2: '))
print('1 - Add')
print('2 - Subtract')
print('3 - Divide')
print('4 - Multiply')

choice = int(input('Choose Operation: '))

#print(number1 + number2)
#print(choice)
if choice==1:
    result = number1 + number2
    print(number1 + number2)
elif choice==2:
    result = number1 - number2
    print(number1 - number2)
elif choice==3:
    result = number1 / number2
    print(number1 / number2)
elif choice==4:
    result = number1 * number2
    print(number1 * number2)
else:
    print('Invalid Choice')

print(result)