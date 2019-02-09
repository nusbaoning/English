from __future__ import print_function
import random
import sys
# baoning
# created 2019.2.9
# latest edited 2019.2.9

d = {
"bene": "well",
"am": "love",
"bell": "war",
"pac": "peace",
"crim": "crime",
"prob": "prove",
"grav": "heavy",
"lev": "lighten",
"mania": "madness",
"psych": "breath",
"cept": "seize",
"fin": "end",
"ject": "throw",
"tract": "drag",
"duc(t)": "lead",
"sequ": "follow"
}


print("input #words of test:")
a = int(input())
random.seed()
b=0
c=a
i=0
while a>0:
	p = 1.0*a/len(d)
	# print(p, a, type(p))
	# if(i>50):
		# sys.exit(-1)
	l = list(d)
	for key in l:
		roll = random.random()
		# print(roll, roll<p)
		i+=1
		if roll < p:
			print(key)
			if raw_input()=="n":
				b += 1
			print(d[key])
			del d[key]
			a-=1
		if a<=0:
			break
print("correct rate", round(100.0*(c-b)/c,2))
