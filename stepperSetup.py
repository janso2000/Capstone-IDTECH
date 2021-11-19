#import rotary_encoder
import time
import pigpio

# *****************************************************************************?
class motor:
    def __init__(self, pinDir, pinStep, pi, gpioA, gpioB, callback):  
        self.pinDir = pinDir
        self.pinStep = pinStep
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pi = pi
        self.callback = callback
        encoder = decoder() ##???
        encoder.__init__(pi, gpioA, gpioB, callback) #???
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.CCW = GPIO.output(self.pinDir, GPIO.LOW)
        self.CW = GPIO.output(self.pinDir, GPIO.HIGH)
        GPIO.setup(pinDir,GPIO.OUT) # direction
        GPIO.setup(pinStep,GPIO.OUT) # step
        
    def go(self, target, speed):
        self.speed = speed 
        while(encoder.value()!= target)
            #stop, reached goal
            if(encoder.value()> target)
                #too far! go backwards
                self.CCW
            if(encoder.value()< target)
                #not far enough! keep going
                self.CW
            GPIO.output(pinStep, GPIO.HIGH)
            sleep(delay)
            GPIO.output(pinStep, GPIO.LOW)
            sleep(delay)
     

	 ##stop???           
