import time as t
import matplotlib.pyplot as p
print ('This app will help you to type faster!!!')
input ('to continue press enter.')
times = []
counter = 0
tries = []
print ("You will be typing the sentence 'perplexoid is the best' 5 times as fast as you can.")
print ('Easy - if you make a mistake you can repeat the exact try without losing time.')
input ('To start on easy difficulty (others in development), press enter.')

while counter < 5:
    time_s = round(float(t.time()), 2)
    word = input ("Type 'perplexoid is the best', quick! ")
    if word != 'perplexoid is the best':
        print ("You've made a mistake, try again.")
        time_s = round(float(t.time()), 2)
        word = input ("Type 'perplexoid is the best', quick! ")
    time_e = round(float(t.time()), 2)
    times.append (time_e - time_s)
    trys = counter + 1
    counter += 1
    tries.append (str(trys))
print ('Congratulations! Here is the plot of you success (or suckcess).')
t.sleep (3)
print ('--------')
p.plot (tries, times)
p.ylabel ('Taken time')
p.xlabel ('Number of try')
p.show()
    
