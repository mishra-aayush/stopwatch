'''
Program to replicate a stopwatch
'''

import time

print('\nPress enter to start the stopwatch')
print('Press Ctrl+C to stop the stopwatch')

input()

print('\nStopwatch Started')

startTime = time.time()
lastTime = startTime
lapCount = 1

try:
	while True:
		input()
		lapTime = time.time()

		currLapTime = round(lapTime-lastTime,2)
		totalTime = round(lapTime-startTime,2)
		print('Lap {}: Lap Time = {} \t Total Time = {}'.format(lapCount, currLapTime, totalTime))

		lastTime = lapTime
		lapCount += 1
		continue

except KeyboardInterrupt:
	print('\nStopwatch Stopped!')
	