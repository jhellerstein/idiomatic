# A Idiomatic Bloom Example
This directory provides an example of Bloom in `idiomatic`. Contents:

- `chat_client.py`, `chat_server.py`: Python driver programs for the chat client and server
- `client.bl`, `server.bl`: Bloom programs for chat
- `fluentchat.cc`: a dylib wrapper for the Bloom code
- `Makefile`: a simple Makefile

## Building the code
```bash
$ python ../../idiomatic client.bl -o client.h
$ python ../../idiomatic server.bl -o server.h
$ make clean; make
```
Have a look at `client.h` and `server.h`. You should be able to see how the `.bl` files got compiled into the C++ boilerplate.

Also have a look at `fluentchat.cc`, which includes both of the `.h` files we built above. Note the conventions for the server arguments (`ChatClientArgs`, `ChatServerArgs`) and server initialization (`ChatClientMain<fluent::lineagedb::NoopClient>(args, config);`, `ChatServerMain<fluent::lineagedb::NoopClient>(sargs, config);`). (You can ignore the `lineagedb` and `config` details -- they aren't relevant to our discussion.)


## Running the code:
### Running the server
```bash
$ python chat_server.py tcp://0.0.0.0:9000
```

### Running clients (open a new shell for each):
```bash
$ python chat_client.py tcp://0.0.0.0:9000 tcp://0.0.0.0:9001 Alice
```

```bash
$ python chat_client.py tcp://0.0.0.0:9000 tcp://0.0.0.0:9002 Bob
```

