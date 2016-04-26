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
# sudo apt-get install mininet  
# git clone git://github.com/mininet/mininet  
# cd mininet  
# install.sh -h  
```
**Install OpenVirtex**  
```
# git clone https://github.com/OPENNETWORKINGLAB/OpenVirteX.git -b 0.0-MAINT

Copy the following files from this repository to the OpenVirteX directory as

# cp ovx/java/src/CreateOVXNetwork.java OpenVirteX/src/main/java/net/onrc/openvirtex/api/service/handlers/tenant/
# cp ovx/java/src/ConnectHost.java OpenVirteX/src/main/java/net/onrc/openvirtex/api/service/handlers/tenant/
# cp ovx/java/src/DisconnectHost.java OpenVirteX/src/main/java/net/onrc/openvirtex/api/service/handlers/tenant/

These files are necessary for sending messages on change in configuration

Remove the old jar file
# rm OpenVirteX/target/OpenVirteX.jar

Make following changes in OpenVirteX/scripts/ovx.sh file

1. Comment the line 
    mvn package > /dev/null
    
2. Add the below line,
    mvn package -Dmaven.test.skip=true > /dev/null


```
**Install FloodLight**
```
# sudo apt-get install build-essential default-jdk ant python-dev eclipse  
# git clone git://github.com/floodlight/floodlight.git  
# cd floodlight  
# java -jar target/floodlight.jar  
```

**Setup:**
```
Run the following on seperate VMs
```
**1. Running Mininet Topology**  
```
# sudo python mininet_topology.py  
```

**2. Running OpenVirteX**
```
(i) Start MongoDB for OpenVirteX

# sudo mkdir ~/mongo_data/
# sudo mongod --dbpath ~/mongo_data/ --logpath ~/mongologs --fork

(ii) Run OpenVirteX
# sh OpenVirteX/scripts/ovx.sh  

(iii) Add switches to the the virtual topology
# python ovx/utils/add_switches.py <CONTROLLER_IP_1> <PORT_1> <CONTROLLER_IP_2> <PORT_2>

where,
CONTROLLER_IP_1 : IP address of the controller for Tenant_1
CONTROLLER_IP_2 : IP address of the controller for Tenant_2
```
**3. Running the Publisher**   
```
# cd ovx/scripts
# sh start_publisher.sh <file_with_list_of_ovx_ips>

The publisher will start listening to incoming messages on port 50000
```
**4. Running message receivers on OVXs**
```
On each VM running OVX,

# cd ovx/scripts
# sh start_receiver.sh <ip_of_the_publisher>

The receiver will start listening to incoming messages from the publisher on port 49999
```

**Configuration:**

**1. Adding hosts:**
```
The following files can be used to add hosts to the virtual topology

ovx/utils/add_hosts_hd1.py -- Adds hosts to hardware domain 1
ovx/utils/add_hosts_hd2.py -- Adds hosts to hardware domain 2
ovx/utils/add_hosts_hd3.py -- Adds hosts to hardware domain 3
```

**2. Test for connectivity:**
```
On the VM running mininet,

mininet> h1 ping -c3 h3

mininet> h2 ping -c3 h6

mininet> h2 ping -c3 h4

The above commands should be able to ping the hosts
```

**Teardown:**

**1. Stop mininet:**
```
On the VM running mininet

mininet> exit

# sudo mn -c

```

**2. Stop publisher:**
```
# cd ovx/utils/
# python stop_publisher.py
```

**3. Stop receivers on each OVX:**
```
# cd ovx/utils/
# python stop_receiver.py
```

**4. Stopping OpenVirteX:**
```
Press CTRL + C to stop the script ovx.sh
```
