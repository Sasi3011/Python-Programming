# Check if a file exists
import os
if os.path.exists('example.txt'):
    print("File exists.")
else:                                         
    print("File does not exist.")

# Python Check File Size
file_size = os.path.getsize('example.txt')
print(f"File size: {file_size} bytes")        

# Python Count Number of Lines in a File
file = open('example.txt', 'r')
lines = file.readlines()
file.close()                                    
line_count = len(lines)
print(f"Number of lines: {line_count}")

# Python Search for a String in Text Files
def search_string_in_files(directory, search_string):           
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file = open(os.path.join(directory, filename), 'r')
            if search_string in file.read():
                print(f"Found '{search_string}' in {filename}")
            file.close()
search_string_in_files('.', 'example')

# Read Specific Lines From a File in Python
file = open('example.txt', 'r')
lines = file.readlines()
file.close()                        
specific_lines = lines[1:4]  
print("Specific lines:", specific_lines)

# Delete Lines From a File in Python
file = open('example.txt', 'r')
lines = file.readlines()
file.close()
file = open('example.txt', 'w')
for line in lines:                          
    if "delete this line" not in line:
        file.write(line)
file.close()

# Writing List to a File in Python
file = open('example.txt', 'w')
my_list = ['apple', 'banana', 'cherry']         
for item in my_list:
    file.write(f"{item}\n")
file.close()

# Python List Files in a Directory
directory = '.'  # Current directory
for filename in os.listdir(directory):         
    if filename.endswith('.txt'):
        print(filename)

# Python Count Number of Files in a Directory
file_count = sum([len(files) for r, d, files in os.walk(directory)])
print(f"Number of files: {file_count}")         

# Python list Files in Directory with Extension txt
for filename in os.listdir(directory):
    if filename.endswith('.txt'):                   
        print(filename)

# Python Remove/Delete Non-Empty Folder
import shutil
directory = 'non_empty_folder'
if os.path.exists(directory):
    shutil.rmtree(directory)  
    print(f"Removed directory: {directory}")
else:
    print(f"Directory {directory} does not exist.")

# Python Get File Creation and Modification DateTime
import datetime
file_path = 'example.txt'
if os.path.exists(file_path):                   
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    print(f"Creation time: {datetime.datetime.fromtimestamp(creation_time)}")
    print(f"Modification time: {datetime.datetime.fromtimestamp(modification_time)}")
else:
    print(f"File {file_path} does not exist.")
