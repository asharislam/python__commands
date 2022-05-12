"""f = open("data.txt", "x")"""

######################
"""first_side = input("give me a file name please: ")
extention = input("give me a file extention please: ")
filename = first_side + "." + extention
try:
    open(filename, "x")
except:
    print("This type of name already exits")"""

"""##############################################
 open(name, mode)
 x = file_create
 r = read
 w = write
 a = append, update
 + = for_called two mode together
 ##################################################"""

"""write_name = open("data.txt", "w")
write_name.write("Hello world")
write_name.close()"""
###############################################
#write a programme to data.txt file
"""filename = open("ashar.txt", "w")
filename.write("Hello Bangladesh")
filename.close()"""
######################
"""read_name = open("data.txt", "r")
print(read_name.read())
read_name.close()"""
##############################
#update data in file(append)
"""w_s = input("plese write something to a add file: ")
speach = "\nw_s"
f_n = input("please file name: ")
f_n2 = f_n + ".txt" 
append_name = open(f_n2, "a") #######not solve
append_name.write("\n w_s")"""
##########################################
"""first_file_name = input("File Name Please: ")
file_name = first_file_name  + ".txt"

first_writing = input(" write_something: ")


append_name = open(file_name, "a")
append_name.write( first_writing)"""
##############################################
"""append_name = open("data.txt", "a")
append_name.write('\n"Hello bangladesh"')"""

#############################################
"""with open("data.txt", "r+") as f:
    print(f.read())"""
############################################
 with open("example.txt", "r") as f:
     print(f.read())





