#!/usr/bin/python
from ctypes import cdll
import argparse

parser = argparse.ArgumentParser("Launch a Fluent chat server.")
parser.add_argument('address',
	                help='ZeroMQ address (e.g. tcp://0.0.0.0:8000)')

args = parser.parse_args()

chat_lib = cdll.LoadLibrary("fluentchat.dylib")

chatserver = chat_lib.server(args.address.encode("ascii"))
