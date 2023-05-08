#!/usr/bin/python3
import builtins as b
b.print(__import__('re').sub('[^A-Za-z]+', ' ', b.str(__file__))[2:] + ' that combines remarkable power with very clear syntax')
