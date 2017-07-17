# A Bloomly Example
This directory provides an example of `yml2fluent`. Contents:

- `chat_client.py`, `chat_server.py`: Python driver programs for the chat client and server
- `client.yml`, `server.yml`: YAML specifications of the Bloom programs for chat
- `fluentchat.cc`: a dylib wrapper for the Bloomly code
- `Makefile`: a simple Makefile

## Building the code
```bash
$ python ../../yml2fluent.py client.yml -o client.h
$ python ../../yml2fluent.py server.yml -o server.h
$ make clean; make
```
Have a look at `client.h` and `server.h`. You should be able to see how the yaml files got embedded into the C++ boilerplate (and translated accordingly).

Also have a look at `fluentchat.cc`, which includes both the `.h` files we built above. Note the conventions for the server arguments (`ChatClientArgs`, `ChatServerArgs`) and server initialization (`ChatClientMain<fluent::lineagedb::NoopClient>(args, config);`, `ChatServerMain<fluent::lineagedb::NoopClient>(sargs, config);`). (You can ignore the `lineagedb` and `config` details -- they aren't relevant to our discussion.)


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

