import time
import pigpio
import rotary_encoder
from time import sleep
import RPi.GPIO as GPIO
# *****************************************************************************
class motor:
    def __init__(self, pinDir, pinStep, gpioA, gpioB):  
        self.pinDir = pinDir
        self.pinStep = pinStep
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pos =0
        self.delay=0
        self.mm=0
        self.pi = pigpio.pi()
        def callback(way):
            #this is the call back function that keeps a continuous encoder position update, even when the encoder is not explicitly called
            self.pos += way
            self.encoder.setValue(self.pos)
            print("pos={}".format(self.encoder.value()))
            self.mm = self.encoder.value()*.32515
            print("mm={}".format(self.mm)) 
        self.encoder = rotary_encoder.decoder(self.pi, gpioA, gpioB, callback) 
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinDir,GPIO.OUT) # sets up direction pin
        GPIO.setup(pinStep,GPIO.OUT) # sets up step pin
        
    
    def go(self, target, setSpeed): #note 200 steps per rev for the motor
        #0 speed will set delay to .01
        #100 speed will set delay to .000001
        speed =(.000001 + ((100-setSpeed)*.00009999))
        self.target=int(target*3.0755) #this converts the mm target entered into encoder steps
        self.delay = speed
        while(self.encoder.value() != self.target):
            #stop, reached goal
            if(self.encoder.value()> self.target):
                #too far! go backwards
                GPIO.output(self.pinDir, GPIO.LOW)
            if(self.encoder.value()< self.target):
                #not far enough! keep going forward
                GPIO.output(self.pinDir, GPIO.HIGH)
            #pulsing code, speed is dictated by wait between pulses
            GPIO.output(self.pinStep, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.pinStep, GPIO.LOW)
            sleep(self.delay)

  #example code 
if __name__ == "__main__":
 
   #the following is needed for all motors
   import time
   import stepperSetup
   #the following is needed for each individual motor set up
   #Where (dir, step, GpioA, GPioB)
   motorx = stepperSetup.motor(4, 21, 12, 24)       
   motory = stepperSetup.motor(26, 13, 25, 16)
   motorz = stepperSetup.motor(22, 23, 19, 20)
   
   #all you need to do is use .go(desired mm position, speed)
   #speed needs to be between 0-100
 
   motorz.go(-150,70)
   sleep(.01) #for any concequtive motor movements referncing the same motor shoudl have a small wait to prevent polling errors
   motorz.go(-100,70)
   motorx.go(-40, 70)
   motory.go(-30,70)
   motorx.go(35,70)
   motory.go(20,70)
 