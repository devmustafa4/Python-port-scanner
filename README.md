# Python-port-scanner
A simple port scanner that scans the ports based on user input built using python.

## Prerequisites
- You must have python 3 installed in your system. 

## How to Run:
- Clone the repository to your pc
- Navigate inside the python-port-scanner folder 
- Open Cmd
- Type "python portscanner.py target_ip_address"
  replace target_ip_address with an ip of your choice.
  
## Sample Ouput
![image](https://user-images.githubusercontent.com/74109263/145900072-91a1022a-f2bf-4015-b1d3-0f3fb46f2245.png)
right: A local host is started at 127.0.0.1 and port 8000
left: The program is run to scan the ip address for open ports

The program runs on a single thread and is slow but can be made faster by adding multithreading to the program.
