
import requests
import time
import multiprocessing

authToken = "{check readme.md}"
requestPost = "{check readme.md}"

def beg():

	payload = {
		'content': "pls beg"
	}
	header = {
		'authorization': authToken
	}
	r = requests.post(requestPost, data=payload, headers=header)
def hunt():

	payload1 = {
		'content': "pls hunt"
	}

	header1 = {
		'authorization': authToken
	}
	r = requests.post(requestPost, data=payload1, headers=header1)


def fish():
	payload2 = {
		'content': "pls fish"
	}

	header2 = {
		'authorization': authToken
	}
	r = requests.post(requestPost, data=payload2, headers=header2)

def dig():
	payload3 = {
		'content': "pls dig"
	}

	header3 = {
		'authorization': authToken
	}

	r = requests.post(requestPost, data=payload3, headers=header3)	

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

