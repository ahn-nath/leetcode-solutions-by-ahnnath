class RecentCounter:

    def __init__(self):
        self.last_valid_index = 0
        self.requests = []

    def ping(self, t: int) -> int:
        # update requests list
        self.requests.append(t)
        # define range
        range_ = [t - 3000, t]
        result = 0
        switch = 1
        # loop over the list of requests
        for i in range(self.last_valid_index, len(self.requests)):
            curr = self.requests[i]
            if range_[0] <= curr <= range_[1]:
                result += 1
                # update the first valid index to use as a reference, considering the next t will be larger
                # if switch:
                #   switch = 0
                #    self.last_valid_index = i

        print(result)
        return result


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
if __name__ == '__main__':
    obj = RecentCounter()
    obj.ping(1)  # 1
    obj.ping(100)  # 2
    obj.ping(3001)  # 3
    obj.ping(3002)  # 3
    obj.ping(4000)  # 3
    obj.ping(7000)  # 2
    obj.ping(15000)  # 1
