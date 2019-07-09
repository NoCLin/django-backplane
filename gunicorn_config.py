import multiprocessing

bind = "0.0.0.0:8000"
worker_class = "gevent"
workers = multiprocessing.cpu_count() * 2 + 1
raw_env = ["LANG=zh_CN.UTF-8", "LC_ALL=zh_CN.UTF-8"]
