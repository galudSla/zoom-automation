import ray
import os 
import pyaudio
import wave
import time
from datetime import datetime
from screen_recorder_sdk import screen_recorder
from moviepy.editor import *
import random


def recordScreen(seconds):
    screen_recorder.enable_dev_log ()
    params = screen_recorder.RecorderParams ()
    screen_recorder.init_resources (params)
    screen_recorder.start_video_recording ('.\\exports\\test.mp4', 15, 8000000, True)
    time.sleep(seconds)
    screen_recorder.stop_video_recording ()
    with open('.\\exports\\test.mp4'):
        pass

def recordAudio(seconds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = seconds
    WAVE_OUTPUT_FILENAME = '.\\exports\\test.wav'

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording audio")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording audio")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def audioScreenRecordingMultiproccessing(zoomDuration):
    ray.init()
    duration = zoomDuration

    @ray.remote
    def audio():
        recordAudio(duration)
            
    @ray.remote
    def video():
        recordScreen(duration)

    ray.get([audio.remote(), video.remote()])

def mergeVideoAudio():
    videoclip = VideoFileClip('.\\exports\\test.mp4')
    audioclip = AudioFileClip('.\\exports\\test.wav')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile('.\\exports\\final.mp4')

def exportName(label):
    today = datetime.now()
    today = today.strftime("%d-%m-%Y")
    namePlusDate = label+'('+today+')'
    return namePlusDate

def extensionAdd(label):
    return label+'.mp4'

def tempDeletion():
    toDelete = ['.\\exports\\test.mp4', '.\\exports\\test.wav']
    for file in toDelete:
        os.remove(file)   

def renamingCleaning(label):
    label = exportName(label)
    newName = '.\\exports\\'+extensionAdd(label)
    oldName = '.\\exports\\final.mp4'
    os.rename(oldName, newName)
    print('Succesfully renamed {} to {}'.format('final.mp4', newName))


if __name__ == "__main__":
    audioScreenRecordingMultiproccessing(2)
    mergeVideoAudio()
    testName = 'test'+str(random.randrange(10000))
    renamingCleaning(testName)
    tempDeletion()
