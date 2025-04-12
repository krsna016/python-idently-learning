file_path: str = f'/Users/anurag/Desktop/python-idently-learning/_18_file_handling/info.txt'
with open(file_path) as f:  # By-default, the file is opened in read mode
    text: str = f.read(5)  # read the first 5 bytes
    # print(f.read())
    # print(f.read())
    print(text)

# The second read will not print anything because the file pointer is at the end of the file.
# So it is good to store the file in a variable and then print it.

with open(file_path) as f:
    # This is used to read the file line by line
    text_line1: str = f.readline()
    print(text_line1, end=" ")  # By default, it ends with a new line
    text_line2: str = f.readline()
    print(text_line2)

with open(file_path) as f:
    # This is used to read the file line by line and store it in a list
    text_lines: list[str] = f.readlines()
    print(text_lines[0])
