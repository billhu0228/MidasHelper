#coding=utf-8

class mctReader(object):
	def __init__(self,mctdir,therange):
		super(mctReader, self).__init__()

		with open(mctdir,'r') as fid:
			conts=fid.readlines()

		for ii,line in enumerate(conts):
			if line.startswith('*NODE'):
				nres=self.nodeRead(conts,ii)
			elif line.startswith('*ELEMENT'):
				eres=self.elemRead(conts,ii)
		
		ndata={n:(x,y,z) for n,x,y,z in nres}
		
		for item in eres:
			item+=[0.5*(self.n2x(item[1],ndata)+self.n2x(item[2],ndata)),]
		
		rec1=['a',None,None,therange[0]]
		rec2=['b',None,None,therange[1]]
		edata=eres+[rec1,rec2,]
		
		edata.sort(key=lambda x:x[-1])
		
		imin=edata.index(rec1)
		imax=edata.index(rec2)
		self.elem=[0,0]
		
		if imin!=0:
			self.elem[0]=edata[imin-1][0]
		else:
			self.elem[0]=edata[imin+1][0]
		
		if imax!=len(edata)-1:
			self.elem[1]=edata[imax+1][0]
		else:
			self.elem[1]=edata[imax-1][0]

	@staticmethod
	def n2x(n,ndata):
		return ndata[n][0]

	@staticmethod
	def nodeRead(conts,loc):
		data=conts[loc:-1]
		nodedata=[]
		for line in data:
			if line[0]==';' or line.startswith('*NODE') or line=='\n':
				continue
			elif line[0]=='*' and not line.startswith('*NODE'):
				break
			else:
				parse=line.split(',')
				parse=[float(a) for a in parse]
				parse[0]=int(parse[0])
				nodedata.append(parse)
		return nodedata

	@staticmethod
	def elemRead(conts,loc):
		data=conts[loc:-1]
		elemdata=[]
		for line in data:
			if line[0]==';' or line.startswith('*ELEMENT') or line=='\n':
				continue
			elif line[0]=='*' and not line.startswith('*ELEMENT'):
				break
			else:
				parse=line.split(',')
				parse[0]=int(parse[0])
				parse[4]=int(parse[4])
				parse[5]=int(parse[5])
				elemdata.append([parse[0],parse[4],parse[5]])
		return elemdata
#=====================================================================
if __name__ == '__main__':
	ff=mctReader('TestModel\\test.mct',[500,2500])
	
	print (ff.elem)
	#print ff.edata