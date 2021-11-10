def tracesinus(freq):
#  sinus function at freq(Hz) frequency
   t = np.arange(0., 0.01, 0.00005)
   plt.plot(t,np.sin(2*pi*freq*t))
   label1 = "fonction sinus, fréquence " 
   label2 = str(freq) 
   label3 = "Hz"
   label = label1 + label2 + label3 
   plt.ylabel(label)
   plt.show()