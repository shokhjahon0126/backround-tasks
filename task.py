from redis import Redis
from time import sleep


redis = Redis(
    host='localhost',
    port=6379,
    username="shokhjahon",
    password=123
)

# redis.set(
#     name="username",
#     value="shokhjahon",
#     ex=60
# )

print(redis.get("username"))
print(redis.ttl("username"))