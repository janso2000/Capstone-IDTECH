import time
import stepperSetup
#import time
from time import sleep
import stepperSetupZ
#import pigpio
if __name__ == "__main__":
    x=0
    #pi = pigpio.pi()
    startx=0
    starty=0
    motorzf = stepperSetupZ.motor(22, 23, 19, 20, 5, 6)
    motorz = stepperSetup.motor(22, 23, 19, 20)
    motorx = stepperSetup.motor(4, 21, 12, 24)
  # print("motor configured")        
    motory = stepperSetup.motor(26, 13, 16, 25)
    motorz.go(-200,70)
    motorzf.goTil(8000, -5, 100)
    motorz.go(-190,70)
    sleep(.01)

    motory.go(20,50)
    sleep(.01)
    motorx.go(35,70)
    
    motory = stepperSetup.motor(26, 13, 16, 25)
    motorz.go(-200,70)
    motorzf.goTil(8000, -5, 100)
    motorz.go(-190,70)

