from opcodes import *

CONSTS = [LOAD_CONST]

NAMES = [LOAD_NAME, LOAD_GLOBAL, 
		STORE_NAME, STORE_GLOBAL]

VARNAMES = [LOAD_FAST, STORE_FAST]

JUMPTARGET = [JUMP_ABSOLUTE, 
	POP_JUMP_IF_TRUE, POP_JUMP_IF_FALSE,
	JUMP_IF_TRUE_OR_POP, JUMP_IF_FALSE_OR_POP]


# primitive functions

arithFuncs = {
	'+' : BINARY_ADD,
	'*' : BINARY_MULTIPLY, 
	'-' : BINARY_SUBTRACT, 
	'/' : BINARY_TRUE_DIVIDE,
	'//': BINARY_FLOOR_DIVIDE,
	'**': BINARY_POWER, 
	'%' : BINARY_MODULO,
}

def getOpCode(func):
	return arithFuncs[func]

def getCompIndex(func):
	return cmp_op.index(func)