import os
import subprocess 
#hostname = "google.com" #example
response = os.system("ping -q -c 1 eepaserves > /dev/null")

if response == 0:
  #print (hostname, 'is up!')
  os.system("dunstify 'The server is up!'")
else:
  #print (hostname, 'is down!')
  os.system("dunstify 'The server is down'")