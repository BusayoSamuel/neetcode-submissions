class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.hashmap[key]

        l = 0
        r = len(timestamps) - 1
        res = ""

        while l <= r:
            m = (r + l) // 2

            time, value = timestamps[m] 

            if time > timestamp:
                r = m - 1
            elif time < timestamp:
                res = value
                l = m + 1
            else:
                return value

        return res


