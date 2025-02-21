import os
import requests

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def search_entire_computer(filename):
    potential_roots = ['C:\\', 'D:\\', 'E:\\']  # Adjust this list as needed
    for root in potential_roots:
        result = find_file(filename, root)
        if result:
            return result
    return None

filename_to_find = "example.txt"
file_path = search_entire_computer(filename_to_find)

if file_path:
    print(f"Found file at: {file_path}")
    url = "http://192.168.1.203:5000/upload"  # Update to your server's URL

    data = {"message": "Hello, here is a file."}
    files = {'file': open(file_path, 'rb')}

    try:
        response = requests.post(url, data=data, files=files)
        print("Server response:", response.text)
    except Exception as e:
        print("Error:", e)
else:
    print("File not found on the computer.")

