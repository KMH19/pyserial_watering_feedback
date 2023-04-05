import serial.tools.list_ports
import cronitor
import time
import datetime

ports = serial.tools.list_ports.comports()
cronitor.api_key = '0c78d73ce8324e37b464617df85e43af'

serialInst = serial.Serial()
portsList = []

count = 1
errors = 0

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
            packet = serialInst.readline()
            
            ## Printing the raw string 
            # print(repr(packet))
            
            if packet.decode('utf').lstrip('b').rstrip('\r\n') == 'water':
    
                print("Water tick:", datetime.datetime.now())
                
                monitor = cronitor.Monitor('water-tick')

                # send a heartbeat event with a message
                monitor.ping(message="Water tick received", metrics={'count': count, 'error_count': errors})

                # include counts & error counts
                #monitor.ping(metrics={'count': count, 'error_count': errors})
                
                count+=1
                
                time.sleep(10)
                
    