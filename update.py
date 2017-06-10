#!/usr/bin/env python
import urllib2
import sys
import os

start = "\033[1m"
end = "\033[0;0m"
major = sys.version_info.major
major_str = str(major)

f = open(".version")
ver = f.read()
print "What do you want to update ?: "
answer =raw_input("(" + start +"S"+ end + "cript version/"+ start +"P" + end +"ython version of script) ->  ")
print answer
if answer == "s" or "S":
    print "# Checking fo latest version ..."
    ctvr = urllib2.urlopen("https://raw.githubusercontent.com/whtn12/meow-tool/master/.version").read()
    if float(ver) == float(ctvr):
        print "# You have the latest version! :"
        print ver
    else:
        print "# If you don't have git client please exit !!"
        os.system("git clone https://github.com/whtn12/meow-tool.git ../")
elif answer == "p" or "P":
    print "[*] checking you major python version ..."
    print "[*] Major version is " + major_str
    if major == 2:
        print "--> You script is already compatible !!"
    else:
        os.system("2to3 -w __main__.py")
else:
    print "Please choose a valid option"
