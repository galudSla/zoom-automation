import pyautogui
import subprocess
import time
from datetime import datetime
import yaml


def configPath(which, what):
    with open('config.yml', 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg[which][what]


def dayName():
    today = datetime.now()
    return today.strftime('%A')


def timeNow():
    now = datetime.now().strftime('%H:%M')
    return now


def waitTime(rowToCheck):
    t1 = datetime.strptime(timeNow(), '%H:%M')
    t2 = datetime.strptime(rowToCheck, '%H:%M')
    difference = t2 - t1
    if difference.total_seconds() > 0:
        return difference.total_seconds()
    else:
        dayEnd = datetime.strptime('23:59', '%H:%M')
        difference = dayEnd - t1
        return difference.total_seconds()


def startZoom(zoomPath):
    try:      
        open = subprocess.Popen(zoomPath)
    except Exception as e:
        print('There was an error: '+str(e))


def joinMeeting():
    joinButton = pyautogui.locateCenterOnScreen('.\\img\\joinButton.png')
    pyautogui.moveTo(joinButton)
    pyautogui.click()
    time.sleep(3)


def meetingID(meetingid):
    pyautogui.write(str(meetingid))
    pyautogui.press('enter')
    time.sleep(3)


def meetingPswd(pswd):
    pyautogui.write(str(pswd))
    pyautogui.press('enter')
    time.sleep(3)


def recordingTime(rowToCheck):
    start = datetime.strptime(rowToCheck['start'], '%H:%M')
    end = datetime.strptime(rowToCheck['end'], '%H:%M')
    recordingTime = end - start
    return recordingTime.total_seconds()

if __name__ == "__main__":
    pass
