str="anil kumar"
l=len(str)
try:
    for single_char in l-1:
        print('hi')
except(TypeError):
    print("int object is not iterable")
##############################################
str="anil kumar"
l=len(str)
try:
    for read_single_char in range(l+1):
        print(str[read_single_char])
except(IndexError):
    print("string index out of range")
##############################################
str="anil kumar"
l=len(str)
try:
    for read_single_char in range(l):
        print(str[read_single_char])
except(IndentationError):
    print("string index out of range")
#############################################
dict = {'name':["anil","kumar"]}
try:
    print(dict['anil'])
except(KeyError):
    print("Key Doesn't exist in given dictionary")
###############################################
dict = {'name':["anil","kumar"]}
try:
    dict['name']='pendela'
    pritn(dict)
except(NameError):
    print("name 'pritn' is not defined")

