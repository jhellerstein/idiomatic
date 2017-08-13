OBJS = noop_server.o noop_client.o
CC = g++ 
DEBUG = -g
FLUENT_DIR = /Users/jmh/code/fluent
FLUENT_BUILD = ${FLUENT_DIR}/build/Debug
INCLUDES = -I$(FLUENT_DIR)/src \
   -I$(FLUENT_BUILD)/src/googletest_project/googletest/include \
   -I$(FLUENT_BUILD)/src/range-v3_project/include \
   -I$(FLUENT_BUILD)/src/cereal_project/include
CFLAGS = -std=c++14 -Wall -c $(DEBUG) $(INCLUDES) \
         -Wall \
         -Wextra \
         -Werror \
         -pedantic \
         -frtti # for handling exceptions in dylibs
LFLAGS = -Wall $(DEBUG) -dynamiclib
LDLIBS = -L$(FLUENT_BUILD)/fluent -lfluent -lzmq -lglog -lfmt

%.o: %.cc
	$(CC) $(CFLAGS) $(CPPFLAGS) -c $<

fluentchat.dylib: fluentchat.o client.h server.h
	$(CC) $(LFLAGS) fluentchat.o $(LDLIBS) -o fluentchat.dylib

clean:
	rm *o fluentchat.dylib
