from manager import Manager
from builds.service_pb2_grpc import StatServiceServicer, add_StatServiceServicer_to_server
from builds.service_pb2 import Stat, Id
from concurrent.futures import ThreadPoolExecutor
import grpc

manager = Manager()


class Service(StatServiceServicer):
    def CalcStat(self, request: Id, context) -> Stat:
        comments, symbols = manager.get_stat(request.id)
        return Stat(
            comments=comments,
            symbols=symbols
        )


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_StatServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    server.wait_for_termination()


if __name__ == '__main__':
    execute_server()
