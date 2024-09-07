from fastapi import FastAPI, Query, HTTPException, Request
from kv_base_model import KeyValue
from typing import  Dict, Optional

app = FastAPI()

#Dictionary Data Structure to store the key value pairs.
from prometheus_client import Summary
from prometheus_client.core import CollectorRegistry
from prometheus_client.exposition import generate_latest, CONTENT_TYPE_LATEST

registry = CollectorRegistry()

REQUEST_LATENCY = Summary(
    'request_latency_seconds', 'Request latency in seconds', ['method', 'endpoint'], registry=registry
)



@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    method = request.method
    endpoint = request.url.path
    with REQUEST_LATENCY.labels(method=method, endpoint=endpoint).time():
        response = await call_next(request)
    return response

@app.get("/metrics")
async def metrics():
    return generate_latest(registry), 200, {'Content-Type': CONTENT_TYPE_LATEST}


list_of_keyvalues: Dict[str, str] = {}

@app.get("/")
async def root():
    return {"message": "This is a sample KV store"}

@app.get("/get/{key}")
async def read_item_from_kv(key):
        if key in list_of_keyvalues:
            return {"value": list_of_keyvalues[key]}
        else:
            raise HTTPException(status_code=404, message=f"Value for {key} not found")

@app.post("/key/set")
async def set_key_in_kv(keyvalue: KeyValue):
    try:
        if keyvalue.key in list_of_keyvalues:
            return {"message": f"Key {keyvalue.key} already exists."}
        else:
            list_of_keyvalues[keyvalue.key] = keyvalue.value
    
        return {"message": {f"{keyvalue.key}:{keyvalue.value}"}}
    except:
        return {"message":"Adding the value of {key} to KV Store has failed.", "success":False}

@app.get("/search")
async def search_keys_by_prefix_or_suffix_from_kv(prefix: Optional[str] = Query(None), suffix: Optional[str]  = Query(None)):
    try:
        list_of_keys = []
        if prefix  and suffix:
            return {"message": "Either Prefix or Suffix can only be passed for the search endpoint."}
        for key,value in list_of_keyvalues.items():
            if prefix:
                if key.startswith(prefix):
                    list_of_keys.append(key)
            elif suffix:
                if key.endswith(suffix):
                    list_of_keys.append(key)
        return {"Matching Key List" : list_of_keys}
    except:
        return {"Searching keys with {prefix} failed"}    


