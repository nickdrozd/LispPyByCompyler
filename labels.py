# labels

labels = []

# label numbering

label_count = 0

def newLabelNumber():
	global label_count
	label_count += 1
	return label_count

def makeLabel():
	global labels
	label = 'label_' + str(newLabelNumber())
	labels += [label]
	return label