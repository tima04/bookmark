#!/usr/bin/env python
import os
import sys
import json

file_ = "/home/kothiyal/.jump.json"

def jump(arg, up=True):
    if up:
        os.chdir("../"*arg)
        print (os.getcwd())
    else:
        try:
            dir_ = json.load(open(file_, "r"))[arg]
            os.chdir(dir_)
            print (os.getcwd())
        except:
            print ("Error: alias does not exist")

def alias(arg) :
    try:
        table = json.load(open(file_, "r"))
    except:
        table = {}
    table[arg] = os.getcwd()
    json.dump(table, open(file_, 'w+'))
    return None

def show():
    try:
        table = json.load(open(file_, "r"))
    except:
        table = {}
    rslt = ""
    for k, v in table.items():
        rslt += "%s: %s,"%(k, v) + "\n"
    print (rslt)

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 3 or n < 2:
        print ("wrong usage: supply 1 or 2 arguments")
    if n == 3: # alliasing
        assert sys.argv[1] == "a", "Error: wrong argument."
        alias(sys.argv[2]) 
    else: #n = 2, either jump up or to the alias or show aliases
        arg = sys.argv[1]
        if arg == "s":
            show()
        elif arg in [str(x) for x in range(20)]:
            jump(int(arg), up=True)
        else:
            jump(arg, up=False)
