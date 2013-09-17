def main():
# main program for reading unsafe code to variable, executing code if it's safe.
    read_success = 0
    check_char = 0
    usercode = ""
    try:
	      usercode = file("TestSandBox.py").read()
	      print "Read script file successed"		
	      read_success = 1
    except IOError as e:
	      print "Oops! cannot read script file"
    exec usercode

main()
