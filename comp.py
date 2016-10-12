from instructions import *
from llh import *
from parse import parse, schemify
from debug import *

from bytecode import *

def compyle(exp):
	parsed = parse(exp)
	compiled = compExp(parsed).makeCodeObj()
	function = makeFunction(compiled)
	return function	

def compExp(exp):
	lisp = schemify(exp)
	debug_print('Compiling ', exp)
	if isNum(exp):
		debug_print('Number')
		return  numInstr(lisp, exp)
	elif isVar(exp):
		debug_print('Variable')
		return  varInstr(lisp, exp)
	elif isDef(exp):
		debug_print('Define expression...')
		[_, var, val] = exp	
		valInstr = compExp(val)
		return  defInstr(lisp, var, valInstr)
	elif isIf(exp):
		debug_print('If expression...')
		[_, test, then, othw] = exp
		testInstr = compExp(test)
		thenInstr = compExp(then)
		othwInstr = compExp(othw)
		return  ifInstr(lisp, 
			testInstr, thenInstr, othwInstr)
	elif isLambda(exp):
		debug_print('Lambda expression...')
		[_, params, body] = exp
		# bodyCode = compSeq(body)
		bodyInstr = compExp(body)
		return  lambdaInstr(lisp, 
			params, bodyInstr)























numStr = '5'
numFunc = compyle(numStr)

varStr = 'x'
varFunc = compyle(varStr)

defStr = '(define x 5)'
defFunc = compyle(defStr)

ifStr = '(if 0 4 5)'
ifFunc = compyle(ifStr)

lambStr = '(lambda () 5)'
lamFunc = compyle(lambStr)
