// Simple inline assembly example
//
#include <stdio.h>
int main(int argc, char **argv)
{	
	int x = 1;
	printf("Hello x = %d\n", x);
	
	asm ("movl %1, %0;"
    :"=r"(x) 
    :"r"(x+1) 
    :);
	
	printf("Hello x = %d after increment\n", x);
	
	if(x == 2){
		printf("OK\n");
	}
	else{
		printf("ERROR\n");
	}
}	
	
	
