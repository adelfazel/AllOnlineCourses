# python3
import math

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times      = [None] * len(self.jobs)
        self.heap =[(i,0) for i in range(self.num_workers)]
        self.height=self.getHeight(self.num_workers)
        #print("self.height:%d"%self.height)

    def levelRemaining(self,idx):
        return self.height-self.getHeight(idx)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])
    def getHeight(self,idx):
        return math.ceil(math.log(idx+1,2))
    def assign_jobs(self):
        for jobIdx in range(len(self.jobs)):
            e=self.heap[0]
            self.start_times[jobIdx]     =(e[1])
            self.assigned_workers[jobIdx]=(e[0])
            self.heap[0] = (e[0],e[1]+self.jobs[jobIdx])
            if self.num_workers>5:
                self.pass_down(0)
            else:
                self.pass_down_lastLevel(0)

    def pass_down(self,idx):
        smallestIdx=idx
        if self.isSmaller(2*idx+1,smallestIdx):
            smallestIdx = 2 * idx + 1
        if self.isSmaller(2*idx+2,smallestIdx):
            smallestIdx = 2 * idx + 2
        if idx!=smallestIdx:
            tmp=self.heap[idx]
            self.heap[idx]=self.heap[smallestIdx]
            self.heap[smallestIdx] = tmp
            #print("self.levelRemaining(idx):%d"%self.levelRemaining(idx))
            if self.levelRemaining(idx)>3:
                self.pass_down(smallestIdx)
            else:
                self.pass_down_lastLevel(smallestIdx)

    def pass_down_lastLevel(self,idx):
        if self.num_workers<2*idx+2:
            return
        smallestIdx=idx
        if self.isSmaller(2*idx+1,smallestIdx):
            smallestIdx=2*idx+1
        if 2 * idx + 2 < self.num_workers:
           if self.isSmaller( 2 * idx + 2,smallestIdx):
               smallestIdx = 2 * idx + 2
        if idx!=smallestIdx:
            tmp=self.heap[idx]
            self.heap[idx]=self.heap[smallestIdx]
            self.heap[smallestIdx] = tmp
            self.pass_down_lastLevel(smallestIdx)


    def isSmaller(self, idx1, idx2):
        if self.heap[idx1][1] < self.heap[idx2][1]:
            return True
        if self.heap[idx1][1] == self.heap[idx2][1] and self.heap[idx1][0] < self.heap[idx2][0]:
            return True
        return False

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
