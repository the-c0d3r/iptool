import sys, os, urllib, socket

from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("resources/ipgui.ui")[0]

class IP(QtGui.QMainWindow,form_class):

    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.txtlanip.setText("0.0.0.0")
        self.txtwanip.setText("0.0.0.0")
        self.btngetlanip.clicked.connect(self.getlanip)
        self.btngetwanip.clicked.connect(self.getwanip)
        self.statusbar.showMessage("Product of MSF (www.mmsecurity.net)")

        self.lblpic.setPixmap(QtGui.QPixmap(os.getcwd()+"resources/msf.png"))

        self.show()

    def getlanip(self):
        lanip = socket.gethostbyname(socket.gethostname())
        self.txtlanip.setText(lanip)
    
    def getwanip(self):
        try:
            wanip = urllib.urlopen("http://myip.dnsdynamic.org/").read()
        except:
            QtGui.QMessageBox.warning(self,"Error!","No Internet Access",buttons=QtGui.QMessageBox.Ok)
        else:
            self.txtwanip.setText(wanip)

def main():
    app = QtGui.QApplication(sys.argv)
    exe = IP()
    #exe.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
