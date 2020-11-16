#include <bits/stdc++.h>                    // needed for C++ standard libraries
#include <ns3/core-module.h>                // core module holds Time, Scheduler, Simulator and other classes
#include <ns3/network-module.h>             // network module has has several network APIs
#include <ns3/point-to-point-module.h>      // needed for creating point-to-point links between nodes
#include <ns3/flow-monitor-module.h>        // flow-monitors collect and store data of a simulation
#include <ns3/gnuplot.h>                    // helps in plotting the graphs
#include <ns3/ipv4-global-routing-helper.h> // manages Ipv4 routing
#include <ns3/applications-module.h>        // has BulkSendApplications, UdpClientServer, UdpEcho
#include <ns3/internet-module.h>            // has Ipv4 Helper Classes, TCP, UDP and other modules
using namespace std;
using namespace ns3;

// constants
double ERROR = 0.000001;

// debug strings
const string MAX_BYTES = "Maximum number of bytes the application can send";
const string TCP_PROTOCOL = "TCP agent type to use at H2 : TcpHighSpeed, TcpVegas, TcpScalable";
const string PACKET_SIZE = "Packet size in bytes";
const string SIMULTANEOUSLY = "Simultaneously start flows for TCP and UDP";
const string RUN_TIME = "Run time as a factor of 5s";
const string OFFSET = "Offset for different time intervlals";
const string LOOP_RUNS = "Number of for loop runs";

// fucntion definitions
void flowMonCalc(map<FlowId, FlowMonitor::FlowStats>::const_iterator);
void printValuesFromCmd(uint, string);
void makeGNUPltFiles(bool, uint, string, Gnuplot2dDataset, Gnuplot2dDataset, Gnuplot2dDataset, Gnuplot2dDataset);

