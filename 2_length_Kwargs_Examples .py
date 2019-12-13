# *kargs for variable number of keyword arguments 
 

# Example:1

''' 
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')

'''
# Example: 2

# variable number of keyword arguments with 
# one extra argument.
 
'''
def myFun(arg1, **kwargs):  
    print("First arg1", arg1)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')
'''
