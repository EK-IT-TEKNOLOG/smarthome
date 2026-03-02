#smarthome_main.py l. 90:
########################################
# VARIABLES
mac_addr_receiver = []                 # The list holding the MAC address of the receivers
#Tilføj mac adresser på jeres styringer her
sirene = b'\x12\x23\x34\x45'
#Tilføj mac adresser på jeres sensorer her
flammesensor = b'\x12\x23\x34\x45'
#.... Indsæt flere her
#Indsæt styringer som peers:
en.esp_now_add_mac_address(sirene)

#smarthome_main.py l. 496:
    if msg:
        msg = msg.decode("utf-8")
        mac_addr = misc.mac_addr_bytestr_to_str(host)
        if msg[0] == '*':              # By design, EK ITT, is the first char of a broadcast messages an *
            if show_broadcast_messages == 1: # Only show broadcast messages if wanted. Control in Configuration
                lcd.print_received_frame(mac_addr, msg)
                print("Broadcast " + mac_addr + "  " + msg[1:]) # Remove the broadcast identifier *
        else:
            lcd.print_received_frame(mac_addr, msg)
            print("Message   " + mac_addr + "  " + msg)
            # Do something with the direct messages here
            data_from_msg = msg.split('|')
            if host == flammesensor:
                print('[+] Got data from flamesensor')
                if data_from_msg[3]: #Make sure you change this to match your data
                    en.esp_now_send_message(sirene, b'ACTIVATE') #Or some other message that you want to use

