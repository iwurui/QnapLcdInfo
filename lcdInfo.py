#!/usr/bin/env python3
import psutil, socket, re, threading, datetime, time, platform
from qnapdisplay import QnapDisplay

Lcd = QnapDisplay()
infoIndex=0
t=None
blankLcdTimeout=5;

def getDataArray(network_regex="^eth|^enp|^bond"):
        output = []
        cpu_freq = psutil.cpu_freq()
        output.append([socket.gethostname(), platform.platform()])
        output.append(["CPU: "+ str(psutil.cpu_percent(1))+"% ","FREQ: "+str(int(cpu_freq.current))+" MHz"])
        output.append(["LOAD(1m): "+ str(psutil.getloadavg()[0]),"LOAD(5m): "+ str(psutil.getloadavg()[1])])
        output.append(["Last boot:", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")])
        output.append(["Memory: "+str(psutil.virtual_memory().percent)+"%","Swap: "+str(psutil.swap_memory().percent)+"%"])
        for disk in psutil.disk_partitions():
                output.append(["Usage " + disk.mountpoint ,str(int(psutil.disk_usage(disk.mountpoint).used / (1024**3))) + "G/" + str(int(psutil.disk_usage(disk.mountpoint).total / (1024**3)))+ "G" + " " + str(psutil.disk_usage(disk.mountpoint).percent)+ "%"])
        networks = psutil.net_if_addrs()
        for network in networks:
                if(networks[network][0].netmask and re.search(network_regex,network)):
                        output.append([network, networks[network][0].address])
        return(output)
def timerCallback():
#        Lcd.Disable()
        Lcd.Enable()
def timerReset(t=None):
        if(t):
                t.cancel()
        t = threading.Timer(blankLcdTimeout, timerCallback)
        t.start()
        return t

while(True):
        t = timerReset(t)
        Lcd.Enable()
        data= getDataArray()
        Lcd.Write(0, data[infoIndex][0])
        Lcd.Write(1, data[infoIndex][1])
        if(Lcd.Read() =="Up"):
                delta= -1;
        else:
                delta= +1;
        infoIndex = (infoIndex + delta) % len(data)
