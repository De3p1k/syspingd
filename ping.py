import os
import subprocess 

response = os.system("ping -q -c 1 <IP OR HOST NAME OF THE SERVER> > /dev/null")

if response == 0:
  file = open("<PATH TO YOUR LOG FILE>", 'r')
  if file.readline() !='A':
    file.close()
    os.system("dunstify --icon <PATH TO YOUR ICON> 'The server is up!'")
    file = open("<PATH TO YOUR LOG FILE>", 'w')
    file.write('A')
    file.close()
else:
  file = open('<PATH TO YOUR LOG FILE>', 'r')
  if file.readline() == 'A':
    file.close()
    os.system("dunstify --icon <PATH TO YOUR ICON> 'The server is down'")
    file = open("<PATH TO YOUR LOG FILE>", 'w')
    file.write('B')
    file.close()
file.close()%                                                                                                                                                                                                                                                         
