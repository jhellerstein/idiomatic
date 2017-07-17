#include "./server.h"
#include "./client.h"
#include "lineagedb/connection_config.h"
#include "lineagedb/noop_client.h"

#ifdef __cplusplus
extern "C"
{
#endif

int
client(const char *server, const char *nick, const char *client) {
    ChatClientArgs args;
    args.server_address = server;
    args.nickname = nick;
    args.address = client;

    return ChatClientMain(args);
}

int
server(const char *addr) {
    ChatServerArgs sargs{addr};

    return ChatServerMain(sargs);
}


#ifdef __cplusplus
}
#endif
