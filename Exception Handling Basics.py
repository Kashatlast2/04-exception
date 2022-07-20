#Open File/Resource

try:
    # Business Logic to read
    i = 0   #not hardcode, getting a input from a user
    j = 10/i
    values = [1, 2]
    sum(values)
except TypeError:
    print('TypeError')
    j = 10
except ZeroDivisionError:
    print('ZeroDivisionError')
    j = 0
except:
    print('OtherError')
else:
    print('Else')
finally:
    # Close to Resource
    print('Finally')

print(j)
print('End')


#try:
#    10/0
#except TypeError:
#    print('TypeError')
#except ZeroDivisionError:
#    print('ZeroDivisionError')
#
#print('End')


#try:
#    10/0
#except object:
#    print('ZeroDivisionError')

#print('End')


#try:
#    10/0
#except BaseException:
#    print('BaseException')

#print('End')


#try:
#    10/0
#except (ZeroDivisionError,TypeError):
#    print('BaseException')

#print('End')

#try:
#    sum([1,'1'])
#except TypeError as error:
#    print(error)

#print('End')