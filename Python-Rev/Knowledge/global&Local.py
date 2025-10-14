# -----------------------------
# Global vs Local Variables
# -----------------------------

g = 5.25   # global variable

def fun():
    global g        # tells Python we want to use the global 'g'
                    # without this, 'g' inside function would be treated as a new local variable
    a = 10          # local variable
    g = 199         # modifies the global 'g'
    
    print('local:  ', a)   # prints local variable
    print('global: ', g)   # prints modified global variable

fun()
print('Outside :', g)  # shows modified global value (199)


# -----------------------------
# locals() and globals()
# -----------------------------
x, y, z = 5, 1.23, 'Hell'   # global variables

def fun2():
    a, b, c = 1, 2, 3       # local variables
    print("Local Symbol Table:")
    print(locals())         # dictionary of current function's local variables
    
    print("\nGlobal Symbol Table:")
    print(globals())        # dictionary of all globals (variables, functions, modules, etc.)

fun2()
