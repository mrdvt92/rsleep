#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <math.h> 

const float VERSION = 0.05;

int main(int argc, char **argv) {
  float        v_sleep;
  float        v_limit;
  int          v_argv;
  int          v_print;
  FILE         *urandom;
  unsigned int seed;

  urandom = fopen("/dev/urandom", "r"); 
  if (urandom == NULL) { 
    srand48(time(NULL));
  } else {
    fread(&seed, sizeof(seed), 1, urandom); 
    srand48(seed); /* seed the pseudo-random number generator */ 
  }

  while ((v_argv = getopt(argc, argv, "dvh")) != -1)
         switch (v_argv)
           {
           case 'd':
             v_print = 1;
             break;
           case 'v':
             printf("rsleep version: %.2f\n", VERSION);
             exit(0);
             break;
           case 'h':
             printf("rsleep is an executable which provides random sleep for scripts.\n\n");
             printf("Syntax:\n   rsleep [-d] [seconds]\n   rsleep -v\n   rsleep -h\n\n");
             printf("Copyright (c) 2013-2025 Michael R. Davis\n");
             printf("This program is free software; you can redistribute it and/or\nmodify it under the terms of the GNU General Public License\nVersion 2 as published by the Free Software Foundation.\n");
             exit(0);
             break;
           }
  
  v_limit=5.0;
  if (optind < argc) /* optind - The index in the argument value array (argv) where the first nonoption command-line argument can be found.  */
    v_limit = atof(argv[optind]);

/*
  if (v_print == 1)
    printf("%.4f\n", v_limit);
*/

  v_sleep = drand48() * v_limit;

  if (v_print == 1)
    printf("%.4f\n", v_sleep);
  
  usleep(v_sleep * 1000000);

  return 0;
}
