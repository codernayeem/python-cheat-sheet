# the with satement is used to release extra things


# without 'with'
fl = open('8_with_satement.py', 'r')
print("File opened")
data = fl.read()
fl.close()

with open('8_with_satement.py', 'r') as fl:
    # fl.__enter__()   : called at the satrt of with satement
    # fl.__exit__()    : called at the end of with satement
    # at the end, 'with' will automaticly call 'file.close()'
    # do something with the fl
    print("File opened")
    data = fl.read()


with open('8_with_satement.py', 'r') as fl1, open('7_exceptions.py', 'r') as fl2: # multiple file opening
    print("2 File opened")


# this fl/fl1/fl2 has a method : fl.__enter__() and fl.__exit__()
# 'with' satement call __enter__() when start, and at the end call __exit__() of those created variables with 'with'
# So, with statement only works which has __enter__() and __exit__() methods

