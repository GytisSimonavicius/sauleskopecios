#Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.

def divider(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You cant divide by zero")
    else:
        print("Answer is :", result)
    finally: 
        # this block is always executed  
        print('This is always executed')  
 
divider(10, 2)
divider(10, 0)