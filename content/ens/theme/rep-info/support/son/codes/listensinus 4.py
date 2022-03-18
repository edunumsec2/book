def listensinus(freq):
#  sinus function at freq(Hz) frequency
   s = Server().boot()
   s.start()
   a = Sine(freq, mul=1, add=0).out()
   time.sleep(5)
   s.stop()