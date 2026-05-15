# Create File
# Write / Append
# Read
# Save

# open() by using open method we can perform file operations
# with open() by this method also we can perform file operations.

"""
file modes:
w: write -> if file is not there, it will create and write the data,
            if already file exists it will override the data (means eventhough if data is present again it will print the data).
r : read: -> if file exists it will read the data otherwise it will throw exception ( file not found exception)
a : append -> it will append the data at the end of the file.

methods used to write the data  :-
write : it will write single line,
writelines : we can write multiple lines

methods to read the data :-
read : it will read all the data into one single str
readline : it will read only one line at once.
readlines : it will read all the lines and it will return a list of lines.
"""
# FileNotFoundError:
# This exception occurs when the specified file does not exist.

# PermissionError:
# This exception occurs when Python does not have permission to access the file or folder.

# UnboundLocalError:
# This exception occurs when a local variable is used before assigning a value.

# StopIteration:
# This exception occurs when no more elements are available in iterator.

# TypeError:
# This exception occurs when operation is performed on wrong datatype.

# ValueError:
# This exception occurs when correct datatype but invalid value is given.

# IndexError:
# This exception occurs when accessing invalid index from sequence.

# KeyError:
# This exception occurs when dictionary key does not exist.

# ZeroDivisionError:
# This exception occurs when dividing number by zero.

# print("first file program")
# obj = open("demo.txt","w")
# obj.write("Hello file handling concept in python")
# obj.write("\n")
# obj.write("Heerendra.\n")
# obj.write("Babu.\n")
# # obj.write(["fourthline\n","fifthline"]) if i use this i will get "TypeError: write() argument must be str, not list"
# obj.writelines(["fourthline\n","fifthline"])
# obj.close()

# print("second file handling programme")
# def file_handling_Ex(filename,mode):
#     try:
#         obj = open(filename,mode)
#         obj.write("second example of file handling with try except and finally blocks.\n")
#         obj.write("hello")
#     except PermissionError as e:
#         print("got the permission exception", e)
#     except FileNotFoundError as e:
#         print("file not founded in you directory : ", e)
#     finally:
#         obj.close()
#
# file_handling_Ex("SecondExample_fileHandling.txt","w")

print("3rd file handling program :")
def reading_the_file(filepat,mode):
    try:
        if mode == "w":
            obj = open(filepat,mode)
            obj.write("3rd example")
        elif mode == "r":
            obj = open(filepat,mode)
            #obj.read()
            print(obj.read())
    except FileNotFoundError as e:
        print("file is not there to read ",e)
    finally:
        obj.close()

reading_the_file("demo.txt","w")
reading_the_file("demo.txt","r")


print("Mithilesh")
print("sathish reddy")
print("shiva")
print("sai")