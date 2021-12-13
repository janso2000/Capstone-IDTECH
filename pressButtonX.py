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
    
    motorzf = stepperSetupZ.motor(22, 23, 19, 20, 5, 6, 612)
   # motorif = stepperSetupZ.motor(2?2, 2?3, 1?9, 2?0, 27, 17, 625)
    motorz = stepperSetup.motor(22, 23, 19, 20)
    motorx = stepperSetup.motor(4, 21, 12, 24)
  # print("motor configured")        
    motory = stepperSetup.motor(26, 13, 25, 16)
    
    motorx.go(178.5,70)
    motory.go(-53,70)
    
    motorz.go(-170,70)
    sleep(.01)
    motorzf.goTil(105, -5, 100)
    motorz.go(-150,80)
    
    x=178.5+40
    motorx.go(x,70)
    sleep(.01)
    motory.go(-31,70)
    
    sleep(.01)
    motorz.go(-195,70)
    sleep(.01)
    motorzf.goTil(105, -5, 100)
    motorz.go(-160,80)
    
    #sleep(.01)

    #motory.go(12,50)
    #sleep(.01)
    
    #motorz.go(-200,70)
    #motorzf.goTil(8000, -5, 100)
   # motorz.go(-190,70)

