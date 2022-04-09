def tracesinush(freq, harmo):
#  sinus function at freq(Hz) frequency, and harmo harmonics
   t = np.arange(0., 0.005, 1/(30*harmo*freq))
   plt.figure(figsize = (harmo+4, harmo+2))
   for i in range (1,harmo+1):
      nbr = 330+i
      plt.subplot(nbr)
      plt.plot(t,np.sin(2*pi*i*freq*t))
      label1 = "fonction sinus, fréquence " 
      label2 = str(i*freq) 
      label3 = "Hz"
      label = label1 + label2 + label3 
      myText = plt.title(label, size = 'x-small')
      fontsize = 8
      plt.title(label)
   plt.show()   
   plt.figure(figsize = (8, 6))
   for i in range (1,harmo+1):
      plt.plot(t,np.sin(2*pi*i*freq*t))
   label1 = "fonction sinus, fréquences " 
   label =''
   for i in range (1,harmo+1):
      label2 = str(i*freq) 
      label3 = "Hz "
      label = label + label2 + label3 
   label = label1 + label
   plt.title(label)
   plt.show() 