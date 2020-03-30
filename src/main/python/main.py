from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QEvent
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from packages import actions


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        #basic setup for the window
        self.setGeometry(200,100,650,500)
        self.setFixedSize(650,500)
        self.setWindowTitle("Rock Paper Scissors")
        self.setWindowFlag(Qt.FramelessWindowHint)
        #set the style for this window
        appStyle = None
        with open(appctxt.get_resource('style/main.css'),'r')as r_file:
            appStyle = r_file.read()

        self.setStyleSheet(appStyle)
       
        self.UI()

    def UI(self):
        #game variables
        self.userScore = 0
        self.computerScore = 0
        self.computerChoice=None
        self.userChoice=None
        #controls and ui fields
        self.pictures = [appctxt.get_resource('images/paper.png'),appctxt.get_resource('images/scissors.png'),appctxt.get_resource('images/rock.png')]
        self.gameStarted = False
        self.computerScoreLabel = QLabel("Computer",self)
        self.computerScoreLabel.setObjectName('computerLabel')
        self.userScoreLabel = QLabel("You",self)
        self.userScoreLabel.setObjectName('userLabel')
        self.feedback = QLabel(self)
        self.feedback.setObjectName('feedbackLabel')
        self.cpuScoreLabel = QLabel(self)
        self.usrScoreLabel = QLabel(self)
        self.cpuScoreLabel.setObjectName("computerScore")
        self.usrScoreLabel.setObjectName("userScore")
        #buttons
        self.startButton = QPushButton(self)
        self.startButton.setText("Start")
        self.startButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.stopButton = QPushButton(self)
        self.stopButton.setText("Stop")
        self.stopButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.resetButton= QPushButton(self)
        self.resetButton.setText("Reset")
        self.resetButton.setCursor(QtCore.Qt.PointingHandCursor)

        #customTitleBar
        self.minimize = QPushButton(self)
        # self.maximize = QPushButton(self)
        self.closeWindow = QPushButton(self)
        self.minimize.setText("_")
        # self.maximize.setText("+")
        self.closeWindow.setText("X")
        self.closeWindow.move(598,0)
        # self.maximize.move(540,0)
        self.minimize.move(545,0)
        self.closeWindow.setObjectName('cls')
        # self.maximize.setObjectName('max')
        self.minimize.setObjectName('min')
        self.minimize.setCursor(QtCore.Qt.PointingHandCursor)
        # self.maximize.setCursor(QtCore.Qt.PointingHandCursor)
        self.closeWindow.setCursor(QtCore.Qt.PointingHandCursor)
        

        #timer
        self.timer = QTimer(self)
        self.timer.setInterval(200)
        #images (3 images total)
        self.computerImage = QLabel(self)
        self.computerImage.setPixmap(QPixmap(appctxt.get_resource('images/rock.png')))
        self.computerImage.move(20,120)
        self.userImage = QLabel(self)
        self.userImage.setPixmap(QPixmap(appctxt.get_resource('images/rock.png')))
        self.userImage.move(380,120)
        self.vsImage = QLabel(self)
        self.vsImage.setPixmap(QPixmap(appctxt.get_resource('images/vs.png')))
        self.vsImage.move(250,170)
        #layout
        self.computerScoreLabel.move(90,70)
        self.cpuScoreLabel.move(140,100)
        self.userScoreLabel.move(485,70)
        self.usrScoreLabel.move(500,100)
        self.startButton.move(175,430)
        self.stopButton.move(280,430)  
        self.resetButton.move(375,430)
        #actions
        self.startButton.clicked.connect(lambda : actions.startButtonClicked(self)) 
        self.stopButton.clicked.connect(lambda : actions.stopButtonClicked(self))
        self.timer.timeout.connect(lambda: actions.timerActions(self))
        self.resetButton.clicked.connect(lambda: actions.resetClicked(self,appctxt))
        self.minimize.clicked.connect(lambda: actions.minimizeClicked(self))
        # self.maximize.clicked.connect(lambda: actions.maximizeClicked(self))
        self.closeWindow.clicked.connect(lambda: actions.closeClicked(self))
        self.installEventFilter(self)
        
        #display
        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.oldPos = event.globalPos()
        elif event.type() == QtCore.QEvent.MouseMove:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        return QtGui.QWindow.eventFilter(self,obj,event)
        
        

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Window()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)