def stream_batches(data,size):
    batches=[]
    for x in data:
        batches.append(x)
        if len(batches)==size:
            yield batches
            batches=[]
    if batches:
        yield batches
data=[1,2,3,4,5,6,7,8]
print(list(stream_batches(data,3)))