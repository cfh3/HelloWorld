#!/usr/bin/env python


class MyClass:
    def __init__(self):
        print "In --> MyClass.__init__()"


def main():
    print "In --> main()"


if __name__ == "__main__":
    app = MyClass()
    main()