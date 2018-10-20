#Yusheng Hu
#L SYSTEM
#VERSION 2
import sys

class Lsystem:
	
	#filename is optional, default is none
	def __init__(self, filename=None):
		self.base=''
		self.rules=[]
		# if the filename variable is not equal to None
		if filename !=None:
			self.read(filename)
			
	def getBase(self):
		return self.base
		
	def setBase(self, b):
		self.base=b
		
	def addRule(self, newrule):
		self.rules.append(newrule)
		
	def read(self, filename):
		fp= file(filename)
		lines=fp.readlines()
		fp.close()
		
		for line in lines:
			words=line.split()
			if words[0]=='base':
				self.setBase(words[1])
			elif words[0]=='rule':
				self.addRule(words[1:])
				
	def replace(self, istring):
  # assign to a local variable (e.g. tstring) the empty string
		tstring=''
  # for each character c in the input string (istring)
  		for c in str(istring):
  			found=False
			for rule in self.rules:
				if rule[0]==c:
					tstring+=rule[1]
					found=True
					break
			if not found:
				tstring+=c
		return tstring
    
    
	def buildString(self, iterations):
	# assign to a local variable (e.g. nstring) the base field of self
		nstring=self.base
		for i in range(iterations):
			nstring=self.replace(nstring)
		return nstring
	def __str__(self):
	#for extension 3
		str = ''
		str += 'base '
		str += self.getBase()
		str += "\n"
		for r in self.rules:
			str += "rule "
			str += r[0]
			str += ' '
			str += '->'
			str +=r[1]
			str +='\n'
		
		return str
def main(argv):
	
  if len(argv) < 3:
	print 'Usage: lsystem.py <filename> <iterations> <output file>'
	exit()

  filename = argv[1]
  iterations = int(argv[2])
  outfile = argv[3]

  lsys = Lsystem()

  lsys.read( filename )

  print lsys

  

  lstr = lsys.buildString( iterations )

  fp = file( outfile, 'w' )
  fp.write(lstr)
  fp.close()

  return


if __name__ == "__main__":
  main(sys.argv)
