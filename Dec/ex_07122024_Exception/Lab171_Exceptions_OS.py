import os
try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path+"\example.txt"
    print(full_path_file)

# Read the File

    file = open(full_path_file) #FileNotFoundError: [Errno 2] No such file or directory:
except Exception as fnfe:
    print("File not found ,fix the path or create a file")
finally:
   print("This code will be executed anyhow")