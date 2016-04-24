#Network Programmability as a Cloud Service
##Network virtualization and programability
---
**Contributors:**

1. Akshay Kumar Battaje
2. Amey Uchagaonkar  
3. Deepanshu Lulla
4. Anuj Tyagi

Mentor: Somaya Arianfar

---
![alt tag](https://github.com/BU-NU-CLOUD-SP16/Network-Programmability-as-a-Service/blob/master/image.jpg)  

**The goals of this project are:**

Add multi–domain network virtualization support to OpenVirtex
Support interoperability between the Multi-domain OpenVirtex and the rest of the MOC platform, e.g. HaaS or/and OpenStack 
Evaluate various aspects of the resulting system, and
Explore novel networking services enabled by providing full network control to the customers

**Technologies used:**

* Mininet (virtual network emulator) and OVS  
* OpenVirtex  
* SDN Controller (FloodLight)  
* Python  
* Java  
* JSON  
* MongoDB  
  

---
**Installation and Deployment**  

**Install Mininet**  
```
#sudo apt-get install mininet  
#git clone git://github.com/mininet/mininet  
#cd mininet  
#install.sh -h  
```
**Install OpenVirtex**  
```
#git clone https://github.com/OPENNETWORKINGLAB/OpenVirteX.git -b 0.0-MAINT  
```
**Install FloodLight**
```
#sudo apt-get install build-essential default-jdk ant python-dev eclipse  
#git clone git://github.com/floodlight/floodlight.git  
#cd floodlight  
#java -jar target/floodlight.jar  
```

**Setup:**

**1. Running Mininet Topology**  
```
#python mininet_topology.py  
```
**2. Running OpenVirtex**  
```
#sh OpenVirteX/scripts/ovx.sh  
#ovx_virtual_topo1.py   
// for hardware domain 1  
#ovx_virtual_topo2.py  
//for hardware domain 2  
```
**3. Running Central Server**   
```
# python centralServer.py
```
