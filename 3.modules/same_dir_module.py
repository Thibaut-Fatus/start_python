## This is a module I've written to demonstrate import strategies


## this function is imported by mini_project
## it has a default argument
## you can call the function with or without an argument
## you can even call it with a keyword argument: see main function
def some_function(arg="without argument"):
    print("I'm some_function called {t}".format(t=arg))


if __name__ == "__main__":
    ## here I'm using a keyword argument
    ## you can see that I'm not executing this code when importing same_dir_module
    some_function(arg="from same_dir_module")
