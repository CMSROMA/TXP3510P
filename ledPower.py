from TXP3510PWrapper import TXP3510P
from time import sleep

import argparse
parser = argparse.ArgumentParser(description='led power')                                                                                           
parser.add_argument("--port", type=str,default='/dev/ttyACM0',required=False, help="USB port")
parser.add_argument("--power", type=int,required=True, help="power status 1=ON 0=OFF")
parser.add_argument("--voltage", type=float,required=False, default=12.3,help="voltage target")
parser.add_argument("--current", type=float,required=False, default=1,help="max current")
 
args = parser.parse_args()         
c0=TXP3510P(args.port)
#c0=K2000('tcp://raspcmsroma01:8820')
#c0.selectChannel(1)
c0.powerOff()
#sleep(10)
#c0.powerOn()
c0.setVoltage(args.voltage)
c0.setCurrent(args.current)
print("Target V/I %s %s"%(c0.getVoltageTarget(),c0.getCurrentTarget()))
sleep(1)

if(args.power>0):
    print('Turning ON led')
    c0.powerOn()

sleep(1)
while True:
    print("Measured V/I %s %s"%(c0.getVoltage(),c0.getCurrent()))
    sleep(1)
