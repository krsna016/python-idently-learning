file_path: str = '/Users/anurag/Desktop/python-idently-learning/_18_file_handling/info.txt'
# If the file does not exist, it will be created
with open(file_path, 'a') as file:
    file.write('This is a new line.\n')
    file.write('This is another new line.\n')
