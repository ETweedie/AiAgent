from functions.get_file_content import get_file_content

print("Results for lorem.txt:")
content = get_file_content("calculator", "lorem.txt")
split_content = content.split("[")
print(f"Length: {len(content)}")
print(f"[{split_content[1]}")
print()

print("Results for main.py")
print(get_file_content("calculator", "main.py"))
print()

print("Results for pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("Results for /bin/cat")
print(get_file_content("calculator", "/bin/cat"))
print()

print("Results for pkg/does_not_exist.py")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
