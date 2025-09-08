#List 5 tools used in machining. Write Python code to add and remove tools
#from a list.

tools=['lathes', 'milling machines', 'drilling machines', 'grinding machines', 'shapers', 'planers', 'broaches', 'power saws']
print('Maching Tools',tools)
mtools=str(input("Enter the maching tool to be add: "))
tools.append(mtools)
print("List of Maching Tools",tools)
rtools=str(input("Enter the maching tool to be removed: "))
tools.remove(rtools)
print('List of Maching Tools after removing',tools)