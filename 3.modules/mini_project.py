##############
###  This project aims to show some basic concept in Python
###  We will see where it goes and feel free to request 
###  whatever you think could be useful in it !
###
###  I won't describe everything, nor lmgtfy what is easy to find
##############

## imports: this is where you declare external modules / files
##          you want to use in this file.
## be careful setting your PYTHONPATH right!

from same_dir_module import some_function

## this is how you define a function
def run():
    print "I'm in run"
    ## you can call other functions, with arguments
    arg_1 = "hey"
    function_1(arg_1)
    ## or some function you have imported
    some_function()
    

## see how I'm letting 2 blank lines between function declaration when not
## in a class. This function has a positional argument:
def function_1(argument):
    ## you can format what you want to print:
    print "I'm function_1 called with argument {a}".format(a=argument)

## if you call "python mini_project.py" the interpreter will
## execute whatever code which is not in a function like this:
print "I'm lonely code not in a function, this is bad"

## but it will also execute it when importing the module!
## That's why you put this function which checks if you're executing
## or importing this module mini_project:
if __name__ == "__main__":
    print "I'm OK here!"
    run()
