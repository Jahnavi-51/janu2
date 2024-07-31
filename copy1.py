file_path1 = "C:\\Users\\LENOVO\\Documents\\source.txt"
with open(file_path1, "r") as file1:
    content1 = file1.read()
file_path2 = "C:\\Users\\LENOVO\\Documents\\destination.txt"
with open(file_path2, "w") as file2:
     file2.write(content1)
     print("successfully copied")



