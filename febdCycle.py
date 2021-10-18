from TXP3510PWrapper import TXP3510P
from time import sleep

c0=TXP3510P('/dev/ttyACM0')
#c0=K2000('tcp://raspcmsroma01:8820')
#c0.selectChannel(1)
c0.powerOff()
sleep(10)
c0.powerOn()

while True:
    print("Measured V/I %s %s"%(c0.getVoltage(),c0.getCurrent()))
    sleep(1)

