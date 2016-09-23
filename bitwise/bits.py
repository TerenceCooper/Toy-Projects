#!/usr/bin/env python3
''' Functional wrapper around the bitwise operators.
Designed to make their use more intuitive to users not
familiar with the underlying C operators.
Extends the functionality with bitmask read/set operations.

The inputs are integer values and
return types are 16 bit integers or boolean.
bit indexes are zero based.

Functions implemented are:
    NOT(int)              -> int
    AND(int, int)         -> int
    OR(int, int)          -> int
    XOR(int, int)         -> int
    shift_left(int, num)  -> int
    shift_right(int, num) -> int
    bit(int, idx)         -> bool
    setbit(int, idx)      -> int
    zerobit(int, idx)     -> int
    listbits(int, num)    -> [int, int..., int]
'''

def NOT(value):
	return ~value

def AND(val1, val2):
	return val1 & val2

def OR(val1, val2):
	return val1 | val2

def XOR(val1, val2):
	return val1^val2

def shift_left(val, num):
	return val << num

def shift_right(val, num):
	return val >> num

def bit(val, idx):
	mask = 1 << idx
	return bool(val & 1)

def setbit(val, idx):
	mask = 1 << idx
	return val | mask

def zerobit(val, idx):
	mask = ~(1 << idx)
	return val & mask

def listbits(val):
	num = len(bin(val)) - 2
	result = []
	for n in range(num):
		result.append( 1 if bit(val,n) else 0)
	return result
