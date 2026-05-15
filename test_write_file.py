from functions.write_file import write_file
# Test file for write_file.py

print("Results for 'calculator/lorem.txt':")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print()

print("Results for 'calculator/pkg/morelorem.txt':")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print()

print("Results for 'calculator/tmp/temp.txt'")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print()