# Create a program that calculates and prints multiples of pi up to 100.  The output should look like:
#
# 1π=3.141592653589793
# 2π=6.283185307179586
# 3π=9.42477796076938
# 4π=12.566370614359172
# 5π=15.707963267948966
# ...
# 99π=311.01767270538954
# 100π=314.1592653589793
#
# Use the '+' sign to concatenate strings. If you are having trouble printing out a combination of letters and numbers,
# use the str() method to cast (convert) a number to a string.  So for example:
# x = 4 - 3
# print("Peter B is #" + str(x))

import math

for x in range(1, 101):
	print(str(x) + "π=" + str(x*math.pi))