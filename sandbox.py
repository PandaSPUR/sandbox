import sys
import resource
import __builtin__


# resource limitation ###########
# set 200 MB memory limit and 5 seconds cpu time
Mega = 2**20
resource.setrlimit(resource.RLIMIT_AS, (200*Mega,200*Mega))
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
from os import nice
nice(1)
#resource.setrlimit(resource.RLIMIT_NOFILE, (0, 0))
# end resource limitation #######

# define safe content ##################
scope = __builtin__
unsafe = ['open', 'execfile', 'compile', 'reload', '__import__', 'eval', 'input', 'apply', 'exit', 'quit', 'raw_input', 'dir', 'globals', 'locals', 'vars']
for func in unsafe:
	del scope.__dict__[func]

# main function #################
def main(program):
	read_success = 0
	try:
		usercode = file(program).read()
		print "Read script file successed"		
		read_success = 1
	except IOError as e:
		print "Oops! cannot read script file"
	if read_success:
		exec usercode in scope.__dict__
# end main function #############

main(sys.argv[1])
