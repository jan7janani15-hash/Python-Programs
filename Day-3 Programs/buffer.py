class DataBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
    def get(self, key):
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value
            return value
        return None
    def put(self,key,value):
        self.data[key]=value
        if len(self.data)>self.capacity:
            self.data.pop(next(iter(self.data)))
buffer=DataBuffer(2)
buffer.put("sensor1",24.5)
buffer.put("sensor2",28.0)
buffer.get("sensor1")
buffer.put("sensor3",31.2)
print(buffer.get("sensor2"))
print(buffer.get("sensor1"))
print(buffer.get("sensor3"))