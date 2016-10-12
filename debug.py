DEBUG = False

def debug_print(*args):
	global DEBUG
	if DEBUG:
		print(*args)

def debug():
	global DEBUG
	DEBUG = not DEBUG
	print('DEBUG ' + ('ON' if DEBUG else 'OFF'))