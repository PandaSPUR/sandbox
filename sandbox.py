import sys
import resource
import __builtin__
import time
import os
### resource limitation
Mega = 2**20 
resource.setrlimit(resource.RLIMIT_AS, (200*Mega,200*Mega))# 200MB memory limit
resource.setrlimit(resource.RLIMIT_CPU, (60, 60)) # limit 60 second cpu time
os.nice(1) # make process to low priority
resource.setrlimit(resource.RLIMIT_NPROC, (0,0))
path = os.getcwd()
os.chmod(path, 333)
### end resource limitation 

scope = __builtin__ # prepare dictionary for interpreter excutes.
unsafe = ['execfile', 'compile', 'reload', '__import__', 'eval',
          'input', 'apply', 'exit', 'quit', 'raw_input', 'dir', 'globals',
          'locals', 'vars']
for func in unsafe:
    del scope.__dict__[func] # delete unsafe command
    
def main(program):
# main program for reading unsafe code to variable, executing code if it's safe.
    read_success = 0
    check_char = 0
    try:
	usercode = file(program).read()
	print "Read script file successed"		
	read_success = 1
    except IOError as e:
	print "Oops! cannot read script file"
    if read_success:
        if 'os.' in usercode:
	    print "There is an arbitrary code inside, do exit"
            usercode = ""
        else:
	    for letter in usercode:
	        if letter == "_":
                    check_char = 1
            
            if check_char == 1:
                print "There is _ in your code that may harm your system."
                print "Press ctrl+c in 10 second to BREAK, or wait to continue"
                time.sleep(1)
                exec usercode in scope.__dict__
            else:
                exec usercode in scope.__dict__

main(sys.argv[1])
