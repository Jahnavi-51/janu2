file_path = "C:\\Users\\LENOVO\\Documents\\output.txt"
with open(file_path, "w") as file:
     c = input("enter the content : ")
     file.write(c)
     print("sucessfully created!!!")
