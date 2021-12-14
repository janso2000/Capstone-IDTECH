import time
import pigpio
import rotary_encoderZ
import strainTay
from time import sleep
import RPi.GPIO as GPIO
# *****************************************************************************
#This is the force feedback command
class motor:
    def __init__(self, pinDir, pinStep, gpioA, gpioB, sig1, sig2, refNum):  
        self.pinDir = pinDir
        self.pinStep = pinStep
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pi = pigpio.pi()
        self.pos =0
        self.delay=0
        self.mm=0
        self.refNum= refNum
        self.strainx=strainTay.strain(sig1, sig2, 128, self.refNum) #this 128 number is the resolution
        self.strainx.setUp() 
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinDir,GPIO.OUT) # direction
        GPIO.setup(pinStep,GPIO.OUT) # step
        
    
    def goTil(self, force, setSpeed): #note 200 steps per rev for the motor
        #0 speed will set delay to .01
        #100 speed will set delay to .000001
        speed =(.000001 + ((100-setSpeed)*.00009999))
        self.force=force       
        self.delay = speed
        GPIO.output(self.pinDir, GPIO.LOW)
        while(self.strainx.getVal()< self.force):
            GPIO.output(self.pinStep, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.pinStep, GPIO.LOW)
            sleep(self.delay)
            print("pulsed")            
     
if __name__ == "__main__":
   #example code
	#the following is needed for all motors
   import time
   import stepperSetupZ
   import stepperSetup
	#the following is needed for each individual motor set up
   #Where (dir, step, GpioA, GPioB, strain gauge sig1, sig2,refNum))
   motorzf = stepperSetupZ.motor(22, 23, 19, 20, 5, 6, 612)
   motorz = stepperSetup.motor(22, 23, 19, 20)

	#all you need to do is use .go(encoder_position, speed)
   #speed needs to be between 0-100

   motorz.go(-160,70)
   sleep(1)
   motorzf.goTil(105, 100)
   sleep(1)
   motorz.go(-100,80)