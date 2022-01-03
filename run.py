# Source code found at https://www.geeksforgeeks.org/clear-screen-python/
# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear ()
print("               O                  ")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | X | . | . |")

sleep(0.2)
clear ()
print("                                  ")
print("     | . | . | O | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | X | . | . |")

sleep(0.2)
clear ()
print("                                  ")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | X | . | . |")

sleep(0.2)
clear ()
print("                                  ")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | X | . | . |")

sleep(0.2)
clear ()
print("                                  ")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | X | . | . |")

sleep(0.2)
clear ()
print("                                  ")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | . | . | . | . | . |")
print("     | . | . | O | . | . | . | . |")
print("     | . | . | O | . | X | . | . |")
print("                                  ")
print("                                  ")
print("                                  ")
