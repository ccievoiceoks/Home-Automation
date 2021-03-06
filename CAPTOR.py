import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Magnetic Contact
GPIO.setup(21,GPIO.IN)
GPIO.setup(26,GPIO.IN)
#Output Contact Led 
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

counters=0
max_counters=int(raw_input("\nHow many times do I need to iterate the loop? :\n\n "))
while counters<max_counters:
  if (GPIO.input(21)==0):
    status1="Contact Ferme"
  else:
    status1="Contact Ouvert"
  if (GPIO.input(26)==0):
    status2="Contact Ferme"
  else:
    status2="Contact Ouvert"
  
  if (GPIO.input(21)):
    print "\nValue Contact BAS =====> ",status1
    print "\nValue Contact HAUT =====> ",status2
    print("Open Contact")
    GPIO.output(4,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    counters+=1
    print "\nCounters => " + str(counters)
  else:
    print "\nValue Contact BAS =====> ",status1
    print "\nValue Contact HAUT =====> ",status2
    print ("Closed Contact")
    GPIO.output(18,GPIO.LOW)
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    counters+=1
    print "Counters => " + str(counters)
GPIO.output(4,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
if (status1=="Contact Ferme" and status2=="Contact Ouvert"):
  print "\n\n\n STATUS FINAL : la porte est FERMEE"
elif (status1=="Contact Ouvert" and status2=="Contact Ferme"):
  print "\n\n\n STATUS FINAL : la porte est OUVERTE"
else:
  print "\n\n\n STATUS FINAL : la porte n'est ni FERMEE ni OUVERTE , elle est ENTRE-OUVERTE"
print " "
print " Script Terminated" 
GPIO.cleanup()