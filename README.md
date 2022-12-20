<h1 align="center"> Zoom Automation  </h1> <br>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Script Structure](#script-structure)
- [How To Run](#how-to-run)
- [Issues](#issues)
- [Authors](#authors)


## Introduction

A python script that joins and record a scheduled zoom meeting. 

## Features

A few of the things you can do with Zoom automation:

* No third-party recording software
* Schedule the whole week
* Easy customization with .csv schedule format
* Runs on the backround 


## Getting Started

### Dependencies

* Python 3.5 and above

* Library requirements are stored in requirements.txt\


## Installation

* `git clone https://github.com/galudSla/zoom-automation.git`
* `cd to bill-split folder directory`
* `python -m venv <yourvenvname>`
* `activate virtualenvironment`
* `pip install -r requirements.txt`


## Script Structure

* Firstly open config.yml and edit the zoom absolute path and the name of your .csv schedule file (default schedule.csv). The script takes advantage of the information in the schedule.csv in order to plan the automation. Be careful to keep the format of the dates, time and the name of the day as it is presented in the cloned schedule.csv when entering the schedule information, otherwise you will bump into errors. 
* The script checks if today matches the day in the schedule and saves in a new dataframe the row that meet the condition. If there is no scheduled meeting for today the script is set to sleep until the day changes (23:59), then it checks the day again and get a new dataframe. 
* If there is a meeting planned for today the scipt will sleep until the start time of the meeting. The recording time is set to be the difference between the starting time and the ending time in the schedule.csv.
* The meeting id and password need to be scrapped from the zoom meeting URL.\
i.e 
```
https://zoom.us/j/99986686827?pwd=R0QxMTNDc2hKMi9QK24wVDcwMENLUT09#success 
ID: 99986686827
PASSWORD: R0QxMTNDc2hKMi9QK24wVDcwMENLUT09
```
* The label column typically stands for the name of the lessons, or gives some information about the meeting. Note that the label information is later going to be used in the name concatinated with the current date.
* The exports folder is the directory where all the exports are saved. Note that all the media test files are created in this directory, but they are deleted as long as the final.mp4 is renamed properly to the label plus the date.
* There are two module scipts, recordProccess.py and timeZoomFunctions.py. The first has the functions responsible for recording audio and video, merging them into one, multiproccessing and proper directory storing plus deleting temps. The second has the functions responsible for extracting information from the csv file and automating Zoom app.

## How To Run

* After configuring config.yml and updating info on schedule.csv run zoomAutomation.py only from the command line.


## Issues 

Sometimes the audio gets out of sync with the video in the final .mp4 file. It maybe has something to do with the multiproccessing architecture.


## Authors

@galudSla\
email: tedgiann@gmail.com

