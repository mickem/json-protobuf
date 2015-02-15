@IF DEFINED PYTHON (@setlocal enableextensions & %PYTHON% -u -x %~f0 %* & goto :EOF) ELSE (@setlocal enableextensions & python.exe -u -x %~f0 %* & goto :EOF)
#!python.exe
# EASY-INSTALL-SCRIPT: 'json-protobuf==0.0.1','protoc-gen-json'
__requires__ = 'json-protobuf==0.0.1'
try:
	import pkg_resources
	pkg_resources.run_script('json-protobuf==0.0.1', 'protoc-gen-json')
except:
	import sys
	from os.path import dirname, realpath
	path = dirname(realpath(__file__))
	sys.path.append(path)
	execfile("%s/protoc-gen-json"%path)