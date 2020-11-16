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
    printf(1,"Random burst times\n");
    printf(1, "Burst times of parent process = %d\n", get_burst_time());
    int x0 = 3,a = 5,b = 4,m = 17;
    for (int i = 0; i < N; i++)
    {
        x0 = (a*x0+b)%m;

        int ret = fork();
        if (ret == 0)
        {
            // struct processInfo info;
	        // getProcInfo(getpid(),&info);
	        // printf(1,"pid = %d  context=%d \n",getpid(),info.numberContextSwitches);
            
            set_burst_time(x0+3);
            delay();
            // getProcInfo(getpid(),&info);
	        // printf(1,"pid = %d  context=%d \n",getpid(),info.numberContextSwitches); 
            exit();
        }
        else if (ret > 0)
        {
            pids[i] = ret;
            burstTimes[i] = x0+3;
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

    printf(1, "\nAll children executed\n");
    for (int i = 0; i < N; i++)
        printf(1, "Child %d.    pid %d    burst time = %d\n", i, pids[i],burstTimes[i]);

    printf(1, "\nExit order \n");
    for (int i = 0; i < N; i++)
        printf(1, "pid %d   burst time = %d\n", rets[i],burstTimes[rets[i]-4]);

    exit();
}
