#include "./fig1.h"
#include "./fig2.h"
#include "./fig6.h"
#include "lineagedb/connection_config.h"
#include "lineagedb/noop_client.h"

#ifdef __cplusplus
extern "C"
{
#endif

int
fig1(const char addrclient) {
    hello_serverArgs sargs{addr};

    return hello_serverMain(sargs);
}

int
fig2(const char *addr) {
    kvs_serverArgs sargs{addr};

    return kvs_serverMain(sargs);
}

int
fig6(const char *addr) {
    redisArgs sargs{addr};

    return redisMain(sargs);
}


#ifdef __cplusplus
}
#endif
