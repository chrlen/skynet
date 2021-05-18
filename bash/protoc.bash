#! /bin/bash

protoc -I=./ --python_out=./skynet/proto ./skynet.proto