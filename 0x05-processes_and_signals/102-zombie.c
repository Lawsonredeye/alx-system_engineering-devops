#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - main point of execution
 *
 * Return: zero always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main point of execution
 *
 * Return: zero always
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
