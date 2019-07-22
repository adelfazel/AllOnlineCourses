# python3

from collections import namedtuple
from functools import reduce

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.lastTime=0
        self.finish_time=[]

    def getLatestTime(self):
        if self.isBufferEmpty():
            return self.lastTime
        else:
            return self.finish_time[-1]

    def addToBuffer(self,request):
        if self.isBufferFull():
            while self.finish_time:
                if self.finish_time[0]<=request.arrived_at:
                    self.lastTime=self.finish_time[0]
                    del self.finish_time[0]
                else:
                    break

            if self.isBufferFull():
                return (True,-1)
        self.finish_time.append(max(self.getLatestTime(),request.arrived_at)
                                        +request.time_to_process)
        return (False,self.finish_time[-1]-request.time_to_process)

    def isBufferFull(self):
        return len(self.finish_time)==self.size
    def isBufferEmpty(self):
        return len(self.finish_time)==0

    def process(self, request):
        res=self.addToBuffer(request)
        return Response(res[0],res[1])



def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))


    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
