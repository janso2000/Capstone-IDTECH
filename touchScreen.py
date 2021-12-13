import time
import stepperSetup
#import time
from time import sleep
import stepperSetupZ
#import pigpio
if __name__ == "__main__":
    #x=0
    #pi = pigpio.pi()
    x=0
    y=0
    
    motorzf = stepperSetupZ.motor(22, 23, 19, 20, 5, 6, 612)
   # motorif = stepperSetupZ.motor(2?2, 2?3, 1?9, 2?0, 27, 17, 625)
    motorz = stepperSetup.motor(22, 23, 19, 20)
    motorx = stepperSetup.motor(4, 21, 12, 24)
  # print("motor configured")        
    motory = stepperSetup.motor(26, 13, 25, 16)
    
    #go to start
    x=225
    motorx.go(x,70)
    y=-90
    motory.go(y,70)
    
    #press start
    motorz.go(-185,70)
    sleep(.01)
    motorzf.goTil(35, -5, 100)
    motorz.go(-150,80)#38
    sleep(.01)
    
    #go to button #2
    x=x+80
    motorx.go(x,70)
    y=y+38
    motory.go(-44,70)#-44
    
    #press button #2
    motorz.go(-183,70)
    sleep(.01)
    motorzf.goTil(105, -5, 100)
    motorz.go(-150,80)#38
    sleep(.01)
    
    #go to approve
    
    y=y+24
    
    motory.go(y,70)
    
    #press approve
    motorz.go(-175,70)
    sleep(.01)
    motorzf.goTil(30, -5, 100)
    motorz.go(-150,80)#38
    sleep(.01)
    
    #go to start
    x=x-59
    motorx.go(x,70)
    y=y-61
    motory.go(y,70)
    
    #press approve
    motorz.go(-175,70)
    sleep(.01)
    motorzf.goTil(30, -5, 100)
    motorz.go(-150,80)#38
    sleep(.01)
    
    #tap to pay
    y=y+60
    motory.go(y,70)
    
    #go to home button
    y=y-53
    x=x+25
    motorx.go(x,70)
    motory.go(y,70)
    
    #press home
    motorz.go(-175,70)
    sleep(.01)
    motorzf.goTil(30, -5, 100)
    motorz.go(-150,80)#38
    sleep(.01)
    
    
    
    
    
    #sleep(.01)

    #motory.go(12,50)
    #sleep(.01)
    
    #motorz.go(-200,70)
    #motorzf.goTil(8000, -5, 100)
   # motorz.go(-190,70)


