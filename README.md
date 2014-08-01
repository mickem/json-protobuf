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

## Missing plugin_pb2 Python Module

The protocol buffers Python installer does not install a file required by protoc-gen-lua at this time. The missing file is the Python interface to the compiler plugin *plugin.proto*. The protoc-gen-lua Python script may fail when importing the *google.protobuf.compiler.plugin_pb2* module.

A thread on the protocol buffers mailing list [discusses the issue](http://groups.google.com/group/protobuf/browse_thread/thread/e58c33f20c27f4a9).

At this time, the issue can be worked around by manually installing the missing file.

Assuming you have a working protoc compiler on your system and have the existing Python protocol buffers package installed, from the protocol buffers source code directory, run the following:

    $ protoc -Isrc --python_out=/path/to/output/directory src/google/protobuf/compiler/plugin.proto

The command should produce no output if successful. Additionally, the file */path/to/output/directory/google/protobuf/compiler/plugin_pb2.py* should have been created.

Next, find the location of the installed protocol buffer Python package. If you have *locate*, try finding it via *`locate descriptor_pb2.py`*. A common location is something like */usr/lib/python2.6/site-packages/protobuf-2.3.0-py2.6.egg/google/protobuf/*. Navigate to this directory and:

    $ mkdir compiler
    $ touch compiler/__init__.py
    $ cp /path/to/plugin_pb2.py compiler/plugin_pb2.py

In common English:

1. Create a new directory, from the install root, *google/protobuf/compiler*
2. Create an empty file, *\_\_init\_\_.py* in this directory. This tells Python that the directory contains Python modules.
3. Copy the *plugin_pb2.py* file produced by protoc to this new directory.

Depending on the installed location of protocol buffers, these actions may require superuser or administrator privileges.

# Compiling Produced Files

You should be able to compile the produced .h and .cc files like you would for protocol buffer output files. If you have an existing Makefile, project, etc, just add the produced .h and .cc files to it.
