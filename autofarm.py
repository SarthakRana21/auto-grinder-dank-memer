import requests
import time
import multiprocessing

def beg():

	payload = {
		'content': "pls beg"
	}
	header = {
		'authorization': 'OTg5MTEzNzY1Mjg0OTY2NDQw.GmbKmu.uam-UpHAl-zXhf2XODXuxhLaXMZ7UnmukTy4y0'
	}
	r = requests.post('https://discord.com/api/v9/channels/798564021635776512/messages', data=payload, headers=header)
def hunt():

	payload1 = {
		'content': "pls hunt"
	}

	header1 = {
		'authorization': 'OTg5MTEzNzY1Mjg0OTY2NDQw.GmbKmu.uam-UpHAl-zXhf2XODXuxhLaXMZ7UnmukTy4y0'
	}
	r = requests.post('https://discord.com/api/v9/channels/798564021635776512/messages', data=payload1, headers=header1)


def fish():
	payload2 = {
		'content': "pls fish"
	}

	header2 = {
		'authorization': 'OTg5MTEzNzY1Mjg0OTY2NDQw.GmbKmu.uam-UpHAl-zXhf2XODXuxhLaXMZ7UnmukTy4y0'
	}
	r = requests.post('https://discord.com/api/v9/channels/798564021635776512/messages', data=payload2, headers=header2)

def dig():
	payload3 = {
		'content': "pls dig"
	}

	header3 = {
		'authorization': 'OTg5MTEzNzY1Mjg0OTY2NDQw.GmbKmu.uam-UpHAl-zXhf2XODXuxhLaXMZ7UnmukTy4y0'
	}

	r = requests.post('https://discord.com/api/v9/channels/798564021635776512/messages', data=payload3, headers=header3)	

for x in range(1000):
	p1 = multiprocessing.Process(target=beg)
	p2 = multiprocessing.Process(target=hunt)
	p3 = multiprocessing.Process(target=fish)
	p4 = multiprocessing.Process(target=dig)

	if __name__ == '__main__':
		p1.start()
		time.sleep(6.5)
		
		p2.start()
		time.sleep(6.5)
		
		p3.start()
		time.sleep(6.5)
		
		p4.start()
		time.sleep(6.5)
