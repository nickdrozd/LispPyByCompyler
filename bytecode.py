# from dis import dis
import dis
from types import CodeType, FunctionType
from opcode import opmap, cmp_op

def opref(num):
    s = []
    for k in opmap:
        v = opmap[k]
        if v == num:
            s += [k]
    return s[0] if len(s) == 1 else s

def code_attr(obj):
    typeName = obj.__class__.__name__

    if typeName == 'function':
        code = obj.__code__
    elif typeName == 'code':
        code = obj
    elif typeName == 'str':
        code = compile(obj, '', 'eval')

    for attr in dir(code):
        prefix = attr[:3]
        if prefix == 'co_':
            suffix = str(attr[3:])
            if suffix in ['code', 'lnotab']:
                print(suffix + ': ' + str(list(getattr(code, attr))))
            else:
                print(suffix + ': ' + str(getattr(code, attr)))

def inspect(func):
    dis.dis(func)
    code_attr(func)

def rec(n):
    print(n)
    if n == 0:
        return 1
    else:
        return n * rec(n-1)

def acc(n, t):
    if n == 0:
        return t
    else:
        return acc(n-1, t * n)

def loop(n):
    t = 1
    while n > 0:
        t *= n
        n -= 1
    return t


def print5():
    print(5)
    return 5


byterec_code = CodeType(1, 0, 1, 4, 67,
                   bytes([
                    116, 1, 0, 
                    100, 2, 0, 
                    124, 0, 0,
                    131, 2, 0,
                    1,

                    124, 0, 0, 
                    100, 0, 0,
                    107, 2, 0,
                    114, 29, 0,
                    
                    100, 1, 0,
                    83,
                    
                    124, 0, 0,
                    116, 0, 0,
                    124, 0, 0,
                    100, 1, 0,
                    24,
                    131, 1, 0,
                    20,
                    83,
                    ]),
                    (0, 1, 'n: '), ('byterec', 'print'), ('n',),
                    'file',
                    'byterec', 0,
                    b'', (), ())

byterec = FunctionType(byterec_code, globals())

five_code = CodeType(0, 0, 0, 1, 0,
                     bytes([100, 0, 0, 
                            83]),
                     (5,), (), (),
                     '', 'five', 0,
                     b'', (), ())

five = FunctionType(five_code, {})

var_code = CodeType(0, 0, 0, 1, 0,
                     bytes([124, 0, 0, 
                            83]),
                     (), (), ('x',),
                     '', 'var', 0,
                     b'', (), ())

var = FunctionType(var_code, {})

def define():
    a = 3
    b = 4
    global x
    x = a * b
    return x


def f():
    return lambda x: x**2

def g():
    def h():
        return 5
    return h

def set_x(n):
    x = n**2
    def setx(n):
        global x
        x = n
    setx(n)
    return x

crash = FunctionType(
            CodeType(
                0,0,0,0,0,
                bytes([1]),
                (),(),(),
                '','',0,b'',
                (),()
                ), 
            {})

ifl = lambda : (5 if 0 else 6) + 4


def a():
    global x
    x = 5