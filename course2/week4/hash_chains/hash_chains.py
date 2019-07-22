# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]

    def find(self,s):
        hash=self._hash_func(s)
        if self.elems[hash]==[]:
            return (-1,hash)
        idx=-1
        for eIdx in range(len(self.elems[hash])):
            if self.elems[hash][eIdx]==s:
                return (hash,eIdx)
        return (-1,hash)

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if self.elems[query.ind]==[]:
                self.write_chain(" ")
            else:
                self.write_chain(cur for cur in reversed(self.elems[query.ind])
                        if self._hash_func(cur) == query.ind)
        else:
            hashInd = self.find(query.s)
            if query.type == 'find':
                self.write_search_result(hashInd[0]!=-1)
            elif query.type == 'add':
                if hashInd[0] == -1:
                    self.elems[hashInd[1]].append(query.s)
            else:
                if hashInd[0] != -1:
                    self.elems[hashInd[0]].pop(hashInd[1])

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
