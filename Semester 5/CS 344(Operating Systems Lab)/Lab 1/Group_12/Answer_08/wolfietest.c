#include "types.h"
#include "stat.h"
#include "user.h"


int main(int argc,char* argv[]){
	int size = atoi(argv[1]);
	char* buff = (char*)malloc(size*sizeof(char));
	int x = wolfie(buff,size);
	printf(1,"%d\n",x);	
	
	if(x != -1){
		for(int i=0;i<x;++i){
			printf(1,"%c",buff[i]);
		}
		printf(1,"\n");
	}
	
	exit();
}
