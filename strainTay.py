#! /usr/bin/python2

import time
import sys

class strain:
    def __init__(self, hx1, hx2, hx3):  
        self.hx1 =hx1
        self.hx2 =hx2
        self.hx3 =hx3
    def setUp(self):
        referenceUnit = 5.67
        EMULATE_HX711=False
        if not EMULATE_HX711:
            import RPi.GPIO as GPIO
            from hx711 import HX711
            
        else:
            from emulated_hx711 import HX711
        #hx = HX711(27, 17, 128)
        hx = HX711(self.hx1, self.hx2, self.hx3)
        self.hx = hx
        hx.set_reading_format("MSB", "MSB")
        hx.set_reference_unit(referenceUnit)
        hx.reset()
        hx.tare()
        print("Tare done! Add weight now...")
        

    def getVal(self):   
        val = self.hx.get_weight(3)
        print(val,"g")
        #self.hx.power_down()
        #self.hx.power_up()
        #time.sleep(0.0001)
        return val
        
if __name__ == "__main__":
    
    import strainTay
    strainx=strain(5, 6, 128)
    strainx.setUp()
    while True:
        strainx.getVal()
    cleanAndExit()
