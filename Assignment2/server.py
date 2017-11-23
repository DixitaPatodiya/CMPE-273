
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import rocksdb
import queue

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyReplicatorServicer(datastore_pb2.ReplicatorServicer):
    def __init__(self):
        self.db = rocksdb.DB("MasterServer.db", rocksdb.Options(create_if_missing=True))
        self.operations_queue = queue.Queue()


    def push(method):
        def wrapper_function(self, request, context):
            rp = datastore_pb2.ReplicatorResponse(
                action=method.__name__,
                key=request.key.encode(),
                data=request.value.encode()
            )
            self.rp_queue.put(rp)
            # delegate the call to passed in method
            return method(self, request, context)

        return wrapper_function


    def put(self, request, context):
        print("Put{}:{} to master_db".format(request.key, request.data))
        data = self.db.put(request.key.encode(), request.data.encode())
        return datastore_pb2.Response(value=data)

    def get(self, request, context):
        print("Get{} from master_db".format(request.key))
        data = self.db.get(request.key.encode())
        return datastore_pb2.Response(value=data)

    def delete(self, request, context):
        print("Delete{} from master_db".format(request.key))
        self.db.delete(request.key.encode())
        return datastore_pb2.Response(value='0')

    def sync(self, request, context):
        print("Connection Successfully Established")
        while True:
            rp = self.rp_queue.get()
            print("Replicating data ({}, {}, {}) to slave".format(rp.op, rp.key, rp.data))
            yield rp


def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    datastore_pb2_grpc.add_ReplicatorServicer_to_server(MyReplicatorServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)
