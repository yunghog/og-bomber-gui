#setup to install og-bomber
#author : Samartha
import platform
import getpass
import os
import json
banner="""

    ██████╗  ██████╗       ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
    ██╔═══██╗██╔════╝       ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██║   ██║██║  ███╗█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
    ██║   ██║██║   ██║╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ╚██████╔╝╚██████╔╝      ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝       ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                    ---------text & call bomber-spoofing---------
                            -----author : Samartha-----
                                 ---build v1.0---
"""
os.system('cls')
print(banner)
print('::Checking Requirements::')
try:
    from selenium import webdriver
    print("[+]selenium - available")
    try:
        driver=webdriver.PhantomJS()
        print("[+]PhantomJS - available")
    except Exception as e:
        print(e)
except ImportError:
    print("[-]selenium - not available")
    try:
        print("::Trrying to install selenium::")
        os.system("pip install selenium")
        print("[+]selenium installed")
    except Exception :
        print("Couldnt install [-]selenium\nTry again later")
        exit()
try:
    import requests
    print("[+]requests - available")
except ImportError:
    print("[-]requests - not available")
    try:
        print("::Trrying to install requests::")
        os.system("pip install requests")
        print("[+]requests installed")
    except Exception :
        print("Couldnt install [-]requests\nTry again later")
        exit()
myOs=platform.system()
username = getpass.getuser()
driver=webdriver.PhantomJS()
print("::Registering the user::")
request_string="http://ogbomber.rf.gd/isExist.php?un="+username
driver.get(request_string)
exists_response=driver.find_element_by_id("result").text
if 'true' in exists_response:
    print("[+]user Already registered")
elif 'false' in exists_response:
    request_string="http://ogbomber.rf.gd/register.php?un="+username+"&os="+myOs
    driver.get(request_string)
    print("[+]User registered")
else:
    print(exists_response)
print("::User profile::")
request_string="http://ogbomber.rf.gd/userDetails.php?un="+username
driver.get(request_string)
user_details=driver.find_element_by_id("result").text
user_details_json=json.loads(user_details)
u=user_details_json
print("[+]User ID : ",u["uid"],"\n[+]Username : ",u["uname"],"\n[+]Subscription : ",u["urole"], "\n[+]Quota    : ",u["uquota"])
if u["urole"]=="free":
    print("""Now you are having free membership. You are limited to send 200 messages everyday
Subscribe to premium and get unlimited messages everyday
::Use this to prank your friends only::
::dont misuse::""")
