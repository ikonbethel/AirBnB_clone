#!/usr/bin/env python3
from cmd import Cmd

class Basic(Cmd):
    Cmd.prompt = "(hbnb) "
    def do_greet(self, line):
        print ("hello")
        
    def do_EOF(self, line):
        return True
    
    def do_sum(self, line):
        sum = 0
        for i in line.split():
            sum = sum + int(i)
        print (sum)
    
    def do_quit(self, line):
        return True
    
    def default(self, line):
        print ("unknowns")
    
if __name__ == '__main__':
    Basic().cmdloop()