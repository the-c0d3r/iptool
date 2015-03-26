import sys, os, urllib, socket 
import fcntl, struct
#import webbrowser

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

        #self.lblpic.setPixmap(QtGui.QPixmap(os.getcwd()+"/resources/msf.png"))
        #self.lblpic.mousePressEvent = self.openBrowser()
        self.show()

    def getlanip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ifname = 'wlan0'
        lanip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24])
        self.txtlanip.setText(lanip)

    def getwanip(self):
        try:
            wanip = urllib.urlopen("http://myip.dnsdynamic.org/").read()
        except:
            QtGui.QMessageBox.warning(self,"Error!","No Internet Access",buttons=QtGui.QMessageBox.Ok)
        else:
            self.txtwanip.setText(wanip)

    # def openBrowser(self):
    #     browser = webbrowser.WindowsDefault()
    #     browser.open_new("http://www.mmsecurity.net/forum")

def main():
    app = QtGui.QApplication(sys.argv)
    exe = IP()
    #exe.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
