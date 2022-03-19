# coding=UTF-8
import time, json, random, queue, types, sys, socket, math, os
from binascii import hexlify
from TestUtilsL23 import XenaScriptTools

def runtest(xm, ports, rate, size, duration):
	print("Start the scripting...")
	##RELEASE THE ports, relinquish other users.
	xm.Send(ports[0] + ' P_RESERVATION RELEASE')
	xm.Send(ports[0] + ' P_RESERVATION relinquish')
	xm.Send(ports[1] + ' P_RESERVATION RELEASE')
	xm.Send(ports[1] + ' P_RESERVATION relinquish')


	##Release the port and then Reserve the ports
	print ("Resever the port...")
	xm.Send(ports[0] + ' P_RESERVATION RESERVE')	
	xm.Send(ports[1] + ' P_RESERVATION RESERVE')
	##RESET PORTS
	xm.Send(ports[0] + ' P_RESET')
	xm.Send(ports[1] + ' P_RESET')
	time.sleep(3)


	MAC1= '000000000002'
	MAC2= '000000000001'
	IP1 = '192.168.100.100'
	IP2 = '192.168.100.101'
	IP1 = hexlify(socket.inet_aton(IP1)).decode()
	IP2 = hexlify(socket.inet_aton(IP2)).decode()
	hearder1 = '0x' + str(MAC2) + str(MAC1) + '08004500002E000000007FFFF0B6' + str(IP1) + str(IP2) 
	hearder2 = '0x' + str(MAC1) + str(MAC2) + '08004500002E000000007FFFF0B6' + str(IP2) + str(IP1) 

	print("Start to configure the streams...")
	##Create the streams in port 0
	##Create the SID index of stream
	xm.SendExpectOK(ports[0] + " PS_CREATE [0]")
	##Create the TPLD index of stream
	xm.SendExpectOK(ports[0] + " PS_TPLDID [0] 0")
	##Configure the packet size
	xm.SendExpectOK(ports[0] + " PS_PACKETLENGTH [0]" + size)
	##Configure the packet type
	xm.SendExpectOK(ports[0] + " PS_HEADERPROTOCOL [0] ETHERNET IP")
	##Configure the packet header
	xm.SendExpectOK(ports[0] + " PS_PACKETHEADER [0] "+ str(hearder1))
	##Enable streams
	xm.SendExpectOK(ports[0] + " PS_ENABLE [0] on")
	##Configure the stream rate
	xm.SendExpectOK(ports[0] + " PS_RATEFRACTION [0] " + str(int(rate)*10000))

	##Create the streams in port 1
	xm.SendExpectOK(ports[1] + " PS_CREATE [1]")
	xm.SendExpectOK(ports[1] + " PS_TPLDID [1] 1")
	xm.SendExpectOK(ports[1] + " PS_PACKETLENGTH [1]" + size)
	xm.SendExpectOK(ports[1] + " PS_HEADERPROTOCOL [1] ETHERNET IP")
	xm.SendExpectOK(ports[1] + " PS_PACKETHEADER [1] "+ str(hearder2))
	xm.SendExpectOK(ports[1] + " PS_ENABLE [1] on")
	xm.SendExpectOK(ports[1] + " PS_RATEFRACTION [1] " + str(int(rate)*10000))

	print("Start the traffic...")
	#####START TRAFFIC
	xm.SendExpectOK(ports[0] + ' P_TRAFFIC ON')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC ON')
	time.sleep(2)
	xm.SendExpectOK(ports[0] + ' P_TRAFFIC OFF')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC OFF')
	xm.SendExpectOK(ports[0] + ' PT_CLEAR')
	xm.SendExpectOK(ports[1] + ' PT_CLEAR')
	xm.SendExpectOK(ports[0] + ' PR_CLEAR')
	xm.SendExpectOK(ports[1] + ' PR_CLEAR')
	time.sleep(1)

	xm.SendExpectOK(ports[0] + ' P_TRAFFIC ON')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC ON')
	time.sleep(int(duration))
	xm.SendExpectOK(ports[0] + ' P_TRAFFIC OFF')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC OFF')
	print("Stop the traffic and collect the result...")
	xm.Send(ports[0] + ' P_RESERVATION RELEASE')
	xm.Send(ports[1] + ' P_RESERVATION RELEASE')
	time.sleep(2)

	####Get traffic result
	##Get the TX and RX result
	TX1 = (filter(xm, ports[0] + ' PT_STREAM [0] ?'))[3]
	TX2 = (filter(xm, ports[1] + ' PT_STREAM [1] ?'))[3]
	RX1 = (filter(xm, ports[1] + ' PR_TPLDTRAFFIC [0] ?'))[3]
	RX2 = (filter(xm, ports[0] + ' PR_TPLDTRAFFIC [1] ?'))[3]
	print('TX1: %s, TX2: %s, RX1: %s, RX2: %s,'%(TX1, TX2, RX1, RX2))

	##Get the latency 
	latency1 = (filter(xm, ports[1] + ' PR_TPLDLATENCY [0] ?'))[1]
	latency2 = (filter(xm, ports[0] + ' PR_TPLDLATENCY [1] ?'))[1]

	##Get the error
	error1 = filter(xm, ports[1] + ' PR_TPLDERRORS[1] ?')
	error2 = filter(xm, ports[0] + ' PR_TPLDERRORS[0] ?')

	##Get the FCS
	FCS1 = (filter(xm, ports[0] + ' PR_EXTRA ?'))[0]
	FCS2 = (filter(xm, ports[1] + ' PR_EXTRA ?'))[0]

	##Caculate the lost
	Lost1 = int(TX1) - int(RX1)
	Lost2 = int(TX2) - int(RX2)

	##print the result
	print()
	print ('----------------------------------------------------------------------------------------------------')
	print ('Stream1 |  TX: ' + str(TX1) + '  |  RX: ' + str(RX1) + '  |  Lost :' + str(Lost1) + ' |  FCS: ' + str(FCS2) + '  |  Misoder Error: ' + error1[2] + '  |  Payload Errors: ' + error1[3])
	print ('----------------------------------------------------------------------------------------------------')
	print ('Stream2 |  TX: ' + str(TX2) + '  |  RX: ' + str(RX2) + '  |  Lost :' + str(Lost2) + ' |  FCS: ' + str(FCS1) + ' |  Misoder Error: ' + error2[2] + '  |  Payload Errors: ' + error2[3])
	print ('----------------------------------------------------------------------------------------------------')
	print ('Ending.......')


def filter(xm, cmd):
	getvalue = xm.Send(cmd)
	getvalue1 = getvalue.split('  ')[-1]
	getvalue2 = getvalue1.split(' ')
	return getvalue2

def main(argv):
	with open('config.txt','r+') as f:
		configs = f.readlines()
	config_dict = {}
	for conf in configs:
		parsed = conf.strip('\n').split(':')
		if len(parsed) > 1:
			config_dict[parsed[0]] = parsed[1]

	ip_address = config_dict.get('ip_address')
	print(ip_address)
	ports = config_dict.get('ports').split(' ')
	print(ports)
	rate = config_dict.get('rate')
	size = config_dict.get('size')
	duration = config_dict.get('duration')
	xm = XenaScriptTools(ip_address)
	print('Start to connect to the chassis...')
	xm.LogonSetOwner("xena", "python_test_1")
	print('Logon successful...')
	runtest(xm, ports, rate, size, duration)


if __name__ == '__main__':
    sys.exit(main(sys.argv))