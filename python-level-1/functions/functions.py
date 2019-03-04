# functions group togeher a set of statement that are ment to repeatselself.

#############################################
# This is a simple function
############################################
def my_fuction(pram1 ="default"):

    """
    THIS IS HOW YOU CAN DOCUMENT WHAT THE FUNCTION IS DOING.

    """
    print("my first function!")

my_fuction()
############################################



#############################################
# This will call the pram when the script is run
############################################
def my_fuction(pram1 ="default"):
    print("my first function! {}" .format(pram1))

my_fuction()
############################################

############################################
# This is a simple function
############################################
def my_fuction(pram1 ="default"):
    print("my first function!")

my_fuction()
############################################


#############################################
# This hot to return an output of a function
############################################
test = "testing hello"

def hello():
    return (test)

result = hello()
print (result)
############################################

#############################################
# This is how to verify the input is what is expected
############################################
def addNum (num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need intergers!"

result = addNum("2",3)
print (result)
############################################

#############################################
# Another example with strings
############################################
def addStrings (str1, str2):
    if type(str1)==type(str2)==type("string"):
        return str1+str2
    else:
        return "Sorry, I a string!"

result = addStrings(1,"Second Word")
print (result)
############################################
