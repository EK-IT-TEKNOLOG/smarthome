# https://docs.micropython.org/en/latest/library/espnow.html
import network
import espnow
import binascii
import time
wlan = network.WLAN(network.STA_IF) 
# A WLAN interface must be active to send()/recv()
station = network.WLAN(network.STA_IF)
station.active(True)

esp_now = espnow.ESPNow()
esp_now.active(True)
peer = b'\xff\xff\xff\xff\xff\xff'
esp_now.add_peer(peer)

def get_mac_address():
    wlan.active(True)                      # Activate the WLAN

    if wlan.active():                      # Check if the WLAN is active

        mac_address = wlan.config("mac")   # Returns the MAC address in six bytes
        
        print("[+] The MAC address is: ", end = "")
        for i in range(5):
            print("%02X:" % mac_address[i], end = "")
        print("%02X" % mac_address[5])     # Print the last byte without the trailing colon

    else:
         print("WLAN is not active")

get_mac_address()
start_time = time.ticks_ms()
threshold = 3000
while True:
    host, msg = esp_now.recv(100)
    if msg:             # msg == None if timeout in recv()
        print(f'[+] {time.ticks_ms()}: Besked fra',binascii.hexlify(host),':', msg)
        get_mac_address()
    #print(start_time, time.ticks_ms(),time.ticks_diff(start_time, time.ticks_ms()))
    if abs(time.ticks_diff(time.ticks_ms(), start_time)) > threshold:
        print('[+] Activating actuators')
        try:
            esp_now.send(peer, [b'ACTIVATE', b'DEACTIVATE'][random.randint(0,1)])
        except:
            pass
        start_time = time.ticks_ms()
        get_mac_address()

