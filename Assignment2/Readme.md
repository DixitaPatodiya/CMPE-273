### Assignment 2
Implement a RocksDB replication in Python using the design from this C++ replicator.  (Links to an external site.)Links to an external site.You can use Lab 1 as a based line. Differences form the replicator are:

You will be using GRPC Python server instead of Thrift server.
You will be exploring more into GRPC sync, async, and streaming.
You can ignore all cluster management features from the replicator.

Run :
python3.6 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto
python3.6 server.py
python3.6 client.py
pyhton3.6 replicator_test.py
