#######################################################################
# This class works on the logic and functionality of the music player
# that plays audio tracks within the cli-audio program. 
#
# @author Hai Duong, Theodore Lang, Trung-Vuong Pham
# @date November 18, 2018
#######################################################################

"""PyAudio Example: Play a wave file (callback version)."""

# imports needed for function
import pyaudio
import wave
import time
import os
from excepts.CLI_Audio_Exception import CLI_Audio_File_Exception

class Player:

    # constructor method 
    def __init__(self):
        self.currentSong = "Nothing playing."
        self.paused = True
        self.position = 0

    # getter method for the current song
    def getCurrentSong(self):
        return self.currentSong

    # method to pause a song that is playing
    def pause(self):
        if self.paused == False:
            self.paused = True
            self.stream.stop_stream()
        else:
            self.paused = False
            self.stream.start_stream()
    
    # method to play a song 
    def play(self, track):
        self.paused = False
        
        song = os.path.isfile(track)
        if not song: # if a file is not a song
            raise CLI_Audio_File_Exception
            
        self.currentSong = track
            
        self.wf = wave.open(track, 'rb')

        # instantiate PyAudio (1)
        self.p = pyaudio.PyAudio()

        # open self.stream using callback (3)
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                channels=self.wf.getnchannels(),
                rate=self.wf.getframerate(),
                output=True,
                stream_callback=self.callback)

        # start the self.stream (4)
        self.stream.start_stream()

    # method to stop the track from playing
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()

        self.p.terminate() 
    
    # method for callbacks
    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
