# files_notes
# File I/O using Python
- Data maintained in files is persistent
- Computers store files on secondary storage devices
- solid-state drives, hard disks, and more
- We consider text files in several popular formats
# Some file types
- plain text (see details)
- JSON (JavaScript Object Notation) (see example)
- CSV (comma-separated values) (see example)
- Fixed width format (see example)
# File
- A text file is a sequence of characters
- A binary file (for images, videos and more) is a sequence of bytes
- First character in a text file or byte in a binary file is located at position 0
- In a file of n characters or bytes, the highest position number is n – 1
- For each file you open, Python creates a file object that you’ll use to interact with the file
# End of File
- Every operating system provides a mechanism to denote the end of a file (EOF)
- Some use an end-of-file marker
- Others maintain a count of the total characters or bytes in the file
- Programming languages hide these operating-system details from you
# Standard File Objects
- When a Python program begins execution, it creates three standard file objects:
- sys.stdin—the standard input file object
- sys.stdout—the standard output file object, and
- sys.stderr—the standard error file object.
- Though considered file objects, they do not read from or write to files by - default
- The input function implicitly uses sys.stdin to get user input from the keyboard
- Function print implicitly outputs to sys.stdout, which appears in the command line
- Python implicitly outputs program errors and tracebacks to sys.stderr, which also appears in the command line
- Import the sys module if you need to refer to these objects explicitly in your code—this is rare-
- 
