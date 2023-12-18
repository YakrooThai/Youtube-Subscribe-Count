import board, busio, displayio, time
import terminalio

from time import sleep


import os
import ipaddress
import wifi
import socketpool
import time
import adafruit_requests
import ssl
import os, sys
import gc
from youtube_config import CIRCUITPY_WIFI_SSID,CIRCUITPY_WIFI_PASSWORD,channel_name, API_KEY,video1,video2,video3,video4

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def display_first_IP(subi):
    ipv4_address_str = str(wifi.radio.ipv4_address)
    ipname = ipv4_address_str
    sub = str(subi)
    
    display_IP(ipname, sub)
    
def get_subscriber_count(channel_name):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_name}&key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
    
        if 'items' in data and len(data['items']) > 0:
            subscriber_count = data['items'][0]['statistics']['subscriberCount']
            return int(subscriber_count)
        else:
            return None
    except OSError as e:  
        print("Err requests1")
        return None
    except MemoryError as mem_error:
        print("Memory Error:", mem_error)
        return None
    except Exception as e:
        print("Unhandled exception:", e)
        pass  
    
def get_video_count(video1):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video1}&key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
    
        if 'items' in data and len(data['items']) > 0:
            video_count = data['items'][0]['statistics']['viewCount']
            return int(video_count)
        else:
            return None
    except OSError as e:  
        print("Err requests2")
        return None
    except MemoryError as mem_error:
        print("Memory Error:", mem_error)
        return None
    except Exception as e:
        print("Unhandled exception:", e)
        pass  
#-------------------------------
#
#-------------------------------
print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect(CIRCUITPY_WIFI_SSID, CIRCUITPY_WIFI_PASSWORD)

print("Connected to WiFi")
print("Available WiFi networks:")

found_Yakroo_RSSI = None

for network in wifi.radio.start_scanning_networks():
    ssid = str(network.ssid, "utf-8")
    if ssid == CIRCUITPY_WIFI_SSID :
        found_Yakroo_RSSI = network.rssi
        print("\t%s\t\tRSSI: %d\tChannel: %d" % (ssid, network.rssi, network.channel))
        break  

wifi.radio.stop_scanning_networks()

if found_Yakroo_RSSI is not None:
    print(f"RSSI: {found_Yakroo_RSSI}")
else:
    print("Yakroo_2.4GHz not found")

signal_strength = map_range(found_Yakroo_RSSI, -100, -40, 0, 5)
print("Signal Strength (0-5):", signal_strength)

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

#  prints IP address 
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
#===========================================
subscriber_count = get_subscriber_count(channel_name)

if subscriber_count is not None:
    print(f"Subscriber: {subscriber_count}")
    ipv4_address_str = str(wifi.radio.ipv4_address)
    ipname=ipv4_address_str
    sub=str(subscriber_count)
       
else:
        print("Error: Unable to fetch subscriber count")

    
oldcnt=0
while True:
    print(f"<<=======Youtube API========>>")
    try:
        subscriber_count = get_subscriber_count(channel_name)
    except OSError as e:  
        print("Err requests2")

    if subscriber_count is not None:
        print(f"Subscriber: {subscriber_count}")
        
        texts = "{:3}".format(subscriber_count)
        print("Sub= %s" % texts)
        tmp_sub=int(texts)
    else:
        print("Error: Unable to fetch subscriber count")
    gc.collect()
    print("mem: ", gc.mem_free())
    
    video_count1 = get_video_count(video1)
    if video_count1 is not None:
        print(f"Clip1: {video_count1}")
        textv1 = "{:3}".format(video_count1)
        print("v1= %s" % textv1)
        tmp_v1=int(textv1)
    else:
        print("Error: Unable to fetch subscriber count")
    gc.collect()
    print("mem: ", gc.mem_free())
   
    video_count2 = get_video_count(video2)
    if video_count2 is not None:
        print(f"Clip2: {video_count2}")
        textv2 = "{:3}".format(video_count2)
        print("v2= %s" % textv2)
        tmp_v2=int(textv2)
    else:
        print("Error: Unable to fetch subscriber count")
    gc.collect()
    print("mem: ", gc.mem_free())
   
    video_count3 = get_video_count(video3)
    if video_count3 is not None:
        print(f"Clip3: {video_count3}")
        textv3 = "{:3}".format(video_count3)
        print("v3= %s" % textv3)
        tmp_v3=int(textv3)
    else:
        print("Error: Unable to fetch subscriber count")
    gc.collect()
    print("mem: ", gc.mem_free())
    
    video_count4 = get_video_count(video4)
    if video_count4 is not None:
        print(f"Clip4: {video_count4}")
        textv4 = "{:3}".format(video_count4)
        print("v4= %s" % textv4)
        tmp_v4=int(textv4)
    else:
        print("Error: Unable to fetch subscriber count")
    gc.collect()
    print("mem: ", gc.mem_free())
    
    time.sleep(10)












