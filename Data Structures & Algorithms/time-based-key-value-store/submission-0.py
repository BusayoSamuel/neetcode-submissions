class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.hashmap[key]

        prev = ""

        for time, value in timestamps:
            if time == timestamp:
                return value
            elif time > timestamp:
                return prev
            
            prev = value

        return prev

