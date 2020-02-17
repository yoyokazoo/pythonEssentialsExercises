import math

# to see the whole rainbow we want to tick each of RGB up and down one at a time
# Starting with red at 255 and green and blue at 0:
# phase 0: green up to 255
# phase 1: red down to 0
# phase 2: blue up to 255
# phase 3: green down to 0
# phase 4: red up to 255
# phase 5: blue down to 0
def getRGBPhase(ticks):
	phase = int((ticks % 1536) / 256)
	return phase

# takes ticks, normalizes them to 0-255, 
# counting up in even phases and down in odd phases
def getNormalizedTicks(ticks, phase):
	normalized_ticks = ticks % 256
	if phase % 2 == 1: # odd
		return 255 - normalized_ticks
	else:
		return normalized_ticks

def convertTicksToRed(normalized_ticks, phase):
	if phase == 0:
		return 255
	elif phase == 1:
		return normalized_ticks
	elif phase == 2:
		return 0
	elif phase == 3:
		return 0
	elif phase == 4:
		return normalized_ticks
	else: # phase == 5
		return 255

def convertTicksToGreen(normalized_ticks, phase):
	if phase == 0:
		return normalized_ticks
	elif phase == 1:
		return 255
	elif phase == 2:
		return 255
	elif phase == 3:
		return normalized_ticks
	elif phase == 4:
		return 0
	else: # phase == 5
		return 0

def convertTicksToBlue(normalized_ticks, phase):
	if phase == 0:
		return 0
	elif phase == 1:
		return 0
	elif phase == 2:
		return normalized_ticks
	elif phase == 3:
		return 255
	elif phase == 4:
		return 255
	else: # phase == 5
		return normalized_ticks

def getPongPaddleColorForTime(ticks):
	phase = getRGBPhase(ticks)
	normalized_ticks = getNormalizedTicks(ticks, phase)

	print("Phase: {0} normalized_ticks: {1}", phase, normalized_ticks)

	r = convertTicksToRed(normalized_ticks, phase)
	g = convertTicksToGreen(normalized_ticks, phase)
	b = convertTicksToBlue(normalized_ticks, phase)
	return [r, g, b]