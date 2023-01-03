import math
import random
import time
import tkinter as tk
import wave
from threading import Thread
import pyaudio
from PIL import Image, ImageTk
from pydub import AudioSegment

#starting off-----------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title('Music Interaction')
root.maxsize(700, 1000)
root.config(bg='lightblue')

#setting up the audio---------------------------------------------------------------------------------------------------
wav = wave.open('xylo1.wav')
p = pyaudio.PyAudio()
correctSpeed = wav.getframerate()
wav.close()


#playing everything_______________________________________________________
def playS():
    Thread(target=drum).start()
    Thread(target=guitar).start()
    Thread(target=piano).start()
    Thread(target=orch).start()
    Thread(target=xylo).start()
    Thread(target=flute).start()

#defining faster, slower, louder, and softer_______________________________________________________


def faster():
    global correctSpeed
    if correctSpeed < 54000:
        correctSpeed = math.floor(correctSpeed * 1.05)
    else:
        correctSpeed = correctSpeed * 1


def slower():
    global correctSpeed
    if correctSpeed > 24000:
        correctSpeed = math.floor(correctSpeed / 1.1)
    else:
        correctSpeed = correctSpeed * 1


def louder():
    loudDrum()
    loudGuitar()
    loudPiano()
    loudOrch()
    loudXylo()
    loudFlute()


def softer():
    quietDrum()
    quietGuitar()
    quietPiano()
    quietOrch()
    quietXylo()
    quietFlute()

#functions for each instrument------------------------------------------------------------------------------------------


drumChoice = 'drum1.wav'
guitarChoice = 'guitar1.wav'
pianoChoice = 'piano1.wav'
orchChoice = 'orch1.wav'
xyloChoice = 'xylo1.wav'
fluteChoice = 'flute1.wav'

def newDrum():
    choices = ['drum1.wav', 'drum2.wav', 'drum3.wav', 'drum4.wav', 'drum5.wav']
    global drumChoice
    drumChoice = random.choice(choices)


def drum():
    global drumChoice
    w = wave.open(drumChoice)
    py = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = w.readframes(frame_count)
        return data, pyaudio.paContinue
    stream = py.open(format=py.get_format_from_width(w.getsampwidth()), channels=w.getnchannels(), rate=correctSpeed, output=True, stream_callback=callback)
    time.sleep(math.floor(w.getnframes()/correctSpeed) - 1)
    py.close(stream)
    w.close()


def newGuitar():
    choices = ['guitar1.wav', 'guitar2.wav', 'guitar3.wav', 'guitar4.wav', 'guitar5.wav']
    global guitarChoice
    guitarChoice = random.choice(choices)


def guitar():
    global guitarChoice
    w = wave.open(guitarChoice)
    py = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = w.readframes(frame_count)
        return data, pyaudio.paContinue
    stream = py.open(format=py.get_format_from_width(w.getsampwidth()), channels=w.getnchannels(), rate=correctSpeed, output=True, stream_callback=callback)
    time.sleep(math.floor(w.getnframes()/correctSpeed) - 1)
    py.close(stream)
    w.close()


def newPiano():
    choices = ['piano1.wav', 'piano2.wav', 'piano3.wav', 'piano4.wav', 'piano5.wav']
    global pianoChoice
    pianoChoice = random.choice(choices)


def piano():
    global pianoChoice
    w = wave.open(pianoChoice)
    py = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = w.readframes(frame_count)
        return data, pyaudio.paContinue
    stream = py.open(format=py.get_format_from_width(w.getsampwidth()), channels=w.getnchannels(), rate=correctSpeed, output=True, stream_callback=callback)
    time.sleep(math.floor(w.getnframes()/correctSpeed) - 1)
    py.close(stream)
    w.close()


def newOrch():
    choices = ['orch1.wav', 'orch2.wav', 'orch3.wav', 'orch4.wav', 'orch5.wav']
    global orchChoice
    orchChoice = random.choice(choices)


def orch():
    global orchChoice
    w = wave.open(orchChoice)
    py = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = w.readframes(frame_count)
        return data, pyaudio.paContinue
    stream = py.open(format=py.get_format_from_width(w.getsampwidth()), channels=w.getnchannels(), rate=correctSpeed, output=True, stream_callback=callback)
    time.sleep(math.floor(w.getnframes()/correctSpeed) - 1)
    py.close(stream)
    w.close()


def newXylo():
    choices = ['xylo1.wav', 'xylo2.wav', 'xylo3.wav', 'xylo4.wav', 'xylo5.wav']
    global xyloChoice
    xyloChoice = random.choice(choices)


def xylo():
    global xyloChoice
    w = wave.open(xyloChoice)
    py = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = w.readframes(frame_count)
        return data, pyaudio.paContinue
    stream = py.open(format=py.get_format_from_width(w.getsampwidth()), channels=w.getnchannels(), rate=correctSpeed, output=True, stream_callback=callback)
    time.sleep(math.floor(w.getnframes()/correctSpeed) - 1)
    py.close(stream)
    w.close()


def newFlute():
    choices = ['flute1.wav', 'flute2.wav', 'flute3.wav', 'flute4.wav', 'flute5.wav']
    global fluteChoice
    fluteChoice = random.choice(choices)


def flute():
    global fluteChoice
    w = wave.open(fluteChoice)
    py = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = w.readframes(frame_count)
        return data, pyaudio.paContinue
    stream = py.open(format=py.get_format_from_width(w.getsampwidth()), channels=w.getnchannels(), rate=correctSpeed, output=True, stream_callback=callback)
    time.sleep(math.floor(w.getnframes()/correctSpeed) - 1)
    py.close(stream)
    w.close()

#volumes for instruments------------------------------------------------------------------------------------------------


vol1 = AudioSegment.from_wav('drum1.wav')
drumLevel = 0
vol2 = AudioSegment.from_wav('guitar1.wav')
guitarLevel = 0
vol3 = AudioSegment.from_wav('piano1.wav')
pianoLevel = 0
vol4 = AudioSegment.from_wav('orch1.wav')
orchLevel = 0
vol5 = AudioSegment.from_wav('xylo1.wav')
xyloLevel = 0
vol6 = AudioSegment.from_wav('flute1.wav')
fluteLevel = 0


def quietDrum():
    global drumChoice
    global vol1
    global drumLevel
    vol1 = AudioSegment.from_wav(drumChoice)
    if drumLevel > -21:
        vol1 = vol1 - 10
        drumLevel = drumLevel - 10
    else:
        vol1 = vol1 * 1

    drumChoice = vol1.export('drumvol.wav', format='wav').name


def loudDrum():
    global drumChoice
    global vol1
    global drumLevel
    vol1 = AudioSegment.from_wav(drumChoice)
    if drumLevel < 11:
        vol1 = vol1 + 5
        drumLevel = drumLevel + 5
    else:
        vol1 = vol1 * 1

    drumChoice = vol1.export('drumvol.wav', format='wav').name


def quietGuitar():
    global guitarChoice
    global vol2
    global guitarLevel
    vol2 = AudioSegment.from_wav(guitarChoice)
    if guitarLevel > -21:
        vol2 = vol2 - 10
        guitarLevel = guitarLevel - 10
    else:
        vol2 = vol2 * 1

    guitarChoice = vol2.export('guitarvol.wav', format='wav').name


def loudGuitar():
    global guitarChoice
    global vol2
    global guitarLevel
    vol2 = AudioSegment.from_wav(guitarChoice)
    if guitarLevel < 11:
        vol2 = vol2 + 5
        guitarLevel = guitarLevel + 5
    else:
        vol2 = vol2 * 1

    guitarChoice = vol2.export('guitarvol.wav', format='wav').name


def quietPiano():
    global pianoChoice
    global vol3
    global pianoLevel
    vol3 = AudioSegment.from_wav(pianoChoice)
    if pianoLevel > -21:
        vol3 = vol3 - 10
        pianoLevel = pianoLevel - 10
    else:
        vol3 = vol3 * 1

    pianoChoice = vol3.export('pianovol.wav', format='wav').name


def loudPiano():
    global pianoChoice
    global vol3
    global pianoLevel
    vol3 = AudioSegment.from_wav(pianoChoice)
    if pianoLevel < 11:
        vol3 = vol3 + 5
        pianoLevel = pianoLevel + 5
    else:
        vol3 = vol3 * 1

    pianoChoice = vol3.export('pianovol.wav', format='wav').name


def quietOrch():
    global orchChoice
    global vol4
    global orchLevel
    vol4 = AudioSegment.from_wav(orchChoice)
    if orchLevel > -21:
        vol4 = vol4 - 10
        orchLevel = orchLevel - 10
    else:
        vol4 = vol4 * 1

    orchChoice = vol4.export('orchvol.wav', format='wav').name


def loudOrch():
    global orchChoice
    global vol4
    global orchLevel
    vol4 = AudioSegment.from_wav(orchChoice)
    if orchLevel < 11:
        vol4 = vol4 + 5
        orchLevel = orchLevel + 5
    else:
        vol4 = vol4 * 1

    orchChoice = vol4.export('orchvol.wav', format='wav').name


def quietXylo():
    global xyloChoice
    global vol5
    global xyloLevel
    vol5 = AudioSegment.from_wav(xyloChoice)
    if xyloLevel > -21:
        vol5 = vol5 - 10
        xyloLevel = xyloLevel - 10
    else:
        vol5 = vol5 * 1

    xyloChoice = vol5.export('xylovol.wav', format='wav').name


def loudXylo():
    global xyloChoice
    global vol5
    global xyloLevel
    vol5 = AudioSegment.from_wav(xyloChoice)
    if xyloLevel < 11:
        vol5 = vol5 + 5
        xyloLevel = xyloLevel + 5
    else:
        vol5 = vol5 * 1

    xyloChoice = vol5.export('xylovol.wav', format='wav').name


def quietFlute():
    global fluteChoice
    global vol6
    global fluteLevel
    vol6 = AudioSegment.from_wav(fluteChoice)
    if fluteLevel > -21:
        vol6 = vol6 - 10
        fluteLevel = fluteLevel - 10
    else:
        vol6 = vol6 * 1

    fluteChoice = vol6.export('flutevol.wav', format='wav').name


def loudFlute():
    global fluteChoice
    global vol6
    global fluteLevel
    vol6 = AudioSegment.from_wav(fluteChoice)
    if fluteLevel < 11:
        vol6 = vol6 + 5
        fluteLevel = fluteLevel + 5
    else:
        vol6 = vol6 * 1

    fluteChoice = vol6.export('flutevol.wav', format='wav').name


#title------------------------------------------------------------------------------------------------------------------
screen = tk.LabelFrame(root, width=300, height=700, bg='lightblue')
screen.grid(row=0, column=0, padx=50, pady=10)
tk.Label(screen, text='Adjust Each Instrument!\nPress Play to Hear\nThem All Together!',
         font=('Bubblegum Sans', 17), background='lightblue', foreground='black').grid(row=0, column=0, padx=5, pady=0)

#speed------------------------------------------------------------------------------------------------------------------
controls = tk.Frame(screen, width=100, height=500, bg='lightblue')
controls.grid(row=0, column=1, pady=0, padx=10)

upArrow = Image.open(r'C:\Users\nitya\Java Programs\IdeaProjects\Music Interaction Project\up.png')
up = upArrow.resize((60, 40))
upArrowReal = ImageTk.PhotoImage(up)
tk.Button(controls, text='faster', image=upArrowReal, background='white', foreground='black',
          font=('Times New Roman', 10), compound='top', command=faster).grid(row=0, column=1, pady=10)

downArrow = Image.open(r'C:\Users\nitya\Java Programs\IdeaProjects\Music Interaction Project\down.png')
down = downArrow.resize((60, 40))
downArrowReal = ImageTk.PhotoImage(down)
tk.Button(controls, text='slower', image=downArrowReal, background='white', foreground='black',
          font=('Times New Roman', 10), compound='bottom', command=slower).grid(row=1, column=1)

#volume-----------------------------------------------------------------------------------------------------------------
volume = tk.Frame(screen, width=100, height=500, bg='lightblue')
volume.grid(row=0, column=2, pady=0, padx=10)
    #using arrows from before
tk.Button(volume, text='louder', image=upArrowReal, background='white', foreground='black',
          font=('Times New Roman', 10), compound='top', command=louder).grid(row=0, column=1, pady=10)
tk.Button(volume, text='softer', image=downArrowReal, background='white', foreground='black',
          font=('Times New Roman', 10), compound='bottom', command=softer).grid(row=1, column=1)

#play button------------------------------------------------------------------------------------------------------------
play = tk.Frame(screen, width=100, height=500, bg='purple')
play.grid(row=0, column=3, padx=10)
playArrow = Image.open(r'C:\Users\nitya\Java Programs\IdeaProjects\Music Interaction Project\play.png')
playA = playArrow.resize((40, 40))
playArrowReal = ImageTk.PhotoImage(playA)
tk.Button(play, text='Play', image=playArrowReal, background='white', foreground='black',
          font=('Times New Roman', 18), compound='left', command=playS).grid(row=0, column=0)

#instrument buttons-----------------------------------------------------------------------------------------------------
instruments = tk.Frame(screen, width=100, height=500, bg='lightblue')
instruments.grid(row=1, column=0, padx=0, pady=0)

tk.Button(instruments, text='Drum', background='lightgreen', foreground='black',
          font=('Times New Roman', 15), width=8, height=3, command=drum).grid(row=0, column=0, pady=20)
tk.Button(instruments, text='Guitar', background='lightpink', foreground='black',
          font=('Times New Roman', 15), width=8, height=3, command=guitar).grid(row=2, column=0, pady=20)
tk.Button(instruments, text='Piano', background='purple', foreground='black',
          font=('Times New Roman', 15), width=8, height=3, command=piano).grid(row=4, column=0, pady=20)
tk.Button(instruments, text='Orchestra', background='red', foreground='black',
          font=('Times New Roman', 15), width=8, height=3, command=orch).grid(row=6, column=0, pady=20)
tk.Button(instruments, text='Xylophone', background='yellow', foreground='black',
          font=('Times New Roman', 15), width=8, height=3, command=xylo).grid(row=8, column=0, pady=20)
tk.Button(instruments, text='Flute', background='teal', foreground='black',
          font=('Times New Roman', 15), width=8, height=3, command=flute).grid(row=10, column=0, pady=20)

#volume for instruments-------------------------------------------------------------------------------------------------
involume = tk.Frame(screen, width=50, height=700, bg='lightblue')
involume.grid(row=1, column=1)
tk.Button(involume, text='louder', background='lightgreen', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=loudDrum).grid(row=0, column=0, pady=10)
tk.Button(involume, text='softer', background='lightgreen', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=quietDrum).grid(row=1, column=0, pady=10)
tk.Button(involume, text='louder', background='lightpink', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=loudGuitar).grid(row=2, column=0, pady=10)
tk.Button(involume, text='softer', background='lightpink', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=quietGuitar).grid(row=3, column=0, pady=10)
tk.Button(involume, text='louder', background='purple', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=loudPiano).grid(row=4, column=0, pady=10)
tk.Button(involume, text='softer', background='purple', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=quietPiano).grid(row=5, column=0, pady=10)
tk.Button(involume, text='louder', background='red', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=loudOrch).grid(row=6, column=0, pady=10)
tk.Button(involume, text='softer', background='red', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=quietOrch).grid(row=7, column=0, pady=10)
tk.Button(involume, text='louder', background='yellow', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=loudXylo).grid(row=8, column=0, pady=10)
tk.Button(involume, text='softer', background='yellow', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=quietXylo).grid(row=9, column=0, pady=10)
tk.Button(involume, text='louder', background='teal', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=loudFlute).grid(row=10, column=0, pady=10)
tk.Button(involume, text='softer', background='teal', foreground='black',
          font=('Times New Roman', 10), width=6, height=2, command=quietFlute).grid(row=11, column=0, pady=10)

#new phrase buttons-----------------------------------------------------------------------------------------------------
phrase = tk.Frame(screen, width=50, height=700, bg='lightblue')
phrase.grid(row=1, column=2)

tk.Button(phrase, text='New Phrase', background='lightgreen', foreground='black',
          font=('Times New Roman', 13), width=10, height=1, command=newDrum).grid(row=0, column=0, pady=45)
tk.Button(phrase, text='New Phrase', background='lightpink', foreground='black',
          font=('Times New Roman', 13), width=10, height=1, command=newGuitar).grid(row=4, column=0, pady=45)
tk.Button(phrase, text='New Phrase', background='purple', foreground='black',
          font=('Times New Roman', 13), width=10, height=1, command=newPiano).grid(row=8, column=0, pady=45)
tk.Button(phrase, text='New Phrase', background='red', foreground='black',
          font=('Times New Roman', 13), width=10, height=1, command=newOrch).grid(row=12, column=0, pady=45)
tk.Button(phrase, text='New Phrase', background='yellow', foreground='black',
          font=('Times New Roman', 13), width=10, height=1, command=newXylo).grid(row=16, column=0, pady=45)
tk.Button(phrase, text='New Phrase', background='teal', foreground='black',
          font=('Times New Roman', 13), width=10, height=1, command=newFlute).grid(row=20, column=0, pady=45)


root.mainloop()
