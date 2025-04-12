file_path: str = "/Users/anurag/Desktop/python-idently-learning/_18_file_handling/info.txt"

# The main problem in this method is that if we forget to close the file, it will remain open and may cause memory leaks.

# file: TextIO = open(file_path, 'r')
# text: str = file.read()
# print(text)
# file.close()

# The one solution is to use try and finally block to ensure that the file is closed even if an error occurs.

# try:
#     file: TextIO = open(file_path, 'r')
#     text: str = file.read()
#     raise Exception("An error occurred")
#     print(text)
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print("Forcefully closing the file")
#     file.close()

# The above is also not the ideal solution because if we forget to close the file in the finally block, it will remain open.
# The best solution is to use the with statement, which automatically closes the file when the block is exited.

try:
    with open(file_path, 'r') as f:
        text: str = f.read()
    print(text)
except FileNotFoundError:
    print("File not founded!!")
