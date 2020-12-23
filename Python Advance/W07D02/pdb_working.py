# pdb is inbuilt python debugger

a = input()
b = input()

breakpoint()

def sum_the_values(a,b):
    print("we are inside this function")
    print(int(a)+int(b))


sum_the_values(a,b)

# pdb console appears whenever it sees a breakpoint().
# c(continue) => continue all the leftover code after breakpoint.
# n(next) => runs the very next piece of code.
# s(step inside) => to step inside a function such that enter will work like showing us next line executing instead
# of normal donothing behaviour
# we can use print to know values of the variables at a stage in pdb
# we can also know the datatype by using "whatis"