#include "types.h"
#include "stat.h"
#include "user.h"
#include "processInfo.h"

// CPU bound
void delay()
{
    int* data = (int*)malloc(1000*sizeof(int));

    for(int i=0;i<1000;++i)
        data[i] = 0;

    for(int j=0;j<1000;j++)
        data[j]++;
}


int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf(1, "test-case <number-of-children>\n");
        exit();
    }
    int N = atoi(argv[1]);

    int pids[N];
    int rets[N];
    int burstTimes[N];
    set_burst_time(2);
    printf(1,"Decreasing burst times\n");
    printf(1, "Burst times of parent process = %d\n", get_burst_time());
    for (int i = 0; i < N; i++)
    {
        
        int burst_time = 20-i;

        int ret = fork();
        if (ret == 0)
        {
            
            set_burst_time(burst_time);
            delay();
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
        // struct processInfo info;
	    // getProcInfo(rets[i],&info);
	    // printf(1,"burstTime= %d  pid = %d  context=%d \n",burstTimes[i],rets[i],info.numberContextSwitches);
    }

    printf(1, "\nAll children completed\n");
    for (int i = 0; i < N; i++)
        printf(1, "Child %d.    pid %d    burst time = %d\n", i, pids[i],burstTimes[i]);

    printf(1, "\nExit order \n");
    for (int i = 0; i < N; i++)
        printf(1, "pid %d   burst time = %d\n", rets[i],burstTimes[rets[i]-4]);

    exit();
}
