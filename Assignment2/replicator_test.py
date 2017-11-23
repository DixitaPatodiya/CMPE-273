import grpc
import datastore_pb2

PORT = 3000

class ReplicatorTest():
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, key, data):
        return self.stub.put(datastore_pb2.Request(key=key, data=data))

    def delete(self, key):
        return self.stub.delete(datastore_pb2.Request(key=key))

def run(host, port):

    rep_test = ReplicatorTest(host, port)
    print('k = hi, d = hello')
    response = rep_test.put('hi', 'hello')
    print(response.data)

    print('k = hey, d = hii')
    response = rep_test.put('hey', 'hii')
    print(response.data)

    print('delete k = hello')
    response = rep_test.delete('hello')
    print(response.data)

if __name__ == "__main__":
    run()
