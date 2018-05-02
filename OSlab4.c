#include <stdio.h>
#include <sys/resource.h>
#include <wait.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
	int temp;
	int fd[2];
	int p1, p2, p3,p4;
	char str1[50] = {"Child process P1 is sending messages!"};
	char str2[50] = {"Child process P2 is sending messages!"};
	char str3[50] = {"Child process P3 is sending messages!"};
	char str[50];
	pipe(fd);
	while ((p1 = fork()) == -1);
	if (p1 > 0)
	{
		while((p2 = fork()) == -1);
		if(p2 > 0)
		{ 
		while((p3 = fork()) == -1);
			if(p3>0){
				wait(0);
				read(fd[0],str,50);
				printf("%s\n",str);
				wait(0);
				read(fd[0],str,50);
				printf("%s\n",str);
				wait(0);
				read(fd[0],str,50);
				printf("%s\n",str);
				}
			else{
				sleep(1);
				lockf(fd[1],1,0);
				write(fd[1],str3,50);
				lockf(fd[1],0,0);
				exit(0);
			    }
    		}
    		else{
        	sleep(1);
        	lockf(fd[1], 1, 0);
        	write(fd[1],str2,50);
        	lockf(fd[1],0,0);
        	exit(0);
	 	 }
 	}
	else
	{
        sleep(1);
        lockf(fd[1],1,0);
        write(fd[1],str1,50);
        lockf(fd[1],0,0);
        exit(0);
	}
}
