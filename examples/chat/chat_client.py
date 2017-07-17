#!/usr/bin/python
from ctypes import * #cdll
import argparse

parser = argparse.ArgumentParser("Launch a Fluent chat server.")
parser.add_argument('server_address',
	                help='ZeroMQ address of the server (e.g. tcp://0.0.0.0:8000)')
parser.add_argument('your_address',
	                help='ZeroMQ address for this client (e.g. tcp://0.0.0.0:8001)')
parser.add_argument('nickname',
	                help='your nickname')

args = parser.parse_args()

chat_lib = cdll.LoadLibrary("fluentchat.dylib")
chat_lib.client.argtypes = [c_char_p, c_char_p, c_char_p]

chatclient = chat_lib.client(args.server_address.encode("ascii"), 
	                         args.nickname.encode("ascii"),
    	                     args.your_address.encode("ascii"))
