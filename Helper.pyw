#coding=utf-8
import sys
from PyQt4 import QtCore, QtGui
from igesReader import igesReader as igesrd

#------------------------------------------------

class mainDialog(QtGui.QDialog):
	def __init__(self,parent=None):
		super(mainDialog, self).__init__(parent)
		tabWidget = QtGui.QTabWidget()
		tabWidget.addTab(PreTab(),u"预应力钢束")

		buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
		buttonBox.accepted.connect(self.accept)
		buttonBox.rejected.connect(self.reject)

		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(tabWidget)
		mainLayout.addWidget(buttonBox)

		self.setLayout(mainLayout)
		self.setWindowTitle(u"Midas助手 v1.0 ---By BillHu")
		
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("resource/16px.png"))
		self.setWindowIcon(icon)

		
class PreTab(QtGui.QWidget):
	def __init__(self,parent=None):
		super(PreTab, self).__init__(parent)

		Label1 = QtGui.QLabel(u"选择钢束文件:")
		Label4 = QtGui.QLabel(u"选择主梁数据:")
		Label2 = QtGui.QLabel(u"输入起始编号:")
		Label3 = QtGui.QLabel(u"输入钢束属性:")
		
		self.LE1 = QtGui.QLineEdit()
		self.LE4 = QtGui.QLineEdit()
		self.LE2 = QtGui.QLineEdit()
		self.LE3 = QtGui.QLineEdit()

		self.LE1.setPlaceholderText(u"选择钢束文件")
		self.LE4.setPlaceholderText(u"选择主梁数据")
		self.LE2.setPlaceholderText(u"输入起始编号")
		self.LE3.setPlaceholderText(u"输入钢束属性")

		self.FB1 = QtGui.QPushButton(u"打开...")
		self.FB1.clicked.connect(self.getIGES)
		self.FB2 = QtGui.QPushButton(u"打开...")
		self.FB2.clicked.connect(self.getMCT)

		mctGenButton = QtGui.QPushButton(u"生成")
		mctGenButton.clicked.connect(self.mctGeneration)

		self.mctListBox = QtGui.QPlainTextEdit()
		self.mctListBox.setReadOnly(True)

		mainLayout = QtGui.QGridLayout()
		mainLayout.setColumnMinimumWidth(1, 250)
		mainLayout.addWidget(Label1,0,0)
		mainLayout.addWidget(Label4,1,0)
		mainLayout.addWidget(Label2,2,0)
		mainLayout.addWidget(Label3,3,0)
		mainLayout.addWidget(self.LE1,0,1)
		mainLayout.addWidget(self.LE4,1,1)
		mainLayout.addWidget(self.LE2,2,1,1,2)
		mainLayout.addWidget(self.LE3,3,1,1,2)

		mainLayout.addWidget(self.FB1,0,2)
		mainLayout.addWidget(self.FB2,1,2)

		mainLayout.addWidget(self.mctListBox,4,0,1,2)
		mainLayout.addWidget(mctGenButton,   4,2)
		self.setLayout(mainLayout)

	def getIGES(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self,u"打开",self.LE1.text(),"IGES (*.iges)")
		if fileName:
			self.LE1.setText(fileName)

	def getMCT(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self,u"打开",self.LE4.text(),"Midas MCT (*.mct)")
		if fileName:
			self.LE4.setText(fileName)

	def mctGeneration(self):
		filedir=self.LE1.text()
		mctdir=self.LE4.text()
		s_num=int(self.LE2.text())
		pro  =self.LE3.text()
		parse=igesrd(filedir,mctdir,pro,s_num)
		self.mctListBox.clear()
		self.mctListBox.insertPlainText(parse.mct)

		clipboard = QtGui.QApplication.clipboard()
		clipboard.setText(parse.mct)

		msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u"提醒", u"MCT命令已拷贝至剪贴板，请直接到MidasMCT命令窗口粘贴执行！") 
		msg_box.exec_()

class infoTab(QtGui.QWidget):
	def __init__(self,parent=None):
		super(infoTab, self).__init__(parent)

		Label1 = QtGui.QLabel(u"选择钢束文件:")
		Label4 = QtGui.QLabel(u"选择主梁数据:")
		Label2 = QtGui.QLabel(u"输入起始编号:")
		Label3 = QtGui.QLabel(u"输入钢束属性:")
		
		self.LE1 = QtGui.QLineEdit()
		self.LE4 = QtGui.QLineEdit()
		self.LE2 = QtGui.QLineEdit()
		self.LE3 = QtGui.QLineEdit()

		self.LE1.setPlaceholderText(u"选择钢束文件")
		self.LE4.setPlaceholderText(u"选择主梁数据")
		self.LE2.setPlaceholderText(u"输入起始编号")
		self.LE3.setPlaceholderText(u"输入钢束属性")

		self.FB1 = QtGui.QPushButton(u"打开...")
		self.FB1.clicked.connect(self.getIGES)
		self.FB2 = QtGui.QPushButton(u"打开...")
		self.FB2.clicked.connect(self.getMCT)

		mctGenButton = QtGui.QPushButton(u"生成")
		mctGenButton.clicked.connect(self.mctGeneration)

		self.mctListBox = QtGui.QPlainTextEdit()
		self.mctListBox.setReadOnly(True)

		mainLayout = QtGui.QGridLayout()
		mainLayout.setColumnMinimumWidth(1, 250)
		mainLayout.addWidget(Label1,0,0)
		mainLayout.addWidget(Label4,1,0)
		mainLayout.addWidget(Label2,2,0)
		mainLayout.addWidget(Label3,3,0)
		mainLayout.addWidget(self.LE1,0,1)
		mainLayout.addWidget(self.LE4,1,1)
		mainLayout.addWidget(self.LE2,2,1,1,2)
		mainLayout.addWidget(self.LE3,3,1,1,2)

		mainLayout.addWidget(self.FB1,0,2)
		mainLayout.addWidget(self.FB2,1,2)

		mainLayout.addWidget(self.mctListBox,4,0,1,2)
		mainLayout.addWidget(mctGenButton,   4,2)
		self.setLayout(mainLayout)


		
if __name__ == '__main__':



	app = QtGui.QApplication(sys.argv)

	tabdialog = mainDialog()
	sys.exit(tabdialog.exec_())