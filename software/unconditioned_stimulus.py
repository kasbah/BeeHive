"""Task to run a simple uncondiotioned stimulus protocol

In this protocol a session corresponds to several trials, where
a reward is presented at a specific location of the behavioural chamber
at specified intervals. To make things easier for users, this a reward can be 
paired with a cue, that will come at the onset of the reward. 
(This could be a click, a noise, a light, etc)"""


#import the necessary libraries
import serial
import machine
import time
import ringbuffer

class USProtocol:

    def __init__(self):
        """the __init__ function is used to define all timing 
        parameters of the task and other things that will be used throughout this protocol"""
        ##PINS/PORTS
        #here users should define what is connected to which physical pin of the behavioural system.
        #ie if a syringe pump is connected to pin IO26, this will be defined here
        self.houseLightPin  = 26
        self.syringePumpPin = 25
        self.cuePin     = 27
        self.lickSpoutPin   = 10
        self.headPortPin    = 11

        

        #now we need to tell the device what each pin is doing, are they inputs, are they outputs?
        #OUTPUTS
        #here the house light is an output, since it is connected to an LED in the physical world
        self.houseLight = machine.Pin(self.houseLightPin, machine.Pin.OUT)
        self.syringePump = machine.Pin(self.syringePumpPin, machine.Pin.OUT)
        self.cue = machine.Pin(self.cuePin, machine.Pin.OUT)

        #INPUTS
        self.lickSpout = machine.Pin(self.lickSpoutPin, machine.Pin.IN)
        self.headPort = machine.Pin(self.headPortPin, machine.Pin.IN)

        ##DURATIONS
        #inter trial interval duration in milliseconds
        self.itiDur = 1000
        #reward duration (for how long a syringe pump will be on, for instance)
        self.rewDur = 100
        # cue duration
        self.cueDur = 100 #should be as long or smaller than reward

        ## NUMBER OF TRIALS:
        self.trials = 50

        ##OPTIONS:
        #here define if a clicker or another cue should be used together with the reward
        # 0 means no cue
        # 1 means cue
        self.useCue = 1

        #####
        #here we define "backstage variables" things that will take care of recording data,
        #managing transmission to PC, etc.
        # in normal cases, users should not need to fiddle with this!
        bufferSize = 1000
        self.buffer1 = ringbuffer.Ringbuffer(bufferSize)
        self.buffer2 = ringbuffer.Ringbuffer(bufferSize)
        #needs to be finished - the idea here is that we fill buffer1 with data, when it gets full,
        #we transmit the data via serial or wireless, and in the meantime start filling buffer2.

    #next we are going to define the functions that compose our task:
    def ITI(self):
        """ITI is the inter trial interval, where house light is on, but nothing else happens.
        So we just need to count time and monitor lick spout and head port"""
        
        #turn on the house light
        self.houseLight.on

        startTiming = time.ticks_us()  # get microsecond counter
        stopTiming = time.ticks_us()  # get microsecond counter
        #the next for loop goes over "each millisecond of the interval", in it we measure time in microseconds and monitor ports
        for i in range(self.itiDur):
            #check the state of each port, both inputs and outputs and add to ring buffer
            #TODO
            while stopTiming - startTiming < 1000:
                stopTiming = time.ticks_us()
        
        #when leaving ITI turn house light off (if it needs to be on on the next phase, it should be turned on again there -
        # the transition between stages is too fast for any sort of flicker to be perceived)
        self.houseLight.off
        
        return
    
    def reward(self):
        """reward is the phase where the syringe pump is turned on. This can come together with a clicker or sound or led of some sort"""
        #turn on the house light
        self.houseLight.on

        startTiming = time.ticks_us()  # get microsecond counter
        stopTiming = time.ticks_us()  # get microsecond counter
        
        #turn syringe pump on
        self.syringePump.on
        #in case a clicker or other cue is wanted this can be done here
        if self.useCue == 1:
            self.cue.on
        
        #the next for loop goes over "each millisecond of the interval", in it we measure time in microseconds and monitor ports
        for i in range(self.rewDur):
            #in case a cue is being used and the duration of the cue is smaller than i, turn the cue off
            if self.useCue == 1 and self.cueDur<=i:
                self.cue.off
            #check the state of each port, both inputs and outputs and add to ring buffer
            #TODO
            while stopTiming - startTiming < 1000:
                stopTiming = time.ticks_us()

    def main(self):
        """main is a simple function where all phases of the task are going to be ordered and then finally we are going to set it to run"""
        # in this case, there is no conditional statement for the transition between ITI and reward. 
        #eventually tasks are going to have conditionals, ie, if there is no response when a certain cue comes, then the task needs to go to 
        #state1 instead of state2, etc.

        for i in range(self.trials):
            self.ITI()
            self.reward()

"""
TODO:
    - Create a header file that will be transmitted before the task starts, so that the data can be converted back and the user has
    a decent annotation of the experiment
    - create the ring buffer routines where the data is going to be stored and send periodically to the main computer
    - maybe createa file with stats on the session for quick checks?(optional add on)
"""

