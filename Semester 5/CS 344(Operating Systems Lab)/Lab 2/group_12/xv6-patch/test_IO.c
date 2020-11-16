#include "types.h"
#include "stat.h"
#include "user.h"
#include "processInfo.h"

// I/O bound
void delayIO(char* str){
    for(int i=0;i<100;++i){
        printf(1,"%s\n",str);
    }
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf(1, "test-case <number-of-children>\n");
        exit();
    }
    int N = atoi(argv[1]);
    char* str = (char*)malloc(500);
    for(int i=0;i<500;++i)
        str[i] = 'l';
    str[500-1] = '\0';
    int pids[N];
    int rets[N];
    int burstTimes[N];
    set_burst_time(2);
    printf(1,"Increasing burst times for I/O bound proccess\n");
    printf(1, "Burst times of parent process = %d\n", get_burst_time());
    
    for (int i = 0; i < N; i++)
    {
        int burst_time = i+3;

        int ret = fork();
        if (ret == 0)
        {
            
            set_burst_time(burst_time);
            delayIO(str);
            exit();
        }
        else if (ret > 0)
        {
            pids[i] = ret;
            burstTimes[i] = burst_time;
        }
        else
        {
            printf(1, "fork error \n");
            exit();
        }
    }

    for (int i = 0; i < N; i++)
    {
        rets[i] = wait();
    }

    printf(1, "\nAll children completed\n");
    for (int i = 0; i < N; i++)
        printf(1, "Child %d.    pid %d    burst time = %d\n", i, pids[i],burstTimes[i]);

    printf(1, "\nExit order \n");
    for (int i = 0; i < N; i++)
        printf(1, "pid %d   burst time = %d\n", rets[i],burstTimes[rets[i]-4]);

    exit();
}