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
const char *REQUEST_NODE = "REQUEST : node";
const char *REQUEST_FILE = "REQUEST : FILE : ";
const char *CLOSING_CONNECTION = "Gracefully closing the connection with the server";
const char *PROPER_CMD_ARGS = "Please enter the args as <executable code><Server IP Address><Server Port number>";
const char *SERVER_STARTED = "Server started for Peer Node and listening for connections...";
const char *CLIENT_PORT = "The client will listen on port:";
const char *NODE_ACCEPTED = "RESPSONSE : node accepted\nSuccesfully connected to Relay_Server";
const char *NODE_DENIED = "RESPSONSE : node denied\nPlease try connecting to the relay server again!";
const char *CONNECTING_TO_RELAY = "Connecting to relay server... Sending message request...";
const char *FILE_HAS_CONTENT = "The file requested for has the content as follows:";
const char *NOT_FILE = "Didn't find the requested file!";
const char *FOUND_FILE = "Found the requested file";
const char *PEER_MESSAGE = "Received the following message from peer -";

/*______________________error messages______________________________*/
const char *ERROR_WRITING_TO_SOCKET = "Error writing to the socket";
const char *ERROR_READING_FROM_SOCKET = "Error reading from the socket";
const char *ERROR_OPENING_CONNECTION = "Error opening connection with the socket";
const char *ERROR_HOST_NOT_FOUND = "Error no such host found";
const char *ERROR_CONNECTING_TO_SOCKET = "Error connecting to the socket";
const char *ERROR_CLOSING_CONNECTION = "Error closing connection with the socket";
const char *IMPROPER_CMD_ARGS = "You have entered the command line arguments in a wrong format";
const char *ERROR_ON_BINDING = "Error while 'binding' the relay server";
const char *ERROR_ON_ACCEPT = "Error caused on accepting the incoming client";

/*____________________global_buffers for messages_____________________*/
char start_server_buffer[MAX_SIZE] = {0};          // a cleared buffer for use of peer node while acting as servers (phase 3)
char relay_server_response_buffer[MAX_SIZE] = {0}; // a cleared buffer for peernodes while acting as clients (phase 1)

void printErrorMessages(const char *ErroMessage)
{
    perror(ErroMessage);
    exit(1);
}

int startActingAsServers(char *portNum)
{
    int sock_FD, newSock_FD, portNumber, flag;
    struct sockaddr_in serverAddress = {0}, clientAddress = {0};
    socklen_t clientLength;

    sock_FD = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_FD < 0)
    {
        printErrorMessages(ERROR_OPENING_CONNECTION);
    }

    portNumber = atoi(portNum);
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY;
    serverAddress.sin_port = htons(portNumber);

    flag = bind(sock_FD, (struct sockaddr *)&serverAddress, sizeof(serverAddress));
    if (flag < 0)
    {
        printErrorMessages(ERROR_ON_BINDING);
    }

    listen(sock_FD, 5);
    printf("%s\n", SERVER_STARTED);
    clientLength = sizeof(clientAddress);

    newSock_FD = accept(sock_FD, (struct sockaddr *)&clientAddress, &clientLength);
    if (newSock_FD < 0)
    {
        printErrorMessages(ERROR_ON_ACCEPT);
    }
    close(sock_FD);

    flag = read(newSock_FD, start_server_buffer, MAX_SIZE - 1);
    if (flag < 0)
    {
        printErrorMessages(ERROR_READING_FROM_SOCKET);
    }
    printf("%s\n%s\n", PEER_MESSAGE, start_server_buffer);

    char message[] = "REQUEST : FILE : ";
    bool check = true;
    for (int i = 0; i < strlen(message); i++)
    {
        if (message[i] != start_server_buffer[i])
        {
            check = false;
            break;
        }
    }

    if (check == true)
    {
        printf("The Peer-Server has received request for the following file : %s\n", &start_server_buffer[strlen(message)]);
        FILE *textFile = fopen(&start_server_buffer[strlen(message)], "r");
        if (textFile == NULL)
        {
            printf("%s\n", NOT_FILE);
            char response[] = "File NOT FOUND";
            flag = write(newSock_FD, response, strlen(response));
            if (flag < 0)
            {
                printErrorMessages(ERROR_WRITING_TO_SOCKET);
            }
        }
        else
        {
            printf("%s\n", FOUND_FILE);
            char response[] = "File FOUND";
            flag = write(newSock_FD, response, strlen(response));
            if (flag < 0)
            {
                printErrorMessages(ERROR_WRITING_TO_SOCKET);
            }

            //send the file
            fseek(textFile, 0, SEEK_END);
            long textFileSize = ftell(textFile);
            fseek(textFile, 0, SEEK_SET); //send the pointer to beginning of the file

            char *text = malloc(textFileSize + 1);
            fread(text, textFileSize, 1, textFile);
            fclose(textFile);
            printf("\n%s\n%s", FILE_HAS_CONTENT, text);

            //send the content to client
            flag = write(newSock_FD, text, strlen(text));
            if (flag < 0)
            {
                printErrorMessages(ERROR_WRITING_TO_SOCKET);
            }
        }
    }
    else
    {
        printf("%s\n%s\n", NOT_FILE, CLOSING_CONNECTION);
        close(newSock_FD);
    }
    return 0;
}

int main(int argc, char *argv[]) //PeerNode Prototype : <executable code><Server IP Address><Server Port number>
{
    // here peer nodes are acting as clients for the relay server.. for documentation see peer_client.c
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

    flag = write(sock_FD, REQUEST_NODE, strlen(REQUEST_NODE)); // send message to server
    if (flag < 0)
    {
        printErrorMessages(ERROR_WRITING_TO_SOCKET);
    }

    flag = read(sock_FD, relay_server_response_buffer, MAX_SIZE - 1);
    if (flag < 0)
    {
        printErrorMessages(ERROR_READING_FROM_SOCKET);
    }

    printf("%s\n", relay_server_response_buffer);
    if (relay_server_response_buffer[17] == '1')
    {
        printf("%s\n", NODE_ACCEPTED);
        printf("%s\n", CLOSING_CONNECTION);
        flag = shutdown(sock_FD, 0);
        if (flag < 0)
        {
            printErrorMessages(ERROR_CLOSING_CONNECTION);
        }

        printf("%s %s\n", CLIENT_PORT, &relay_server_response_buffer[20]); //acting as server
        startActingAsServers(&relay_server_response_buffer[20]);
    }
    else
    {
        printf("%s\n", NODE_DENIED);
    }

    return 0;
}
