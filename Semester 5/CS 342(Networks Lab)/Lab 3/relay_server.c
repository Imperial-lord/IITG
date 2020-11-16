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
const char *REQUEST_NODE = "REQUEST : node";
const char *CLOSING_CONNECTION = "Gracefully closing the connection with the server";
const char *UNKNOWN_RESPONSE = "Received some incomprehensible message from the server!";
const char *PROPER_CMD_ARGS = "Please enter the args as <executable code><Server Port number>";
const char *SERVER_STARTED = "Server started and listening for connections...";
const char *CLIENT_PORT = "The client will listen on port:";
const char *UNABLE_ADDRESS = "Unable to specify an address for the client";
const char *RESPONSE_FOR_NODE = "RESPONSE : Node: 1,";
const char *RESPONSE_FOR_CLIENT = "RESPONSE : client: 1,";
const char *RESPONSE_FOR_PEERINFO = "REQUEST : peer info";
const char *TEXT_DETAILS = "The server has the received information from the peerNodes.\nHere is the Info received by the server:";

/*______________________error messages______________________________*/
const char *ERROR_WRITING_TO_SOCKET = "Error writing to the socket";
const char *ERROR_READING_FROM_SOCKET = "Error reading from the socket";
const char *ERROR_OPENING_CONNECTION = "Error opening connection with the socket";
const char *IMPROPER_CMD_ARGS = "You have entered the command line arguments in a wrong format";
const char *ERROR_ON_BINDING = "Error while 'binding' the relay server";
const char *ERROR_ON_ACCEPT = "Error caused on accepting the incoming client";
const char *ERROR_ON_FORK = "Error was encountered while creating a child process!";

/*____________________global_buffers for messages_____________________*/
char client_response_buffer[MAX_SIZE] = {0}; // declares a buffer to store client response and clears it!
char temp_buffer[MAX_SIZE] = {0};            // declares a temp_buffer and clears it!

void printErrorMessages(const char *ErroMessage)
{
    perror(ErroMessage);
    exit(1);
}

int main(int argc, char *argv[]) //Server Prototype : <executable code><Server Port number>
{
    if (argc != 2)
    {
        printf("%s\n%s", IMPROPER_CMD_ARGS, PROPER_CMD_ARGS);
        exit(0);
    }

    int sock_FD, newSock_FD, portNumber, flag, processID, clientLength;
    struct sockaddr_in serverAddress = {0}, clientAddress = {0};

    FILE *serverNodeInfo = fopen("nodeinfo_server.txt", "w");
    fclose(serverNodeInfo);

    portNumber = atoi(argv[1]);

    sock_FD = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_FD < 0)
    {
        printErrorMessages(ERROR_OPENING_CONNECTION);
    }

    serverAddress.sin_family = AF_INET;         // define the server address and family
    serverAddress.sin_addr.s_addr = INADDR_ANY; // basically refers to 0.0.0.0
    serverAddress.sin_port = htons(portNumber);

    flag = bind(sock_FD, (struct sockaddr *)&serverAddress, sizeof(serverAddress)); // connect with the node server

    if (flag < 0)
    {
        printErrorMessages(ERROR_ON_BINDING);
    }

    listen(sock_FD, 5); // listen for connections
    clientLength = sizeof(clientAddress);
    printf("%s\n", SERVER_STARTED);

    for (;;) // keep waiting for connections
    {
        newSock_FD = accept(sock_FD, (struct sockaddr *)&clientAddress, (socklen_t *)&clientLength);
        if (newSock_FD < 0)
        {
            printErrorMessages(ERROR_ON_ACCEPT);
        }

        processID = fork();
        if (processID < 0)
        {
            printErrorMessages(ERROR_ON_FORK);
        }

        else if (processID == 0) // this is the case where client process starts
        {
            close(sock_FD);
            int clientType = 0; // represents a random client type
            int portNumber = ntohs(clientAddress.sin_port) + 200;

            flag = read(newSock_FD, client_response_buffer, MAX_SIZE - 1);
            if (flag < 0)
            {
                printErrorMessages(ERROR_READING_FROM_SOCKET);
            }
            if (strcmp(client_response_buffer, REQUEST_NODE) == 0)
                clientType = 1;
            else if (strcmp(client_response_buffer, REQUEST_CLIENT) == 0)
                clientType = 2;

            printf("%s\n", client_response_buffer);

            if (clientType == 1)
            {
                //______________________for peer-nodes_______________________________
                printf("%s %d\n", CLIENT_PORT, portNumber);
                char clientName[INET_ADDRSTRLEN];
                if (inet_ntop(AF_INET, &clientAddress.sin_addr.s_addr, clientName, sizeof(clientName)) != NULL)
                {
                    serverNodeInfo = fopen("nodeinfo_server.txt", "a+");
                    fprintf(serverNodeInfo, "%s%c%d\n", clientName, ' ', portNumber);
                    fclose(serverNodeInfo);
                }
                else
                {
                    printf("%s\n", UNABLE_ADDRESS);
                }

                sprintf(temp_buffer, "%s %d", RESPONSE_FOR_NODE, portNumber);
                flag = write(newSock_FD, temp_buffer, strlen(temp_buffer));
                if (flag < 0)
                {
                    printErrorMessages(ERROR_WRITING_TO_SOCKET);
                }
            }

            else if (clientType == 2)
            {
                flag = write(newSock_FD, RESPONSE_FOR_CLIENT, strlen(RESPONSE_FOR_CLIENT));

                flag = read(newSock_FD, client_response_buffer, 255);
                if (flag < 0)
                {
                    printErrorMessages(ERROR_READING_FROM_SOCKET);
                }

                printf("%s\n", client_response_buffer); // message received from client
                if (strcmp(client_response_buffer, RESPONSE_FOR_PEERINFO) == 0)
                {
                    //read the file that stored the peer info
                    serverNodeInfo = fopen("nodeinfo_server.txt", "rb");
                    fseek(serverNodeInfo, 0, SEEK_END);
                    long serverNodeInfoSize = ftell(serverNodeInfo);
                    fseek(serverNodeInfo, 0, SEEK_SET); //send the pointer to beginning of the file

                    char *textInFile = malloc(serverNodeInfoSize + 1);
                    fread(textInFile, serverNodeInfoSize, 1, serverNodeInfo);
                    fclose(serverNodeInfo);

                    textInFile[serverNodeInfoSize] = 0;
                    printf("%s\n%s", TEXT_DETAILS, textInFile);

                    flag = write(newSock_FD, textInFile, strlen(textInFile)); //send this info to client
                    if (flag < 0)
                    {
                        printErrorMessages(ERROR_WRITING_TO_SOCKET);
                    }
                }
            }
            else
            {
                printf("%s\n", UNKNOWN_RESPONSE);
            }
            exit(0);
        }
        else
        {
            fprintf(stderr, "%s\n", CLOSING_CONNECTION);
            close(newSock_FD);
        }
    }

    return 0;
}
