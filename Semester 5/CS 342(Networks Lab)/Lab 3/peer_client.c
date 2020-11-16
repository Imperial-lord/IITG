// includes needed for C programming
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include <sys/socket.h> // defines symbolic constants (like SOCK_STREAM)
#include <netdb.h>      // defines the hostent structure
#include <netinet/in.h> // defines cetain specific types and macros
#include <arpa/inet.h>

#define MAX_SIZE 256 // defines the global buffer size

/*_________________________constants/messages_____________________________*/
const char *REQUEST_PEER_INFO = "REQUEST : peer info";
const char *REQUEST_CLIENT = "REQUEST : client";
const char *RESPONSE_RECEIVED = "Recieved the following response from the server";
const char *CLOSING_CONNECTION = "Gracefully closing the connection with the server";
const char *PROMPT_USER_FOR_FILENAME = "Enter the file name you want to look for:";
const char *CONNECT_TO_NODE = "Now connecting to PeerNode with Info:";
const char *FILE_NOT_FOUND_ON_NODES = "Sorry :( ! The requested file was not found with any peerNode";
const char *SUCCESSFUL_CONNECTION_TO_PEER = "Connection to peer node successful!\nSending a file transfer request.";
const char *CONNECTING_TO_RELAY = "Connecting to relay server... Sending message request...";
const char *CLIENT_ACCEPTED = "RESPSONSE : client accepted\nSuccesfully connected to Relay_Server\nNow getting peer info";
const char *CLIENT_DENIED = "RESPSONSE : client denied\nPlease try connecting to the relay server again!";
const char *UNKNOWN_RESPONSE = "Received some incomprehensible message from the server!";
const char *FILE_HAS_CONTENT = "The file requested for has the content as follows:";
const char *PROPER_CMD_ARGS = "Please enter the args as <executable code><Server IP Address><Server Port number>";

/*______________________error messages______________________________*/
const char *ERROR_WRITING_TO_SOCKET = "Error writing to the socket";
const char *ERROR_READING_FROM_SOCKET = "Error reading from the socket";
const char *ERROR_OPENING_CONNECTION = "Error opening connection with the socket";
const char *ERROR_CLOSING_CONNECTION = "Error closing connection with the socket";
const char *ERROR_CONNECTING_TO_SOCKET = "Error connecting to the socket";
const char *ERROR_HOST_NOT_FOUND = "Error no such host found";
const char *ERROR_FILE_NOT_RECEIVED = "Error in getting the files from the peer nodes";
const char *IMPROPER_CMD_ARGS = "You have entered the command line arguments in a wrong format";

/*____________________global_buffers for messages_____________________*/
char relay_server_response_buffer[MAX_SIZE] = {0}; // declares a buffer to store relay-server response and clears it!
char peernode_response_buffer[MAX_SIZE] = {0};     // declares a buffer to store peernode response and clears it!
char connect_relay_server_buffer[MAX_SIZE] = {0};

void printErrorMessages(const char *ErroMessage)
{
    perror(ErroMessage);
    exit(1);
}

int connectWithPeerNodes(char *nodeIPAddress, int portNumber, char *fileName)
{
    int flag; // this will help track if an action is successful
    int sock_FD;
    struct sockaddr_in serverAddress = {0};
    struct hostent *server;
    struct in_addr ipAddress;

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(portNumber);

    sock_FD = socket(AF_INET, SOCK_STREAM, 0); // here 0 means using the TCP protocol
    if (sock_FD < 0)
    {
        printErrorMessages(ERROR_OPENING_CONNECTION);
    }

    inet_pton(AF_INET, nodeIPAddress, &ipAddress);
    server = gethostbyaddr(&ipAddress, sizeof(ipAddress), AF_INET); // using the nodeIPAddress and getting the node (now acting as a server)

    if (server == NULL)
    {
        fprintf(stderr, "%s", ERROR_HOST_NOT_FOUND);
        exit(0);
    }
    // copy the contents from server address list to serverAddress.sin_addr.s_addr
    memcpy((char *)server->h_addr_list[0], (char *)&serverAddress.sin_addr.s_addr, server->h_length);

    flag = connect(sock_FD, (struct sockaddr *)&serverAddress, sizeof(serverAddress)); // connect with the node server

    if (flag < 0)
    {
        printErrorMessages(ERROR_CONNECTING_TO_SOCKET);
    }

    printf("%s\n", SUCCESSFUL_CONNECTION_TO_PEER);
    char req[MAX_SIZE];
    char *message = "REQUEST : FILE :";
    sprintf(req, "%s %s", message, fileName); // save the contents in req

    flag = write(sock_FD, req, strlen(req)); // send message to peer node server
    if (flag < 0)
    {
        printErrorMessages(ERROR_WRITING_TO_SOCKET);
    }

    memset(peernode_response_buffer, 0, sizeof(peernode_response_buffer));
    flag = read(sock_FD, peernode_response_buffer, MAX_SIZE - 1);
    if (flag < 0)
    {
        printErrorMessages(ERROR_READING_FROM_SOCKET);
    }

    printf("%s\n%s\n", RESPONSE_RECEIVED, peernode_response_buffer);

    if (strcmp(peernode_response_buffer, "File FOUND") == 0)
    {
        // in this case we have found the file
        char fileContent[MAX_SIZE] = {0}; // ASSUMPTION : file has less than 256 characters in total!
        flag = read(sock_FD, fileContent, MAX_SIZE - 1);
        if (flag < 0)
        {
            printErrorMessages(ERROR_READING_FROM_SOCKET);
        }

        printf("%s\n\n%s\n", FILE_HAS_CONTENT, fileContent);
        printf("%s\n", CLOSING_CONNECTION);
        flag = shutdown(sock_FD, 0); // gracefully close connection as file is not found!
        if (flag < 0)
        {
            printErrorMessages(ERROR_CLOSING_CONNECTION);
        }

        return 0; // return 0 to mark the flag=1 in the getFileFromNodes() function!
    }
    else if (strcmp(peernode_response_buffer, "File NOT FOUND") == 0)
    {
        printf("%s\n", CLOSING_CONNECTION);
        flag = shutdown(sock_FD, 0); // gracefully close connection as file is not found!
        if (flag < 0)
        {
            printErrorMessages(ERROR_CLOSING_CONNECTION);
        }
    }
    else
    {
        printf("%s\n", UNKNOWN_RESPONSE);
    }

    return -1;
}

int getFileFromNodes() // connect to all nodes and see if we can find the required file
{
    int flag; // this will help track if an action is successful
    printf("%s ", PROMPT_USER_FOR_FILENAME);
    char fileName[MAX_SIZE]; // stores the filename entered by user in terminal
    scanf("%s", fileName);

    bool found = false;
    char nodeIPAddress[INET_ADDRSTRLEN]; // will store the peer IP
    int portNumber;                      // will store the peer port number

    FILE *nodeInfoFile = fopen("nodesinfo.txt", "r");
    while (fscanf(nodeInfoFile, "%s %d", nodeIPAddress, &portNumber) != EOF) // parse till end of file
    {
        printf("%s %s %d\n", CONNECT_TO_NODE, nodeIPAddress, portNumber);
        flag = connectWithPeerNodes(nodeIPAddress, portNumber, fileName); // connect with the peerNodes and request for "fileName"
        if (flag < 0)
        {
            continue;
        }
        else
        {
            found = true; // found the required file with a peerNode
            break;
        }
    }

    if (found == false) // the required file was not found on any node
    {
        printf("%s", FILE_NOT_FOUND_ON_NODES);
    }

    return 0;
}

int getInfoOfNodes(int sock_FD) // gets the info (IP and Port) of active peer-nodes from the relay-server
{
    int flag; // this will help track if an action is successful

    flag = write(sock_FD, REQUEST_PEER_INFO, strlen(REQUEST_PEER_INFO)); //send message to the server
    if (flag < 0)
    {
        printErrorMessages(ERROR_WRITING_TO_SOCKET);
    }

    flag = read(sock_FD, relay_server_response_buffer, MAX_SIZE - 1); //read response from the server
    if (flag < 0)
    {
        printErrorMessages(ERROR_READING_FROM_SOCKET);
    }

    printf("%s\n%s\n\n", RESPONSE_RECEIVED, relay_server_response_buffer);
    printf("%s\n", CLOSING_CONNECTION);
    flag = shutdown(sock_FD, 0); // close the connection gracefully

    if (flag < 0)
    {
        printErrorMessages(ERROR_CLOSING_CONNECTION);
    }

    /*
        From here onwards we store the information in a file and then use it later for
        taking the IP and Port Number of each Peer Node and pinging them individually 
        requesting for the file name (later in getFileFromPeer function)
    */
    FILE *nodeInfoFile = fopen("nodesinfo.txt", "w"); // open a file in writable mode
    fprintf(nodeInfoFile, "%s", relay_server_response_buffer);
    fclose(nodeInfoFile);

    flag = getFileFromNodes(); // connect to all nodes and see if we can find the required file
    if (flag < 0)
    {
        printf("%s", ERROR_CONNECTING_TO_SOCKET);
    }

    return 0;
}

int main(int argc, char *argv[]) //Client Prototype : <executable code><Server IP Address><Server Port number>
{
    if (argc != 3)
    {
        printf("%s\n%s", IMPROPER_CMD_ARGS, PROPER_CMD_ARGS);
        exit(0);
    }

    int sock_FD, portNumber, flag;
    struct sockaddr_in serverAddress = {0};
    struct hostent *server;

    server = gethostbyname(argv[1]);
    portNumber = atoi(argv[2]);

    sock_FD = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_FD < 0)
    {
        printErrorMessages(ERROR_OPENING_CONNECTION);
    }

    if (server == NULL)
    {
        fprintf(stderr, "%s", ERROR_HOST_NOT_FOUND);
        exit(0);
    }

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(portNumber);
    // copy the contents from server address list to serverAddress.sin_addr.s_addr
    memcpy((char *)server->h_addr_list[0], (char *)&serverAddress.sin_addr.s_addr, server->h_length);

    flag = connect(sock_FD, (struct sockaddr *)&serverAddress, sizeof(serverAddress)); // connect with the node server

    if (flag < 0)
    {
        printErrorMessages(ERROR_CONNECTING_TO_SOCKET);
    }

    printf("%s\n", CONNECTING_TO_RELAY);

    flag = write(sock_FD, REQUEST_CLIENT, strlen(REQUEST_CLIENT)); // send message to server
    if (flag < 0)
    {
        printErrorMessages(ERROR_WRITING_TO_SOCKET);
    }

    flag = read(sock_FD, connect_relay_server_buffer, MAX_SIZE - 1);
    if (flag < 0)
    {
        printErrorMessages(ERROR_READING_FROM_SOCKET);
    }

    printf("%s\n", connect_relay_server_buffer);
    if (connect_relay_server_buffer[19] == '1')
    {
        printf("%s\n", CLIENT_ACCEPTED);
        flag = getInfoOfNodes(sock_FD);

        if (flag < 0)
        {
            printErrorMessages(ERROR_FILE_NOT_RECEIVED);
        }
    }
    else
    {
        printf("%s\n", CLIENT_DENIED);
    }

    return 0;
}
