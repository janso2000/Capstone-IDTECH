#import rotary_encoder
import time
import pigpio
import rotary_encoderZ
import strainTay
from time import sleep
import RPi.GPIO as GPIO
# *****************************************************************************?
class motor:
    def __init__(self, pinDir, pinStep, gpioA, gpioB, sig1, sig2):  
        self.pinDir = pinDir
        self.pinStep = pinStep
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pi = pigpio.pi()
        self.pos =0
        self.delay=0
        self.mm=0
        self.strainx=strainTay.strain(sig1, sig2, 128)
        self.strainx.setUp() 
       # self.strainVal = 0
        
        #self.encoder = rotary_encoderZ.decoder(self.pi, gpioA, gpioB, callback) 
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinDir,GPIO.OUT) # direction
        GPIO.setup(pinStep,GPIO.OUT) # step
        
    
    def goTil(self, force, target, setSpeed): #note 200 steps per rev for the motor
        #0 speed will set delay to .01
        #100 speed will set delay to .000001
        speed =(.000001 + ((100-setSpeed)*.00009999))
        self.force=force#int(target*3.0755)
        self.target= target#int(target*3.0755)
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
	#the following is needed for each individual motor set up
   #dirx=17
   #stepx=27
   #encoderCHA = 6
   #encoderCHB = 13
   x=0
   #motorx = stepperSetupZ.motor(4, pi, 21, 12, 24, 27, 17)
  # print("motor configured")        
   #motory = stepperSetup.motor(26, pi, 13, 16, 25)
   motorz = stepperSetupZ.motor(22, 23, 19, 20, 5, 6)

	#all you need to do is use .go(encoder_position, speed)
   #speed needs to be between 0-100
  
      # motorx.go(25.4,70)
   motorz.goTil(30000, -5, 100)
   #motory.go(-50,70)

   print("motor moved")  
      #motorx.go(-25.4,70)
       #sleep(2)
       #motorx.go(-25.4,70)
      # x=x+1 
