def listensinush(freq, harmo):
#  sinus function at freq(Hz) frequency, and harmo harmonics
   s = Server().boot()
   for i in range (1,harmo+1):
      s.start()
      a = Sine(i*freq, mul=1, add=0).out()
      time.sleep(1)
      s.stop() 