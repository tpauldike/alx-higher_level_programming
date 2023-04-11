#include <stdio.h>
#include <stdlib.h>

int factr(int a);
int main(int argc, char *argv[])
{
	int num;

	if (argv[1])
	{
		num = atoi(argv[1]);
		printf("%d\n", factr(num));
	}
	else
		printf("%d\n", factr(1));

	return (0);
}

int factr(int a)
{
	if (a == 1)
		return (a);
	return (a * factr(a-1));
}
