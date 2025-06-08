#1
name= input("Enter the name: ")
in_file=open("name.txt","w")
print(name, file=in_file)
in_file.close()

#2
in_file=open("name.txt","r")
name=in_file.read().strip()
print(f"Hi {name}!")

#3
with open("numbers.txt","r") as in_file:
    first_number= int(in_file.readline())
    second_number= int(in_file.readline())
result=first_number+second_number
print(result)

#4
total=0
with open("numbers.txt","r") as in_file:
    for line in in_file:
        total += int(line)
print(total)