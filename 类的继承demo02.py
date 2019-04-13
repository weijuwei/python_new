#!/usr/bin/python3

class Parent:
    def myMethod(self):
        print("This is parent method")

class Child(Parent):
    def myMethod(self):
        print("This is child method")

c = Child()
c.myMethod()
super(Child,c).myMethod()
