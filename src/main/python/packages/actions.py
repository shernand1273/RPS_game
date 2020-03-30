from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import random

def startButtonClicked(obj):
    obj.feedback.clear()
    obj.timer.start()
    obj.gameStarted = True


def stopButtonClicked(obj):
    if(obj.gameStarted):
        obj.timer.stop()
        choices = {0:"Paper",1:"Scissors",2:"Rock"} 
        msg=""
        recenter = True
        userWins = False

        if(obj.computerChoice == obj.userChoice):
            msg = "Draw"
            recenter = False
        else:
            pc = obj.computerChoice
            us = obj.userChoice
        
            if(choices[pc]=="Rock" and choices[us]=="Scissors"):
                msg = "You Loose...{} beats {}".format("Rock","Scissors")
            elif(choices[pc]=="Scissors" and choices[us]=="Paper"):
                msg ="You Loose...{} beats {}".format("Scissors","Paper")
            elif(choices[pc]=="Paper" and choices[us]=="Rock"):
                msg = "You Loose...{} beats {}".format("Paper","Rock")
            else:
                msg = "You Win...{} beats {}".format(choices[us],choices[pc])
                userWins = True

    
        obj.feedback.setText(msg)
        obj.feedback.resize(len(msg)*10,30)

        if(recenter):
            obj.feedback.move(190,374)
        else:
            obj.feedback.move(295,374)
            obj.feedback.resize(len(msg)*20,30)
    
        if(userWins):
            obj.feedback.setStyleSheet("color:green")
        else:
            if(msg == "Draw"):
                obj.feedback.setStyleSheet("color:blue")
            else:
                obj.feedback.setStyleSheet("color:red")
                obj.feedback.move(175,374)
                

        #update the scores
        if(userWins):
            obj.userScore +=1
            tempString = str(obj.userScore)
            obj.usrScoreLabel.setText(tempString)
            obj.usrScoreLabel.resize(len(tempString)*20,20)
        elif(not(userWins) and msg == "Draw"):
            pass
        else:
            obj.computerScore +=1
            tempString = str(obj.computerScore)
            obj.cpuScoreLabel.setText(tempString)
            obj.cpuScoreLabel.resize(len(tempString)*20,20)

def resetClicked(obj,ctxt):
    obj.timer.stop();
    obj.feedback.clear()
    obj.usrScoreLabel.clear()
    obj.cpuScoreLabel.clear()
    obj.userScore = 0
    obj.computerScore = 0
    obj.gameStarted = False
    obj.userImage.setPixmap(QPixmap(ctxt.get_resource('images/rock.png')))
    obj.computerImage.setPixmap(QPixmap(ctxt.get_resource('images/rock.png')))


def closeClicked(obj):
    obj.close()

def minimizeClicked(obj):
    obj.showMinimized()

def maximizeClicked(obj):
    obj.show()



def timerActions(obj):
    #we are going to pick two random numbers here
    randOne = random.randint(0,2)
    randTwo = random.randint(0,2)
    computerPicture = obj.pictures[randOne]
    userPicture = obj.pictures[randTwo]
    obj.computerImage.setPixmap(QPixmap(computerPicture))
    obj.userImage.setPixmap(QPixmap(userPicture))
    obj.computerChoice = randOne
    obj.userChoice = randTwo




    