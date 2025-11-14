f = open('data.txt', 'r+')

#Read the entire file
data = f.read()

#Print the data
print(data)

#write to the file
f.write("This is a new line")

#close the file
f.close()