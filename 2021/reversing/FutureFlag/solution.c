/*
 * gcc -shared -o solution.so solution.c
 * LD_PRELOAD=./solution.so ./challenge
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

time_t
time(time_t *t)
{
	return (time_t)(1704063601 + 20 - (rand() % 10)) ;
}
