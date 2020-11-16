/*
    CS 342: Networks Lab (Sept-Nov 2020), IIT Guwahati
    Assignment-04
    Group-49

    Students:
    180123062 - AB Satyaprakash
    180123050 - Tanmay Jain

    Application #6
    The objective is to compare the effect of CBR traffic over UDP agent and FTP traffic over TCP agent. Consider a
    TCP agent from TCP HighSpeed, TCP Vegas and TCP Scalable for the FTP traffic. Consider a Dumbbell topology
    with two routers R1 and R2 connected by a wired link (30 Mbps, 100 ms), and use drop-tail queues with queue
    size set according to bandwidth-delay product of the link. Each of the routers is connected to 2 hosts, i.e. H1, H2
    are connected to R1, and H3, H4 are connected to R2. The hosts are attached to the routers with (80 Mbps,
    20ms) links. The CBR traffic over UDP agent and FTP traffic over TCP agent are attached to H1 and H2
    respectively. Choose appropriate packet size for your experiments and perform the following:

    1. Compare the delay (in ms) and throughput (in Kbps) of CBR and FTP traffic streams when only one of
    them is present in the network. Plot the graphs for the delay (in ms) and throughput (in Kbps) observed
    with different packet sizes.

    2. Start both the flows at the same time and also at different times. Also, compare the delay (in ms) and
    throughput (in Kbps) of CBR and FTP traffic streams. Plot the graphs for the delay (in ms) and
    throughput (in Kbps) observed with different packet sizes.

*/

/*
    Network Topology  - A Dumbell topology with 2 routers R1, R2 and 4 hosts H1, H2, H3 and H4.
                        The (n1,n2) for the links repsresents - (Data Rate (in Mbps), Delay (in ms))


                                               (80 Mbps, 20ms)
                                H1            |               |           H3
                                 \            |               |           /
                                  \-----------                -----------/
                                   \                                    /
                                    \        (30 Mbps, 100 ms)         /
                                     R1 ---------------------------- R2
                                    /                                  \
                                   /                                    \
                                  /-----------                -----------\
                                 /            |               |           \
                                H2            |               |           H4
                                               (80 Mbps, 20ms)
*/

/*****************************************Code begins below********************************************/

// include the header files needed for the program to run. The functionalities are explained by their side.
// These includes are for C++
#include <fstream>       // to perform file processing in C++
#include <bits/stdc++.h> // include all standard libraries in C++

// These includes are for ns3
#include <ns3/core-module.h>                // core module holds Time, Scheduler, Simulator and other classes
#include <ns3/network-module.h>             // network module has has several network APIs
#include <ns3/point-to-point-module.h>      // needed for creating point-to-point links between nodes
#include <ns3/flow-monitor-module.h>        // flow-monitors collect and store data of a simulation
#include <ns3/gnuplot.h>                    // helps in plotting the graphs
#include <ns3/ipv4-global-routing-helper.h> // manages Ipv4 routing
#include <ns3/applications-module.h>        // has BulkSendApplications, UdpClientServer, UdpEcho
#include <ns3/internet-module.h>            // has Ipv4 Helper Classes, TCP, UDP and other modules

// These are includes for this file
#include "main-app6.h"

using namespace std;
using namespace ns3;

NS_LOG_COMPONENT_DEFINE("Main-App6");

void flowMonCalc(map<FlowId, FlowMonitor::FlowStats>::const_iterator i)
{
    cout << "Tx Packets: " << i->second.txPackets << "\n";
    cout << "Tx Bytes:" << i->second.txBytes << "\n";
    cout << "Rx Packets: " << i->second.rxPackets << "\n";
    cout << "Rx Bytes:" << i->second.rxBytes << "\n";
    cout << "Net Packet Lost: " << i->second.lostPackets << "\n";
    cout << "Lost due to droppackets: " << i->second.packetsDropped.size() << "\n";
    cout << "Total Delay(in seconds): " << i->second.delaySum.GetSeconds() << endl;
    cout << "Mean Delay(in seconds): " << (double)i->second.delaySum.GetSeconds() / (i->second.rxPackets) << endl;
    cout << "Offered Load: " << (double)i->second.txBytes * 8.0 / (i->second.timeLastTxPacket.GetSeconds() - i->second.timeFirstTxPacket.GetSeconds()) / (double)1000 << " Kbps" << endl;
    cout << "Throughput: " << (double)i->second.rxBytes * 8.0 / (i->second.timeLastRxPacket.GetSeconds() - i->second.timeFirstRxPacket.GetSeconds()) / (double)1000 << " Kbps" << endl;
    cout << "Mean jitter:" << (double)i->second.jitterSum.GetSeconds() / (i->second.rxPackets - 1) << endl;
    cout << endl;
}

void printValuesFromCmd(uint arr[], string tcpProtocol)
{
    cout << "--------------------------------------------------------" << endl;
    cout << "The command line arguments input are:" << endl;
    cout << "maxBytes: " << arr[0] << endl;
    cout << "tcpProtocol: " << tcpProtocol << endl;
    cout << "packetSize: " << arr[1] << endl;
    cout << "simultaneously: " << arr[2] << endl;
    cout << "runTime: " << arr[3] << endl;
    cout << "offset: " << arr[4] << endl;
    cout << "loopRuns: " << arr[5] << endl;
    cout << "--------------------------------------------------------" << endl
         << endl;
}

void makeGNUPltFiles(bool simultaneously, uint offset, string tcpProtocol, Gnuplot2dDataset datasetTcpThroughput,
                     Gnuplot2dDataset datasetTcpDelay, Gnuplot2dDataset datasetUdpThroughput, Gnuplot2dDataset datasetUdpDelay)
{
    /**************************** Plotting with GNU Plot **********************************/
    string simultaneouslyFlag = "Seperate";
    if (simultaneously && offset == 0)
        simultaneouslyFlag = "Simultaneous_Same_Start";
    else if (simultaneously && offset != 0)
        simultaneouslyFlag = "Simultaneous_Different_Start";

    // Construct a readable file name
    string fileNameWithNoExtension = "Udp_and_" + tcpProtocol + "_throughput_" + simultaneouslyFlag;
    string graphicsFileName = fileNameWithNoExtension + ".pdf";
    string plotFileName = fileNameWithNoExtension + ".plt";
    string plotTitle = tcpProtocol + " vs UDP throughput";
    string fileNameWithNoExtensionDelay = "Udp_and_" + tcpProtocol + "_delay_" + simultaneouslyFlag;
    string graphicsFileNameDelay = fileNameWithNoExtensionDelay + ".pdf";
    string plotFileNameDelay = fileNameWithNoExtensionDelay + ".plt";
    string plotTitleDelay = tcpProtocol + " vs UDP delay";

    // Instantiate the plot and set its title.
    Gnuplot plot(graphicsFileName);
    Gnuplot plot_delay(graphicsFileNameDelay);

    plot.SetTitle(plotTitle);
    plot_delay.SetTitle(plotTitleDelay);

    // Make the graphics file, which the plot file will create when it
    // is used with Gnuplot, be a PDF file
    plot.SetTerminal("pdf");
    plot_delay.SetTerminal("pdf");

    // Set the labels for each axis.
    plot.SetLegend("Packet Size(in Bytes)", "Throughput Values(in Kbps)");
    plot_delay.SetLegend("Packet Size(in Bytes)", "Delay(in s)");

    // Instantiate the dataset, set its title, and make the points be
    // plotted along with connecting lines.
    datasetTcpThroughput.SetTitle("Throughput FTP over TCP");
    datasetTcpThroughput.SetStyle(Gnuplot2dDataset::LINES_POINTS);
    datasetTcpThroughput.SetExtra("lw 2");
    datasetUdpThroughput.SetTitle("Throughput CBR over UDP");
    datasetUdpThroughput.SetStyle(Gnuplot2dDataset::LINES_POINTS);
    datasetUdpThroughput.SetExtra("lw 2");

    datasetTcpDelay.SetTitle("Delay FTP over TCP");
    datasetTcpDelay.SetStyle(Gnuplot2dDataset::LINES_POINTS);
    datasetTcpDelay.SetExtra("lw 2");
    datasetUdpDelay.SetTitle("Delay CBR over UDP");
    datasetUdpDelay.SetStyle(Gnuplot2dDataset::LINES_POINTS);
    datasetUdpDelay.SetExtra("lw 2");

    // Add the dataset to the plot.
    plot.AddDataset(datasetTcpThroughput);
    plot.AddDataset(datasetUdpThroughput);

    plot_delay.AddDataset(datasetUdpDelay);
    plot_delay.AddDataset(datasetTcpDelay);

    // Open the plot file.
    ofstream plotFile(plotFileName.c_str());

    // Write the plot file.
    plot.GenerateOutput(plotFile);

    // Close the plot file.
    plotFile.close();

    ofstream plotFile_delay(plotFileNameDelay.c_str());
    plot_delay.GenerateOutput(plotFile_delay);
    plotFile_delay.close();
}

int main(int argc, char *argv[])
{

    // declare and initialise variables to be read from CommandLine
    uint maxBytes = 0;
    string tcpProtocol = "TcpHighSpeed";
    uint packetSize = 1024;
    uint runTime = 1;
    uint offset = 0;
    bool simultaneously = false;
    uint loopRuns = 1;

    CommandLine cmd;
    cmd.AddValue("maxBytes", MAX_BYTES, maxBytes);
    cmd.AddValue("tcpProtocol", TCP_PROTOCOL, tcpProtocol);
    cmd.AddValue("packetSize", PACKET_SIZE, packetSize);
    cmd.AddValue("simultaneously", SIMULTANEOUSLY, simultaneously);
    cmd.AddValue("runTime", RUN_TIME, runTime);
    cmd.AddValue("offset", OFFSET, offset);
    cmd.AddValue("loopRuns", LOOP_RUNS, loopRuns);
    cmd.Parse(argc, argv);

    // store the uint values as an array to send to the function and print!
    uint commandLineArray[] = {maxBytes, packetSize, simultaneously, runTime, offset, loopRuns};

    // print all the values taken from the CommandLine
    printValuesFromCmd(commandLineArray, tcpProtocol);

    if (tcpProtocol == "TcpScalable")
        Config::SetDefault("ns3::TcpL4Protocol::SocketType", TypeIdValue(TcpScalable::GetTypeId()));
    else if (tcpProtocol == "TcpHighSpeed")
        Config::SetDefault("ns3::TcpL4Protocol::SocketType", TypeIdValue(TcpHighSpeed::GetTypeId()));
    else
        Config::SetDefault("ns3::TcpL4Protocol::SocketType", TypeIdValue(TcpVegas::GetTypeId()));

    // Declare portNumber variable for future use
    uint portNumber;

    // Declare datasets for GNU Plot

    Gnuplot2dDataset datasetUdpThroughput;
    Gnuplot2dDataset datasetTcpThroughput;
    Gnuplot2dDataset datasetUdpDelay;
    Gnuplot2dDataset datasetTcpDelay;

    for (uint i = 0; i < loopRuns; i++)
    {

        // assign the same size to udp and tcp packets and increment the size each time.
        uint udpPacketSize, tcpPacketSize;
        udpPacketSize = tcpPacketSize = packetSize + 100 * i;

        //create a node container for 6 nodes (2 routers and 4 hosts)
        // note that n(i)n(j) means that a node container has nodes i and j. For nomenclature see the following diagram.

        /*
                              node 0                                    node 4
                                H1                                        H3
                                 \                                        /
                                  \                                      /
                                   \                                    /
                                    \                                  /
                            node 2  R1 ---------------------------- R2  node 3
                                    /                                  \
                                   /                                    \
                                  /                                      \
                                 /                                        \
                                H2                                        H4
                              node 1                                     node 5                                 
        */

        NodeContainer c;
        c.Create(6);
        NodeContainer n0n2 = NodeContainer(c.Get(0), c.Get(2));
        NodeContainer n1n2 = NodeContainer(c.Get(1), c.Get(2));
        NodeContainer n2n3 = NodeContainer(c.Get(2), c.Get(3));
        NodeContainer n3n4 = NodeContainer(c.Get(3), c.Get(4));
        NodeContainer n3n5 = NodeContainer(c.Get(3), c.Get(5));

        // installing internet stack in all the 6 nodes.
        InternetStackHelper internet;
        internet.Install(c);

        // finding queue sizes per packet
        uint queueSizeHR = (80000 * 20) / (tcpPacketSize * 8);  // 80 Mbps = 80*1000 Mbpms (Megabits per milliseond)
        uint queueSizeRR = (30000 * 100) / (tcpPacketSize * 8); // 30 Mbps = 30*1000 Mbpms (Megabits per milliseond)
        string queueSizeHR2 = to_string(queueSizeHR) + "p";     // convert to string and append 'p'
        string queueSizeRR2 = to_string(queueSizeRR) + "p";     // convert to string and append 'p'

        //point to point helper is used to create point to point links between nodes
        PointToPointHelper point2Point;

        // Now setting up Router to Host Links using point2Point
        // The link has a (80 Mbps, 20 ms) connection
        point2Point.SetDeviceAttribute("DataRate", StringValue("80Mbps"));
        point2Point.SetChannelAttribute("Delay", StringValue("20ms"));
        point2Point.SetQueue("ns3::DropTailQueue<Packet>", "MaxSize", QueueSizeValue(QueueSize(queueSizeHR2)));

        NetDeviceContainer d0d2 = point2Point.Install(n0n2);
        NetDeviceContainer d1d2 = point2Point.Install(n1n2);
        NetDeviceContainer d3d4 = point2Point.Install(n3n4);
        NetDeviceContainer d3d5 = point2Point.Install(n3n5);

        // Now setting up Router to Router Links using point2Point
        // The link has a (30 Mbps, 100 ms) connection
        point2Point.SetDeviceAttribute("DataRate", StringValue("30Mbps"));
        point2Point.SetChannelAttribute("Delay", StringValue("100ms"));
        point2Point.SetQueue("ns3::DropTailQueue<Packet>", "MaxSize", QueueSizeValue(QueueSize(queueSizeRR2)));

        NetDeviceContainer d2d3 = point2Point.Install(n2n3);

        // Making the error model for the Destinations H3 and H4
        Ptr<RateErrorModel> em = CreateObject<RateErrorModel>();
        em->SetAttribute("ErrorRate", DoubleValue(ERROR)); // constant ERROR was defined using #define on line 67
        d3d4.Get(1)->SetAttribute("ReceiveErrorModel", PointerValue(em));
        d3d5.Get(1)->SetAttribute("ReceiveErrorModel", PointerValue(em));

        // Assigning IP to the NetDeviceContainers having 2 nodes each
        // SetBase function, sets ip and subnet mask
        Ipv4AddressHelper ipv4;
        ipv4.SetBase("10.1.0.0", "255.255.255.0");
        Ipv4InterfaceContainer i0i2 = ipv4.Assign(d0d2);

        ipv4.SetBase("10.1.1.0", "255.255.255.0");
        Ipv4InterfaceContainer i1i2 = ipv4.Assign(d1d2);

        ipv4.SetBase("10.1.3.0", "255.255.255.0");
        Ipv4InterfaceContainer i2i3 = ipv4.Assign(d2d3);

        ipv4.SetBase("10.1.4.0", "255.255.255.0");
        Ipv4InterfaceContainer i3i4 = ipv4.Assign(d3d4);

        ipv4.SetBase("10.1.5.0", "255.255.255.0");
        Ipv4InterfaceContainer i3i5 = ipv4.Assign(d3d5);

        // Routing Tables
        Ipv4GlobalRoutingHelper::PopulateRoutingTables();

        // Print all the IP addresses
        cout << "The IP addresses assigned to Senders:" << endl;
        cout << "H1: " << i0i2.GetAddress(0) << endl;
        cout << "H2: " << i1i2.GetAddress(0) << endl;

        cout << "The IP addresses assigned to Recievers:" << endl;
        cout << "H3: " << i3i4.GetAddress(1) << endl;
        cout << "H4: " << i3i5.GetAddress(1) << endl;

        cout << "The IP addresses assigned to Routers:" << endl;
        // R1 and sender hosts
        cout << "R1<--H1: " << i0i2.GetAddress(1) << endl;
        cout << "R1<--H2: " << i1i2.GetAddress(1) << endl;
        // R2 and receiver hosts
        cout << "R2<--H3: " << i3i4.GetAddress(0) << endl;
        cout << "R2<--H4: " << i3i5.GetAddress(0) << endl;
        // R1 and R2
        cout << "R1<--R2: " << i2i3.GetAddress(0) << endl;
        cout << "R1-->R2: " << i2i3.GetAddress(1) << endl;
        cout << endl;

        //printing routing tables for the all the nodes in the container
        Ipv4GlobalRoutingHelper g;
        Ptr<OutputStreamWrapper> routingStream = Create<OutputStreamWrapper>("routing.routes", ios::out);
        g.PrintRoutingTableAllAt(Seconds(2), routingStream);

        /**************************** CBR Traffic on UDP **********************************/
        portNumber = 9;

        // on off helper is for the CBR traffic, we tell INET socket address here that receiver is HOST-3
        OnOffHelper onoff("ns3::UdpSocketFactory", Address(InetSocketAddress(i3i4.GetAddress(1), portNumber)));
        onoff.SetAttribute("PacketSize", UintegerValue(udpPacketSize));

        // install the on off app on HOST-1 and run for 1-5 seconds
        ApplicationContainer udpAppsSource = onoff.Install(n0n2.Get(0));

        // runtime =  (total time of simulation in multiple of 10 for given packet size)
        // i = for loop counter(packet size is increasing after every loop iteration)
        if (simultaneously == false)
        {
            udpAppsSource.Start(Seconds((0.0 + (10 * i)) * runTime));
            udpAppsSource.Stop(Seconds((5.0 + (10 * i)) * runTime));
        }
        else
        {
            udpAppsSource.Start(Seconds((0.0 + (10 * i)) * runTime));
            udpAppsSource.Stop(Seconds((10.0 + (10 * i)) * runTime));
        }

        // Create a packet sink to receive these packets from any ip address.
        PacketSinkHelper sinkUdp("ns3::UdpSocketFactory", Address(InetSocketAddress(Ipv4Address::GetAny(), portNumber)));

        // install the reciver at HOST-3
        ApplicationContainer udpAppsDest = sinkUdp.Install(n3n4.Get(1));

        if (simultaneously == false)
        {
            udpAppsDest.Start(Seconds((0.0 + (10 * i)) * runTime));
            udpAppsDest.Stop(Seconds((5.0 + (10 * i)) * runTime));
        }
        else
        {
            udpAppsDest.Start(Seconds((0.0 + (10 * i)) * runTime));
            udpAppsDest.Stop(Seconds((10.0 + (10 * i)) * runTime));
        }

        /**************************** FTP Traffic on TCP **********************************/

        // portNumber = 12344;
        portNumber = 13356;
        BulkSendHelper source("ns3::TcpSocketFactory", InetSocketAddress(i3i5.GetAddress(1), portNumber));

        // Set the amount of data to send in bytes.  Zero => unlimited.
        source.SetAttribute("MaxBytes", UintegerValue(maxBytes));
        source.SetAttribute("SendSize", UintegerValue(tcpPacketSize));
        ApplicationContainer tcpAppsSource = source.Install(n1n2.Get(0));

        if (simultaneously == false)
        {
            tcpAppsSource.Start(Seconds((5.0 + (10 * i)) * runTime));
            tcpAppsSource.Stop(Seconds((10.0 + (10 * i)) * runTime));
        }
        else
        {
            tcpAppsSource.Start(Seconds((0.0 + (10 * i)) * runTime));
            tcpAppsSource.Stop(Seconds((10.0 + (10 * i)) * runTime));
        }

        // Create a PacketSinkApplication and install it on HOST-4
        PacketSinkHelper sink_tcp("ns3::TcpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), portNumber));
        ApplicationContainer tcpAppsDest = sink_tcp.Install(n3n5.Get(1));

        if (simultaneously == false)
        {
            tcpAppsDest.Start(Seconds((5.0 + (10 * i)) * runTime));
            tcpAppsDest.Stop(Seconds((10.0 + (10 * i)) * runTime));
        }
        else
        {
            tcpAppsDest.Start(Seconds((0.0 + (10 * i)) * runTime + offset));
            tcpAppsDest.Stop(Seconds((10.0 + (10 * i)) * runTime + offset));
        }

        /**************************** Logging of all PARAMETERS **********************************/

        Ptr<FlowMonitor> flowMon;
        FlowMonitorHelper flowMonHelper;
        flowMon = flowMonHelper.InstallAll();
        if (!simultaneously)
            Simulator::Stop(Seconds((10 + (10 * i)) * runTime));
        else
            Simulator::Stop(Seconds((10 + (10 * i)) * runTime + offset));
        // runs the Simulator
        Simulator::Run();
        flowMon->CheckForLostPackets();

        Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier>(flowMonHelper.GetClassifier());
        //Retrieving the flow montor stats for different flows
        map<FlowId, FlowMonitor::FlowStats> stats = flowMon->GetFlowStats();

        double throughput_udp;
        double throughput_tcp;
        double delay_udp;
        double delay_tcp;

        for (map<FlowId, FlowMonitor::FlowStats>::const_iterator i = stats.begin(); i != stats.end(); ++i)
        {
            Ipv4FlowClassifier::FiveTuple t = classifier->FindFlow(i->first);
            cout << "Flow: " << i->first << "\n";
            cout << "Source: " << t.sourceAddress << "\n";
            cout << "Destination: " << t.destinationAddress << "\n";

            if (t.sourceAddress == "10.1.0.1") // for UDP
            {
                //UDP FLOW
                throughput_udp = (double)i->second.rxBytes * 8.0 / (i->second.timeLastRxPacket.GetSeconds() - i->second.timeFirstRxPacket.GetSeconds()) / (double)1000;
                delay_udp = (double)i->second.delaySum.GetSeconds() / (i->second.rxPackets);

                datasetUdpThroughput.Add(udpPacketSize, throughput_udp);
                datasetUdpDelay.Add(udpPacketSize, delay_udp);

                cout << "UDP Flow over CBR " << i->first << " (" << t.sourceAddress << " -> " << t.destinationAddress << ")\n";
                flowMonCalc(i);
            }
            else if (t.sourceAddress == "10.1.1.1") // for TCP
            {
                //TCP FLOW
                throughput_tcp = (double)i->second.rxBytes * 8.0 / (i->second.timeLastRxPacket.GetSeconds() - i->second.timeFirstRxPacket.GetSeconds()) / 1000;
                delay_tcp = (double)i->second.delaySum.GetSeconds() / (i->second.rxPackets);

                datasetTcpThroughput.Add(tcpPacketSize, throughput_tcp);
                datasetTcpDelay.Add(tcpPacketSize, delay_tcp);

                cout << tcpProtocol << " Flow over FTP " << i->first << " (" << t.sourceAddress << " -> " << t.destinationAddress << ")\n";
                flowMonCalc(i);
            }
        }

        cout << "Finished Loop Run Number: " << i << endl
             << endl;
        cout << "--------------------------------------------------------" << endl
             << endl;
        // destorys the simulator
        Simulator::Destroy();
    }

    // Make the plt files, to make the pdf files using GNUPLOT
    makeGNUPltFiles(simultaneously, offset, tcpProtocol, datasetTcpThroughput, datasetTcpDelay, datasetUdpThroughput, datasetUdpDelay);
    return 0;

    /***********************************End of Assignment Code**********************************/
}
