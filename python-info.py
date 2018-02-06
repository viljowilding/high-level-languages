### PYTHON

'''
Features:
- Source code consists of a very basic set of instructions, mostly in natural english, with little syntax.
- Needs a translator
  - The most popular Python release, CPython, runs in an IDE which converts
    source code into to C before running
- Files usually end in the .py suffix
- Uses "The Philosophy of Python"
'''

print("Hello World!")

def whatsYourName(msg):
	print(msg)
	temp = input()
	return temp

name = whatsYourName("What's your name, user?\nName: ")
if name == "Albert":
	print("Hey Albert!")
else:
	print("{} is such a lovely name!".format(name))

'''
The Philosophy of Python:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts
'''
