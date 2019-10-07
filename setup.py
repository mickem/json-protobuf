#  Copyright 2019 Michael Medin
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = 'json-protobuf',
    version          = '1.0.0',
    author           = 'Michael Medin',
    author_email     = 'michael@medin.name',
    description      = 'Json protocol buffer code generator',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url              = 'http://github.com/mickem/json-protobuf',
    packages         = [ 'json_protobuf' ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    scripts          = ['protoc-gen-json', 'protoc-gen-json.cmd'],
    python_requires  = '>=3.6',
    install_requires = [ 'protobuf>=3.0.0' ]
)
