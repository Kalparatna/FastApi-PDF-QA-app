from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from redis import Redis

redis = Redis(host="localhost", port=6379, decode_responses=True)
FastAPILimiter.init(redis)

# Applying rate limiting to WebSocket and REST endpoints (5 requests per minute)
rate_limiter = RateLimiter(times=5, seconds=60)  # 
