# THis one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do THis
def print_two_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
	print "I got nuthin'."


print_two("Chad", "Dibble")
print_two_again("Chad", "Dibble")
print_one("chadthebad")
print_none()