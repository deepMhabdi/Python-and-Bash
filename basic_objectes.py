a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list

b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #tuple

c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #set

convert = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',

}

convert[7] = 'seven' #adding new key-value pair to dictionary

del convert[4] #deleting key-value pair from dictionary
print(convert)

del a[2] #deleting item from list
print(a)
