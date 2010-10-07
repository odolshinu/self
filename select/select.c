/* A DEMO ON SYNCHRONOUS I/O MULTIPLEXING
 * USING 'select' SYSTEM CALL.
 */

#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/select.h>

#define SIZE 1024

/* The a.out consist of one more argument,
   which is a named pipe.
 */
main(int argc, char *argv[])
{
	int fd1, retval, length;
	fd_set rfds, wfds;
	struct timeval tv;
	char buf[SIZE];

	if(!argv[1]) {
		printf("No pipe given\n");
		exit(0);
	}
	fd1 = open(argv[1], O_RDWR);

	FD_ZERO(&rfds);
	FD_SET(0, &rfds);
	FD_SET(fd1, &rfds);

	tv.tv_sec = 5;//Timeout (in seconds)
	tv.tv_usec = 0;

	retval = select(fd1 + 1, &rfds, NULL, NULL, &tv);
	if(retval == -1)
		perror("error:");
	else if(retval) {
		if (FD_ISSET(0, &rfds)) {
			length = read(0, buf, SIZE);
			printf("data available at standard input...\n");
		}
		if(FD_ISSET(fd1, &rfds)) {
			length = read(fd1, buf, SIZE);
			printf("data available in pipe...\n");
		}
		buf[length] = '\0';
		printf("Data is: %s", buf);
	} else
		printf("no response\n");
}
