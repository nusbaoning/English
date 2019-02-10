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
"sequ": "follow",


"ambi": "on both sides",
"epi": "on",
"hyp(o)": "below",
"therm": "warm",
"poly": "many",
"prim": "first",
"hom(o)": "same",
"dis": "apart, not",


"vor": "eat",
"carn": "meat",
"cred": "believe",
"fid": "faith",
"curr/s": "run",
"ped": "foot",
"flect": "bend",
"post": "after",


"mal": "bad",
"cata": "down",
"prot(o)": "first formed",
"ante": "before",
"ortho": "straight, right",
"rect": "straight, right",
"eu": "well",
"dys": "difficult",


"equ": "equal",
"qu i/e r/s": "seek",
"ple(n)": "fill",
"met(e)r": "measure",
"aud": "hear",
"son": "sound",
"err": "wander",
"ced": "proceed",


"vis": "see",
"spect": "see",
"voc": "speak",
"phon": "speak",
"cur": "care",
"peri": "around",
"sens": "sense",
"soph": "wisdom",


"port": "carry",
"pend": "hang",
"pan": "all",
"extra": "beyond",
"phot": "light",
"luc": "light",
"mor(t)": "death",
"troph": "nourishment",


"her": "stick",
"fug": "escape",
"cosm": "order",
"sci": "understand",
"junct": "join",
"part": "part",
"mis": "send",
"pel": "drive",


"put": "think",
"log": "word, speech, reason",
"terr": "earth",
"mar": "sea",
"path": "feeling, suffering",
"pe/un": "punish",
"mat(e)r": "mother",
"aqu": "water",


"c(h)ant": "sing",
"lingu": "tongue, language",
"spir": "breath",
"ver": "truth",
"turb": "disturb",
"volu/v": "roll",
"fac": "make, do",
"lum": "light",


"umbr": "shadow",
"vest": "dress",
"the(o)": "god",
"icon": "image",
"urb": "city",
"cult": "care",
"dem(o)": "people",
"popul": "people",


"cord": "heart",
"culp": "guilt",
"dict": "speak",
"gni/o": "know",
"graph": "write",
"art": "skill, cleverness",
"fort": "strong",
"cis": "cut"

}


a = int(input("input #words of test:"))
random.seed()
b=0
c=a
i=0
while a>0:
	p = 1.0*a/len(d)
	# print(p, a, type(p))
	# if(i>50):
		# sys.exit(-1)
	l = d.keys()
	
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
print("correct rate", round(100.0*(c-b)/c,2), "%")
