#! /usr/bin/python3

from os import system as system

CENTER = 24
N_CLRS = 4
N_MAX_CLRS = 8
BOARD = {
			"pins":["  ".join([ "><" for c in range(0,N_CLRS)]) for i in range(0,N_MAX_CLRS) ],
			"key":()
		}

def getInput(allowed = set(range(1,9))):
	while True:
		try:
			s = input('Select the colors by their number: ')
			s = [int(n) for n in s]
			if len(set(s)) == N_CLRS and len(s) == len(set(s)) and set(s).issubset(allowed): 
				return s
		except ValueError:
			pass


def genSeq(allowed = list(range(1,9))):
	return tuple([allowed.pop(randint(0,len(allowed)-1)) for x in range(0,4)])


def match(t, k):
	return 	{ 
				"placed":[ list(t)[x]==list(k)[x] for x in range(0,len(k)) ].count(True),
				"right":len(set(k).intersection(set(t)))
			}


def printElement(s='', c='-', f='-', w=CENTER):
	print(f+s.center(w,c)+f)


def printBoard(r={"right":-1,"placed":-1}):
	n = r.get("right")
	p = r.get("placed")
	printElement('', f='+')
	printElement('Master Mind'.upper(),c=' ', f='|')
	printElement('', f='+')
	printElement( getColorStr([str(x) for x in range(1,9)], 18, elem='n',sep =''), c=' ', f='|')
	printElement('', f='+')
	for i in BOARD.get("pins"):
		printElement(i, c=' ', f='|')

	printElement('', f='+')
	result='Matched colors: '+ (str(n) if n != -1 else 'X')
	printElement( result , c=' ', f='|')
	result='Matched colors: '+ (str(p) if p != -1 else 'X')
	printElement( result , c=' ', f='|')
	printElement('', f='+')


def getColorStr(t,l=16, elem = '  ',sep='  ', r= ' ', p=' '):
	f= '\033[{};5;{}m{}\033[0m'
	r = f.format('1;38',7,r)
	p = f.format('1;38',1,p)
	s = sep
	s = s.join([f.format('1;48',x,' '+str(x)) if elem =='n' else f.format('1;48',x,'  ')for x in t])
	rhs=((CENTER-l)//2)+(0 if CENTER%2==0 else 1)
	lhs= CENTER-l-rhs
	s=r+" "*rhs+s+" "*lhs+p
	return s


def updateBoard(i, t, r):
	BOARD["pins"][i]= getColorStr(t,16, r= str(r.get("right")), p=str(r.get("placed")))


def game():
	iteration = 0	
	BOARD["key"]=genSeq()
	system('clear')
	printBoard()
	while iteration < 8:
		t=getInput()
		system('clear')
		r=match(t,BOARD.get("key"))
		updateBoard(iteration, t, r)
		printBoard(r=r)
		if r["placed"] == N_CLRS:
			break
		iteration = iteration+1
	else:
		printElement("You lost!", c=' ',f='|')
		printElement(getColorStr(BOARD["key"]), c=' ',f='|')
		printElement('', c='-',f='+')
		return
	printElement("You won!", c=' ',f='|')
	printElement(getColorStr(BOARD["key"]), c=' ',f='|')
	printElement('', c='-',f='+')
	
if __name__ == "__main__":
	from random import randint as randint
	game()