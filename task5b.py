text_write = input('Enter the text :')
file = open('output.txt' , 'w')
file1 = file.write(text_write + '\n')
print('Data added successfully')

text_append = input('Enter Additional text to append : ')
file = open('output.txt' , 'a')
file2 = file.write(text_append + '\n' )
print('Data successfully appended')

file = open('output.txt' , 'r')
file3 = file.read()
print('Final content of file is :\n' , file3)



