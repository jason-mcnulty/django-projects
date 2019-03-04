# Lambda Expression



# filtering



#############################################
# Examples of classic functions
#############################################
mylist = [1,2,3,4,5,6,7,8]

def even_bool (num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))
#############################################

#############################################
mylist = ["tom", "jan", "mike"]

def even_bool (str):
    return str == "mike"

evens = filter(even_bool, mylist)
print(list(evens))
#############################################


#############################################
# Lambda Expression
# this produces the same output but is less lines of code
#############################################
mylist = [10,20,36,47,54,60,73,84]

evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens))
#############################################


#############################################
# Using the IN method
# In will find if it is in the list
#############################################
print ('x' in [1,2,3])
#############################################

#############################################
# looking for a letter in a word does not work
#############################################
print ('a' in ['adam', 'bob', 'john'])
#############################################
