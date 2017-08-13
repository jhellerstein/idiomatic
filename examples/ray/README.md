# A Idiomatic Bloom Example
This directory is an initial effort to provide a simple implementation of Python futures in the style of Ray. First goal is to build a single-node futures server, and then later show how it can be scaled out.

Basic idea, following Ray, is that futures will be pickled by Python `@ray.remote` decorators and sent in to be stored in a KVS; then asynchronously serviced, with results returning to something that can respond to Python `ray.get` calls. 

For now we'll skip the Python pickling and just invoke dummy functions in the futures.


## Building the code
```bash
$ python ../../idiomatic futures.bl -o futures.h
$ make clean; make
```

