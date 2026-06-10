import time ,logging

logger = logging.getLogger(__name__)

class RequestDurationMiddleware:
    def __init__(self,get_responce):
        self.get_responce = get_responce

    def __call__(self, request):
        start = time.perf_counter()
        responce = self.get_responce(request)
        duration_ms = (time.perf_counter() - start) * 100
        logger.info("%s %s -> %d [ %1f ms]",request.method , request.path , responce.status_code , duration_ms)
        responce["X-responce-Time-ms"] = f"{durations_ms:1f}"
        return responce
    


#settings.py

MIDDLEWARE = ['myapp.middleware.RequestDurationMiddleware']

