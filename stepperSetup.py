#import rotary_encoder
import time
import pigpio
import rotary_encoder
from time import sleep
import RPi.GPIO as GPIO
# *****************************************************************************?
class motor:
    def __init__(self, pinDir, pi, pinStep, gpioA, gpioB):  
        self.pinDir = pinDir
        self.pinStep = pinStep
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pi = pi
        self.pos =0
        self.delay=0
        self.mm=0
        def callback(way):
            print("callback started")
            self.pos += way
            self.encoder.setValue(self.pos)
            print("pos={}".format(self.encoder.value()))
            self.mm = self.encoder.value()*.32515
            print("pos={}".format(self.mm))
        self.encoder = rotary_encoder.decoder(self.pi, gpioA, gpioB, callback) 
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinDir,GPIO.OUT) # direction
        GPIO.setup(pinStep,GPIO.OUT) # step
        
    
    def go(self, target, setSpeed): #note 200 steps per rev for the motor
        #0 speed will set delay to .01
        #100 speed will set delay to .000001
        speed =(.000001 + ((100-setSpeed)*.00009999))
        self.target=int(target*3.0755) 
        self.delay = speed
        while(self.encoder.value() != self.target):
            #stop, reached goal
            if(self.encoder.value()> self.target):
                #too far! go backwards
                GPIO.output(self.pinDir, GPIO.LOW)
            if(self.encoder.value()< self.target):
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
   #dirx=17
   #stepx=27
   #encoderCHA = 6
   #encoderCHB = 13
   x=0
   pi = pigpio.pi()
   motorx = stepperSetup.motor(27, pi, 17, 6, 13)
   motory = stepperSetup.motor(10, pi, 22, 19, 26)
	#all you need to do is use .go(encoder_position, speed)
   #speed needs to be between 0-100
   while(x<5):
      # motorx.go(25.4,70)
       motorx.go(25.4,70)
      #motorx.go(-25.4,70)
       sleep(2)
       motorx.go(-25.4,70)
       x=x+1 
