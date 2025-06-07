#1
name= input("Enter the name: ")
in_file=open("name.txt","w")
print(name, file=in_file)
in_file.close()