# A recursion is a method that call itself until it doesnt
# Some terminology:
# --Base Case --: A recursion method needs to have a Base Case, which is something that stop the recursion
# loop requires a return. Is a condition that stops the recursive case, needs to be True at some point to
# avoid stack overflow.
# --Recursive case--: Is the call for the recursion
# --Call Stack---: A call stack is a stack that stores the information about the subroutines of a program, the reason
# to have this stack is to keep track of the point to which each active subroutine should return control when
# it finish executing, example of a code using the code stack:
# def funcThree:
#     print("3")
# def funcTwo:
#     funcThree()
#     print ("2")
# def funcOne:
#     funcTwo()
#     print ("1")
# funcOne()
# When functOne() is called, it will then call funcTwo and then funcThree, is we have a debugger we can keep track of
# each method and see when they are pushed into the stack and when they are being pop.
# Use recursion to solve the factorial, if you use a debugger you can see how they keep track of each function
# recursively with the call stack, the function has the same name but you can see how the n parameter keep changing
# until the top of the call stack is factorial(1) and from there it will start to pop and returning the value
# to the below subroutine in the call stack, it will do that until we reach our results.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(4))
