#coding=utf-8
from mctReader import mctReader as mctrd
import re

class igesReader(object):
	def __init__(self,igesdir,mctdir,pro='1',start_num=1):
		super(igesReader, self).__init__()
		codelist=['106','126']
		fid=open(igesdir,'r')
		conts=fid.readlines()
		fid.close()
		data=[]
		for ii, line in enumerate(conts):
			if line[0:3] in codelist and line[72]=='P':
				data.append(self.polyread(conts,ii,int(line[0:3])))
		self.mct=str('')
		self.tt=data
		self.mct+="*TDN-PROFILE\n"

		for ii,item in enumerate(data):
			item.sort(key=lambda x:x[0])
			beamdata=mctrd(mctdir,[item[0][0],item[-1][0]])
			print(beamdata.elem)
			self.mct += ";----------------------------------------;\n"
			self.mct += "  NAME=%i, %s, %sto%s, 0, 0, SPLINE, 3D\n"%(start_num+ii,pro,beamdata.elem[0],beamdata.elem[1])
			self.mct += "    , USER, 0, 0, NO, \n"
			self.mct += "    STRAIGHT, 0, 0, 0, X, 0, 0\n"
			self.mct += "    0, YES, Y, 0\n"
			for pos in item:
				self.mct+='    %.2f, %.2f, %.2f, NO, 0, 0, 0\n'%(pos[0],pos[1],pos[2])



	def polyread(self,content,loc,code=126):
		if code==126:
			K=int(content[loc].split(',')[1])
			M=int(content[loc].split(',')[2])
			N=K-M+1
			npts=K+1
			skip=7+2*M+N+1+npts
		elif code==106:
			npts=int(content[loc].split(',')[2])
			skip=3

		text=[]
		for a in content[loc:-1]:
			lit=re.split(',|;',a[0:72])
			lit.remove(lit[-1])
			text+=lit
		loclist=text[skip:skip+npts*3]
		pnts=[]

		for n in range(npts):
			pnts.append(tuple([self.myfloat(loclist[3*n+0]),self.myfloat(loclist[3*n+1]),self.myfloat(loclist[3*n+2])]))
		return pnts

	@staticmethod
	def myfloat(datastr):
		try:
			return float(datastr)
		except:
			da=datastr.split('D')
			return float(da[0])*10**int(da[1])
#=====================================================================
if __name__ == '__main__':
	f=igesReader('TestModel/T1.iges','TestModel/T1.mct')







