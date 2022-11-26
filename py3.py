#retourne une tramme sous forme de liste de caractere hexadecimal a partir d'un fichier texte 

import sys
import os
import binascii


def start(file):
    #ouvre le fichier texte
  with open(file, "r+") as file:
        lines = [l for l in (line.strip() for line in file) if l]  # retire les lignes vides
        Trame = []
        for i in range(len(lines)):
            #retirer les espace au debut et a la fin de la ligne
            lines[i] = lines[i].strip()
            #on separe l'offset et le code hexa
            split = lines[i].split("  ")
            offset = []
            offset = offset + split[0].split(" ")
            #on split par des espaces
            ltrame = split[1].split(" ")
            #on retire les espaces vides
            ltrame = [x for x in ltrame if x]
            #converti l'offset en hexa
            offset = int(split[0], 16) 
            Trame.append(ltrame)
            #print(offset)
            #print(ltrame)
        #print(Trame)
        ethernet(Trame)
        http(Trame)
        #ferme le fichier
        file.close()
        return Trame

#convertit hexadecimal en decimal 
def convert(a) :
    return int(a,base=16)

#retourne le datagramme ipv4 
def ethernet(Trame):
    print("Ethernet Header")
    print("Destination MAC: ", Trame[0][0], Trame[0][1], Trame[0][2], Trame[0][3], Trame[0][4], Trame[0][5])
    print("Source MAC: ", Trame[0][6], Trame[0][7], Trame[0][8], Trame[0][9], Trame[0][10], Trame[0][11])
    print("Type: ", Trame[0][12], Trame[0][13])
    ip = Trame[0][12], Trame[0][13]
    if(ip[1]=='00'):
        print("Type: IP")
        ipv4(Trame)

#affiche le datagramme ipv4 
def ipv4(Trame):
    print("IP Header")
    print("Version: ", Trame[0][14][0])
    print("Header Length: ", Trame[0][14][1])
    print("Type of Service: ", Trame[0][15])
    print("Total Length: ", convert(Trame[1][0] + Trame[1][1]))
    print("Identification: ",Trame[1][2], Trame[1][3])
    print("Flags: ", (Trame[1][4]))
    print("Fragment Offset: ",Trame[1][5])
    print("Time to Live: ",convert(Trame[1][6]))
    #lister les differents protocole
    if (Trame[1][7] == '06'):
        print("Protocol: TCP")
        print("Header Checksum: ",Trame[1][8], Trame[1][9])
        print("Source address: ",convert(Trame[1][10]),".",convert(Trame[1][11]),".",convert(Trame[1][12]),".",convert(Trame[1][13]))        
        print("Destination address",convert(Trame[1][14]),".",convert(Trame[1][15]),".",convert(Trame[2][0]),".",convert(Trame[2][1]))
        tcp(Trame)
    elif (Trame[1][7] == '11'):
        print("Protocol: UDP")
        print("Header Checksum: ",Trame[1][8], Trame[1][9])
        print("Source address: ",convert(Trame[1][10]),".",convert(Trame[1][11]),".",convert(Trame[1][12]),".",convert(Trame[1][13]))        
        print("Destination address",convert(Trame[1][14]),".",convert(Trame[1][15]),".",convert(Trame[2][0]),".",convert(Trame[2][1]))
        udp(Trame)
    else:
        print("Protocol: ",Trame[1][7])
        print("Header Checksum: ",Trame[1][8], Trame[1][9])
        print("Source address: ",convert(Trame[1][10]),".",convert(Trame[1][11]),".",convert(Trame[1][12]),".",convert(Trame[1][13]))        
        print("Destination address",convert(Trame[1][14]),".",convert(Trame[1][15]),".",convert(Trame[2][0]),".",convert(Trame[2][1]))


def udp(Trame):
    print("UDP Header")
    print("Source Port: ",convert(Trame[2][2] + Trame[2][3]))
    print("Destination Port: ",convert(Trame[2][4] + Trame[2][5]))
    print("Length: ",convert(Trame[2][6] + Trame[2][7]))
    print("Checksum: ",Trame[2][8] + Trame[2][9])


def tcp(Trame):
    print("TCP Header")
    print("Source Port: ",convert(Trame[2][2] + Trame[2][3]))
    print("Destination Port: ",convert(Trame[2][4] + Trame[2][5]))
    print("Sequence Number: ",convert(Trame[2][6] + Trame[2][7] + Trame[2][8] + Trame[2][9]))
    print("Acknowledgement Number: ",convert(Trame[2][10] + Trame[2][11] + Trame[2][12] + Trame[2][13]))
    print("Header Length: ",Trame[2][14][0])
    print("Flags: ",Trame[2][14][1]+Trame[2][15])
    flags = convert(Trame[2][14][1]+Trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    print("Reserved bit: ",flags[0:3])
    print("Nonce: ",flags[3])
    print("Congestion Window Reduced (CWR): ",flags[4])
    print("ECN-Echo: ",flags[5])
    print("Urgent: ",flags[6])
    print("Acknowledgement: ",flags[7])
    print("Push: ",flags[8])
    print("Reset: ",flags[9])
    print("Syn: ",flags[10])
    print("Fin: ",flags[11])
    print("Window: ",convert(Trame[3][0] + Trame[3][1]))
    print("Checksum: ",Trame[3][2] + Trame[3][3])
    print("Urgent Pointer: ",convert(Trame[3][4] + Trame[3][5]))
    #print("Options: ", Trame[3][6:])

#convert from decimal to ascii
def convertToAscii(dec):
    return chr(dec)

def http(Trame):
    print("HTTP Header")
    for i in range (4,len(Trame)):
        for j in range (0,len(Trame[i])):
            print(convertToAscii(convert(Trame[i][j])),end='')
    

start(sys.argv[1])


    



