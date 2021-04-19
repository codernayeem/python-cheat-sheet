# Exception means error

# catching exception
try:
    i = 50 // 0
except:                        # Catching any exception without details
    print("Error Found")

# more complex example
try:
    fl = open("7_exceptions.py", 'r')
    age = int(input("Enter your age : "))
    result = 1000 // age
    # if age == 0, it throws ZeroDivisionError
except FileNotFoundError:               # Catching a exception
    print("File not Found")
except (ZeroDivisionError, ValueError): # Catching multiple exception
    print("Please enter a valid age")
except InterruptedError as e:           #  Catching exception with details
    print("Please enter a valid age")
except Exception as e:                  # Catching any exception with details
    print("Opps :", type(e), e)
else:                     # execute when got no exception
    print("No Errors. Result :", result)
    fl.close()
finally:                  # execute it, whether exception found or not
    print("Done")



# Raising exception
def calc_xfactor(n):
    if n <= 0:
        raise ValueError("n can not be 0 or less")
    return 10 / n

try:
    calc_xfactor(-6)
except ValueError as error:
    print(error)

# Raising exception is time costly
# if that function should run many times and comes the question of perfomance:
# better return a value like: None ...
