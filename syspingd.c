# include <time.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
# include <sys/types.h>
# include <sys/stat.h>
# include <stdbool.h>
int main(){
	pid_t pid;

	pid = fork();

	if (pid < 0){
		exit(EXIT_FAILURE);
	}

	if (pid > 0){
		exit(EXIT_SUCCESS);
	}

	if (setsid() < 0){
		exit(EXIT_FAILURE);
	}

	chdir("/");

	close(STDIN_FILENO);
	close(STDOUT_FILENO);
	close(STDERR_FILENO);

	while(true){
		system("python3 PATH TO THE PYTHON FILE/ping.py");
		sleep(10);
		
	}
}
