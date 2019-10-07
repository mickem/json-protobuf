json-protobuf provides a Json interface to Google's [Protocol Buffers](http://code.google.com/apis/protocolbuffers/) compiled in C++ code.
The idea is that you can convert a protocol buffer object to a json representation which can be used in API:s.

# Producing Code

json-protobuf provides a plugin for the _protoc_ protocol buffer compiler (it ships with protocol buffers). This plugin tells _protoc_ to produce a set of C++ output files, which define the JSON interface to protocol buffers using the json-spirit library (other libraries will/coul be supported).

First, obtain a copy of json-protobuf:

    $ git clone git@github.com:mickem/json-protobuf.git
    $ cd json-protobuf

Next, install json-protobuf:

    $ python setup.py install

Finally, launch protoc and tell it to produce Lua output:

    $ protoc -I/path/to/your/proto/files --json_out=/output/path file1.proto file2.proto

You simply need to add _--json_out_ to the arguments to _protoc_ to get it to produce the Json output files.

Under the hood, _protoc_ is looking for the program _protoc-gen-json_ somewhere in your $PATH. You can modify $PATH in lieux of installing the package, if you desire.

# Compiling Produced Files

You should be able to compile the produced .h and .cc files like you would for protocol buffer output files. If you have an existing Makefile, project, etc, just add the produced .h and .cc files to it.
