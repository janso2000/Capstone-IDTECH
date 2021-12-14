import time
import stepperSetup
from time import sleep
import stepperSetupZ
#example code for a button press sequence
if __name__ == "__main__":
    startx=0
    starty=0
    
    motorzf = stepperSetupZ.motor(22, 23, 19, 20, 5, 6, 612)
    motorz = stepperSetup.motor(22, 23, 19, 20)
    motorx = stepperSetup.motor(4, 21, 12, 24)    
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
    
    