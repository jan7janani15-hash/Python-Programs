def create_device_config(device_id,**kwargs):
    config={"device_id":device_id}
    fields=["baud_rate","parity","timeout_ms","debug"]
    for key in kwargs:
        if key not in fields:
            raise ValueError("Unsupported key: "+key)
        config[key]=kwargs[key]
    return config
print(create_device_config("D01",baud_rate=115200,parity="N",timeout_ms=500))