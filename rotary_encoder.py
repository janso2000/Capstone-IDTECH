#!/usr/bin/env python

import pigpio

class decoder:

   """Class to decode mechanical rotary encoder pulses."""

   def __init__(self, pi, gpioA, gpioB, callback):

      self.pi = pi
      self.gpioA = gpioA
      self.gpioB = gpioB
      self.callback = callback

      self.levA = 0
      self.levB = 0
      self.pos = 0

      self.lastGpio = None

      self.pi.set_mode(gpioA, pigpio.INPUT)
      self.pi.set_mode(gpioB, pigpio.INPUT)

      self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
      self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

      self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
      self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)

   def _pulse(self, gpio, level, tick):

      """
      Decode the rotary encoder pulse.

                   +---------+         +---------+      0
                   |         |         |         |
         A         |         |         |         |
                   |         |         |         |
         +---------+         +---------+         +----- 1

             +---------+         +---------+            0
             |         |         |         |
         B   |         |         |         |
             |         |         |         |
         ----+         +---------+         +---------+  1
      """

      if gpio == self.gpioA:
         self.levA = level
      else:
         self.levB = level;

      if gpio != self.lastGpio: # debounce
         self.lastGpio = gpio

         if   gpio == self.gpioA and level == 1:
            if self.levB == 1:
               self.callback(1)
         elif gpio == self.gpioB and level == 1:
            if self.levA == 1:
               self.callback(-1)
   def value(self):
       return self.pos
   def setValue(self, set_Value):
       self.pos = set_Value
   def cancel(self):

      """
      Cancel the rotary encoder decoder.
      """

      self.cbA.cancel()
      self.cbB.cancel()
#Example Code
if __name__ == "__main__":

   import time
   import pigpio
   import rotary_encoder
   print("Program started")
   pos=0
   
   def callback(way):
     # print("callback started")
      global pos
      pos += way
      decoderx.setValue(pos)
      print("pos={}".format(decoderx.value()))
      
   #print("callback skipped")
   pi = pigpio.pi()
   #print("pi set")
   decoderx = rotary_encoder.decoder(pi, 3, 2, callback)
   #print("after decoder pos={}".format(pos))
   time.sleep(300)
   #print("after sleep")
   decoderx.cancel()
   pi.stop()
