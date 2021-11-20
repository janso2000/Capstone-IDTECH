#import rotary_encoder
import time
import pigpio
import rotary_encoder
from time import sleep
import RPi.GPIO as GPIO
# *****************************************************************************?
class motor:
    def __init__(self, pinDir, pinStep, gpioA, gpioB):  
        self.pinDir = pinDir
        self.pinStep = pinStep
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pi = pigpio.pi()
        self.pos =0
        self.delay=0
        def callback(way):
            # print("callback started")
            self.pos += way
            self.encoder.setValue(self.pos)
            print("pos={}".format(self.encoder.value()))    
        self.encoder = rotary_encoder.decoder(self.pi, gpioA, gpioB, callback) 
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinDir,GPIO.OUT) # direction
        GPIO.setup(pinStep,GPIO.OUT) # step
        
    
    def go(self, target, setSpeed): #note 200 steps per rev for the motor
        #0 speed will set delay to .01
        #100 speed will set delay to .000001
        speed =(.000001 + ((100-setSpeed)*.00009999))
        
        self.delay = speed
        while(self.encoder.value() != target):
            #stop, reached goal
            if(self.encoder.value()> target):
                #too far! go backwards
                GPIO.output(self.pinDir, GPIO.LOW)
            if(self.encoder.value()< target):
                #not far enough! keep going
                GPIO.output(self.pinDir, GPIO.HIGH)
            GPIO.output(self.pinStep, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.pinStep, GPIO.LOW)
            sleep(self.delay)
    
if __name__ == "__main__":

   #example code
	#the following is needed for all motors
   import time
   import stepperSetup
	#the following is needed for each individual motor set up
   dirx=27
   stepx=17
   encoderCHA = 4
   encoderCHB = 14
   motorx = stepperSetup.motor(dirx, stepx, encoderCHA, encoderCHB)
	#all you need to do is use .go(encoder_position, speed)
   #speed needs to be between 0-100
   motorx.go(10,20)
