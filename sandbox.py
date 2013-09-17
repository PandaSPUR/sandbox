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
resource.setrlimit(resource.RLIMIT_NOFILE, (4,4))
### end resource limitation 

scope = __builtin__ # prepare dictionary for interpreter excutes.
unsafe = ['execfile', 'compile', 'reload', '__import__', 'eval',
          'input', 'apply', 'exit', 'quit', 'raw_input', 'dir', 'globals',
          'locals', 'vars']
forbiddenword = [".os", ".write", "open", "close", "execfile", "compile",
                 "reload", "exit", "quit", "raw_iput", "dir", "globals",
                 "locals", "vars", "import"]
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
        for word in forbiddenword:
	    if word in usercode:
                print "There is an arbitrary code or forbidden word, " + word
                usercode = ""
        exec usercode in scope.__dict__

main(sys.argv[1])
