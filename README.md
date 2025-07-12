# Assignment4

**TASK 1 :**
 File Not Found Error Handling in Python
This Python script demonstrates basic exception handling while working with files. It attempts to open and read a file named sample1.txt and handles the situation gracefully if the file is missing.

🧠 Key Concepts:
open() function to read from a file

try-except block for error handling

FileNotFoundError exception handling

📌 What the Script Does:
Tries to open the file sample1.txt in read mode ('r').

If the file exists, it reads and prints the content.

If the file does not exist, it catches the FileNotFoundError and prints a user-friendly error message.

🖥️ Sample Output:

Error: The Sample.txt file does not found




**TASK 2 :**

This script performs the following steps:

Asks the user to enter text, then writes it to output.txt.

Asks for additional text, then appends it to the same file.

Reads the final content of output.txt and displays it on the screen.


🔧 Example Output
Enter the text : Hello, Python!
Data added successfully

Enter Additional text to append : Learning file handling in Python.
Data successfully appended

Final content of file is :
Hello, Python!
Learning file handling in Python.
