# Writing data to a file is different from appending data, as it overwrites the existing data in the file.
file_path: str = '/Users/anurag/Desktop/python-idently-learning/_18_file_handling/info.txt'
with open(file_path, 'w') as file:
    file.write('This is a new line.\n')
    file.write('This is another new line.\n')
    file.write('This is yet another new line.\n')
