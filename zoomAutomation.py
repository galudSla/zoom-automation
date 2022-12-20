import time
import pandas as pd
import src.timeZoomFunctions as tzf
import src.recordProcess as recordProcess


zoomPath = tzf.configPath('zoom', 'path')
csvName = tzf.configPath('csv', 'name')

tzf.startZoom(zoomPath)
df = pd.read_csv(csvName, sep=';')

while True:
    daysToCheck = df.loc[df['day'] == tzf.dayName()]
    daysToCheck = daysToCheck.sort_values('start', ascending=False)

    for index, row in daysToCheck.iterrows():
        print(tzf.timeNow())

        if tzf.timeNow() == row['start']:
            print('Time for {}'.format(row['label']))      
            tzf.startZoom(zoomPath)
            tzf.joinMeeting()
            tzf.meetingID(row['id'])
            tzf.meetingPswd(row['pswd'])
            
            recordingTime = tzf.recordingTime(row)
            lessonLabel = row['label']
            lessonLabel = recordProcess.exportName(lessonLabel)
            recordProcess.audioScreenRecordingMultiproccessing(recordingTime)
            recordProcess.mergeVideoAudio()
            recordProcess.renamingCleaning(lessonLabel)
            recordProcess.tempDeletion()
           
        else:
            wait = tzf.waitTime(row['start'])
            print('Next lesson is in {} minutes'.format(int(wait/60)))
            time.sleep(wait)

