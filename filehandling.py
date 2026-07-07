try:
    file = open("Data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()

# using with statements
    with open("geek.txt", "r") as file:
     content = file.read()
    print(content)

# w : overwrite in the file 
with open("Data.txt","w") as file:
   file.write("Hello,python \n")
   file.write("File handling is easy with python \n")

print("File written Successfully")


# r: reading file
file = open("Data.txt","r")
content =file.read()
print(content)
file.close()