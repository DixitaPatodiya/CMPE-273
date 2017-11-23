import grpc
import datastore_pb2
import rocksdb

PORT = 3000


class ClientReplicator():
    def __init__(self, host='0.0.0.0', port=PORT):
        self.db = rocksdb.DB("ClientSlave.db", rocksdb.Options(create_if_missing=True))
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def sync(self):
        Queue = self.stub.sync(datastore_pb2.ReplicatorRequest())
        print("Connection established to MasterServer")
        for rp in Queue:
            if rp.action == 'put':
                print("Put {}:{} to slave_db".format(rp.key, rp.value))
                self.db.put(rp.key.encode(), rp.data.encode())
            elif rp.action == 'delete':
                print("Delete {} from slave_db".format(rp.key))
                self.db.delete(rp.key.encode())
            else:
                pass

def main():
    slave = ClientReplicator()
    slave.sync()


if __name__ == "__main__":
    main()
