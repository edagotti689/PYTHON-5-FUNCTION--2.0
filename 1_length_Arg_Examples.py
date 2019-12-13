# Example for usage of *arg:

# Python program to illustrate   
# *args for variable number of arguments 
#Example: 1
'''
def myFun(*argv):
    for arg in argv:
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
'''

# Example: 2
# *args with first extra argument 
'''
def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
'''

