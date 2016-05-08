#!/usr/bin/env python

def MyClass():
    print "In MyClass"

def main():
    print "In main, that was run from the instantiated class"

if __name__ == "__main__":
    app = MyClass()
