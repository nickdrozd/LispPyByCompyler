from opcodes import *

CONSTS = [LOAD_CONST]

NAMES = [LOAD_NAME, LOAD_GLOBAL, 
		STORE_NAME, STORE_GLOBAL]

VARNAMES = [LOAD_FAST, STORE_FAST]

JUMPTARGET = [JUMP_ABSOLUTE, 
	POP_JUMP_IF_TRUE, POP_JUMP_IF_FALSE,
	JUMP_IF_TRUE_OR_POP, JUMP_IF_FALSE_OR_POP]





# primitives

primitives = [
# arithmetic operations
'_+_', '_*_', '-', '/', 
'add1', 'sub1',
# boolean operations
'not', '=', '<', '>', 
'zero?', 'one?', 'eq?',
# type-check operations 
'null?', 'number?', 'list?',
'boolean?', 'symbol?', 
# list operations
'cons', 'car', 'cdr', 
'set-car!', 'set-cdr!', 
'cadr', 'cddr', 'cdadr', 
'caddr', 'cdddr', 'cadddr', 
# I/O operations 
'read', 'display', 
'newline', 'error',
# primitive application operations
'applyNilFunc', 'applyOneFunc', 'applyTwoFunc',
]