import multiprocessing
workers = 2 * multiprocessing.cpu_count() + 1
worker_class = 'eventlet'  # Use gevent async workers
worker_connections = 2000  # Maximum concurrent connections per worker
timeout = 30
graceful_timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 50
bind = "0.0.0.0:4000"
