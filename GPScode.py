from geopy.geocoders import Nominatim
import serial # Serial communication with the GPS uart protocol 
ser = serial.Serial("/dev/ttyACM1",115200) # Set the comport and baudrate 
x = str(ser.read(1200))

pos1 = x.find("$GPRMC")
pos2 = x.find("\n",pos1)
compass = x.find("$GPGLL")
loc = x[pos1:pos2]
data = loc.split(',')
geolocator = Nominatim(user_agent="Catbot GPS CRS101-series")
#if data[2] == 'V':
#      print('No location found')
while True:
     #print(ser.readline())
     print(data)
     if data[2] == 'V':
        print('No location found')
     else:
       print(data)
    # location = geolocator.reverse(str(float(data[3])/100),str(float(data[5])/100))
    # print(location.address)
   #  try: 
       print("Latitude =" + str(data[3]))
       print("Longtitude = " + str(data[5]))
       location = geolocator.reverse(str(data[3])+","+ str(data[5])) 
       print(location.address)
    # except: 
        #print("Connecting sattellite.....")
       print("Compass=" + data[4] +"," + data[6])
       print("speed = " + data[7])
       print("Course = " + data[8])
