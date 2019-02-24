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
"ped": "foot, child",
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
"cis": "cut",


"crypt(o)": "hidden",
"ab(s)": "away, off, from",
"trop": "turn, change",
"neo": "new",
"nov": "new",
"pos": "put",
"ten": "hold",
"mono": "alone",
"uni": "one",

"term(in)": "limit",
"geo": "earth",
"spher": "ball",
"vert": "turn",
"morph": "shape",
"form": "form",
"doc(t)": "teach",
"tut/i": "teach",
"di(p)": "two",
"bi(n)": "two",
"top": "place",
"cent(e)r": "center",
"dom": "house, master",
"omni": "all",
"hol(o)": "all",
"retro": "back",
"tempor": "time",
"chron": "time",
"tri": "three",

"amni": "breath, soul",
"fig": "shape",
"a/enn": "year",
"ev": "age, lifetime",
"corp": "body",
"tang/tact": "touch, sense",
"codi/e": "trunk, document",
"sign": "sign",
"qua dr/rt": "four",
"tetr"	: 	"four",
"capit"	:	"head",
"anthrop"	:	"human",
"kine"	:	"movement",
"dynam"	:	"power",
"grad"	:	"step, degree",
"reg"	:	"rule",
"crit"	:	"judge, decide",
"jur"	:	"swear, law",
"pent"	:	"five",
"quint"	:	"five",
"bio"	:	"life",
"gen"	:	"birth",
"funct"	:	"perform",
"mut"	:	"change",
"fract"	:	"break",
"tele"	:	"distant",
"phil"	:	"love",
"neg"	:	"say no",
"dec"	:	"ten",
"cent"	:	"hundred",
"nom"	:	"name",
"pat(e)r"	:	"father",
"lega"	:	"appoint, legal",
"greg"	:	"herd",
"flu"	:	"flow",
"prehend/s"	:	"seize",
"temper"	:	"moderate, mix",
"purg"	:	"clean",
"mill"	:	"thousand",
"s/hemi":	"half",
"sub"	:	"under",
"hyper"	:	"beyond",
"pre"	:	"before",
"para"	:	"beside",
"meta"	:	"behind, beyond",
"per"	:	"through",
"ant(i)":	"aganist",
"contra":	"against",


"ac(e)r":	"sharp, sour",
"strict":	"tightly controlled",
"stru(ct)"	:	"put together, build, arrange",
"prop(ri)"	:	"own",
"tort"	:	"twist",
"viv"	:	"live",
"serv"	:	"serve",
"clus"	:	"close",


"text"	:	"weave",
"plac"	:	"please, calm",
"aut(o)":	"self, same",
"grat"	:	"pleasing, welcome",
"cla(i)m"	:	"shout, cry out",
"crac/t":	"power",
"punc"	:	"point",
"pot"	:	"able",


"mand"	:	"entrust, order",
"und"	:	"wave, flood",
"sanct"	:	"holy",
"loqu"	:	"talk",
"vir"	:	"man",
"val"	:	"strength",
"cre(t)":	"grow",
"fus"	:	"pour out, melt",


"verb"	:	"word",
"simi/ul"	:	"similar",
"scend"	:	"climb",
"onym"	:	"name, word",
"scrib/p"	:	"write",
"fall"	:	"deceive",
"solu"	:	"free",
"hydr"	:	"water",


"mur"	:	"wall",
"polis/t"	:	"city",
"number":	"number",
"kilo"	:	"thousand",
"micro"	:	"small",
"multi"	:	"many",
"par"	:	"equal",
"phob"	:	"fear",
"hem(o)":	"blood",
"itis"	:	"disease",
"micro"	:	"small",
"super"	:	"over",
"de"	:	"down, away",
"nul(l)":	"none",
"arm"	:	"weapon, tools",
"surg"	:	"rise",
"strat"	:	"spread, bed",
"later"	:	"side",
"tom"	:	"cut",
"iatr"	:	"healer, physician",
"medi"	:	"middle",
"oid"	:	"appearance, form",
"scop"	:	"look at",
"trans"	:	"through, beyond",
"pro"	:	"for, favor, before",
"re"	:	"again, backward",
"derm"	:	"skin",
"endo"	:	"within",


"necro"	:	"dead body",
"paleo"	:	"ancient",
"circu(m)"	:	"circle",
"mini/u":	"small, least",
"inter"	:	"between",
"sur"	:	"super",
"co"	:	"together",
"syn"	:	"together, at the same time",


"toxi"	:	"poison",
"ten(u)":	"thin",
"techni/o":	"art, skill",
"long"	:	"long",
"idio"	:	"private",
"aer(o)":	"air",
"cad"	:	"fall",
"trib"	:	"give, pay"
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
