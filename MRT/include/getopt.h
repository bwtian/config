#ifndef GETOPT_H_INCLUDE
#define GETOPT_H_INCLUDE

#ifdef __cplusplus
extern "C" {
#endif

extern int opterr;
extern int optind;
extern int optopt;
extern char *optarg;

int getopt(int argc, char **argv, char *opts);

#ifdef __cplusplus
}
#endif

#endif /* GETOPT_H_INCLUDE */
