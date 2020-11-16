Please read this document first for detailed explanation of the submission and also how to run and test it.

This is the directory structure:
Group_49
	- readme.txt
	- pltFiles/
        - UdpandTcpHighSpeed_delay_Separate.plt
        - UdpandTcpHighSpeed_delay_Simulataneous_Different_Start.plt
          ........ 16 more such files
    - pdfFiles/
        - UdpandTcpHighSpeed_delay_Separate.pdf
        - UdpandTcpHighSpeed_delay_Simulataneous_Different_Start.pdf
          ........ 16 more such files
    - main-app6.cc
    - main-app6.h


A short description about each file/folder:
1. readme.txt - This is the current file, with all the instructions and brief descriptions needed to run, test and understand the submission.
2. pltFiles - This directory has 18 plt files, covering all the cases (we have discussed it below). The plt files are generated from the code, and have all the points, XY axes labels, title etc.
3. pdfFiles - This directory has 18 pdf files, covering all the cases (we have discussed it below). The pdf files are made using gnuplot. These have been the actual plots drawn in them.
4. main-app6.cc - This file is the c++ code, that uses ns3 and flow monitor to create the simulation of the application.
5. main-app6.h - This file has the headers needed for the code to run. Those include constants, strings, and fucntion definitions.


Prerequisites before running:
1. Make sure that ns3 is downloaded and installed in the Ubuntu environment. The instructions are here: 
    Download : https://www.nsnam.org/releases/ns-3-31/
    Install : https://www.nsnam.org/wiki/Installation
    YouTube video : https://youtu.be/TbsNjQBU9dI

2. Make sure gnuplot is installed in the Ubuntu environment. If not simply open a terminal (Ctrl+Alt+T) and type:
    $ sudo apt-get install gnuplot


How to run and test:

Method = (typing all commands one after the other).

a. First make sure that the files main-app.cc and main-app.h are in the following path (basically inside the scratch folder) of ns3 installtion.
    /home/<user-name>/ns-allinone-3.31/ns-3.31/scratch/main-app6.cc
    /home/<user-name>/ns-allinone-3.31/ns-3.31/scratch/main-app6.h

b. Now run the follwing command in the terminal (inside the ns-3.31 folder).
    $ ./waf --run "scratch/main-app6 --tcpProtocol=<Protocol Name> --loopRuns=<count> --simultaneously=<0 or 1> --offset=<time in sec> --runTime=<time in sec> --packetSize=<size in bytes>"
   For example :
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpHighSpeed --loopRuns=30 --simultaneously=1 --offset=3 --runTime=1 --packetSize=1024"
    All these parameters are optional, since we have already initialised it inside the code.
    Also note that runtime is in a factor of 5 seconds.

c. In the same way as b, there are 9 commands to run for 9 possible cases (each for delay and throughput). The cases are as follows:
    CASE 1.
    tcpProtocol=TcpHighSpeed, TcpVegas, TcpScalable; simultaneously=0; Rest of the parameters does not matter (preferable as given in example).
    CASE 2.
    tcpProtocol=TcpHighSpeed, TcpVegas, TcpScalable; simultaneously=1; offset=0; Rest of the parameters does not matter (preferable as given in example).
    CASE 3.
    tcpProtocol=TcpHighSpeed, TcpVegas, TcpScalable; simultaneously=1; offset=3; Rest of the parameters does not matter (preferable as given in example).

    As is obvious 18 .plt files will be generated (9*2 (1 for delay, 1 for throughput)).

d. For anyfile, the nomenclature clarifies the case. For instance, 
    UdpandTcpHighSpeed_delay_Simulataneous_Different_Start -> Uses TcpHighSpeed, computes delay, starts simultaneously (q2), and has a non-zero offset.

    Here are the 9 commands for easy access:
    Question 1.
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpHighSpeed --loopRuns=30 --simultaneously=0 --offset=0 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpScalable --loopRuns=30 --simultaneously=0 --offset=0 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpVegas --loopRuns=30 --simultaneously=0 --offset=0 --runTime=1 --packetSize=1024"
    Question 2.
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpHighSpeed --loopRuns=30 --simultaneously=1 --offset=0 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpScalable --loopRuns=30 --simultaneously=1 --offset=0 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpVegas --loopRuns=30 --simultaneously=1 --offset=0 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpHighSpeed --loopRuns=30 --simultaneously=1 --offset=3 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpScalable --loopRuns=30 --simultaneously=1 --offset=3 --runTime=1 --packetSize=1024"
    $ ./waf --run "scratch/main-app6 --tcpProtocol=TcpVegas --loopRuns=30 --simultaneously=1 --offset=3 --runTime=1 --packetSize=1024"

e. Total of 18 .plt files will be generated. For each .plt file the corresponding .pdf file is simply obtained by running :
    $ gnuplot x.plt 
    where x is a file name.

