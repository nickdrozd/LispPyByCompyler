from instructions import *
from llh import *
from parse import parse, schemify
from debug import *

from bytecode import *
# import opmap

def compyle(exp):
	parsed = parse(exp)
	compiled = compExp(parsed).makeCodeObj()
	function = makeFunction(compiled)
	return function	

def compExp(exp):
	'''
	Compiles a Lisp string into an Instruction. 
	That Instruction gets converted into a code 
	object later, and then into a function.
	'''
	lisp = schemify(exp)
	debug_print('Compiling %s' % lisp)

	if isNum(exp):
		debug_print('Number')
		return  numInstr(lisp, exp)

	elif isVar(exp):
		debug_print('Variable')
		return  varInstr(lisp, exp)

	elif isDef(exp):
		debug_print('Define')
		[_, var, val] = exp	
		valInstr = compExp(val)
		return  defInstr(lisp, var, valInstr)

	elif isIf(exp):
		debug_print('If')
		[_, test, then, othw] = exp
		testInstr = compExp(test)
		thenInstr = compExp(then)
		othwInstr = compExp(othw)
		return  ifInstr(lisp, 
			testInstr, thenInstr, othwInstr)

	elif isBegin(exp):
		debug_print('Begin')
		[_, *body] = exp
		return compSeq(body)

	elif isLambda(exp):
		debug_print('Lambda')

		# [_, params, *body] = exp
		# bodyCode = compSeq(body)

		# until we figure out compSeq
		[_, params, body] = exp
		bodyInstr = compExp(body)
		return  lambdaInstr(lisp, params, bodyInstr)

	elif isPrimitive(exp):
		debug_print('Primitive function')
		# assume binary func
		[func, arg1, arg2] = exp
		argInstr1, argInstr2 = map(compExp, (arg1, arg2))
		# func is string, args are Instructions
		return primInstr(lisp, func, argInstr1, argInstr2)

		


def compSeq(seq):
	"compiles each expression in the sequence, but only returns the value of the last one"
	# add name to seq
	result = Instruction()
	while seq:
		[exp, *seq] = seq

		instr = compExp(exp)

		if seq: # don't pop the last one
			instr.addPop()

		# this exposes too much internals
		# figure out how to move this to instructions
		result.code += instr.code
		result.stacksize += instr.stacksize
		result.consts.update(instr.consts)
		result.names.update(instr.names)
		result.varnames.update(instr.varnames)

	return result




















'''
numStr = '5'
numFunc = compyle(numStr)

varStr = 'x'
varFunc = compyle(varStr)

defStr = '(define x 5)'
defFunc = compyle(defStr)

lamStr = '(lambda () 5)'
lamFunc = compyle(lamStr)


ifPrimStr = '(if (- 5 4) (* 4 5) (+ 8 9))'
ifPrimFunc = compyle(ifPrimStr)

eqStr = '(== 4 5)'
eqFunc = compyle(eqStr)
'''

beginStr = '(begin (define x 5) (* x x))'
beginFunc = compyle(beginStr)