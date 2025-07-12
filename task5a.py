try:
    file = open('sample1.txt' , 'r' )
    file_read = file.read()
    print( file_read)
except FileNotFoundError:
    print("Error: The Sample.txt file does not found ")
    