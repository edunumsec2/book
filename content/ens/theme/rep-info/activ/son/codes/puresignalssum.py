def puresignalssum(freq, harmo):
#  harmonic signals
   s = Server().boot()
   somme = 0
   for i in range (1,harmo+1):
      s.start()
      a = Sine(i*freq, mul=1, add=0).out()
      time.sleep(1)
#  graphic vizualisation       
      namesc = 'Signal '+str(i*freq)+' Hz'
      sc = Scope(a, 0.003, 0.2, wintitle=namesc) 
      namespeca = 'Spectre du signal '+str(i*freq)+' Hz'
      speca = Spectrum(a, size=4096, wintype=0, wintitle=namespeca)
      somme=somme+a
   speca.outsc = Scope(somme, 0.003, 0.2, wintitle='somme des signaux')
   speca = Spectrum(somme, size=4096, wintype=0, wintitle='spectre de la somme')
   somme.out
   s.gui(locals())