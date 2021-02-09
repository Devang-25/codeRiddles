#!/usr/bin/env python3

import os
import copy
import threading
import traceback
import functools
import concurrent.futures as cf
from multiprocessing import Process, Manager, Pool
from newsplease import NewsPlease
from newsplease.crawler.simple_crawler import SimpleCrawler

# usage: https://rednafi.github.io/digressions/python/2020/04/21/python-concurrent-futures.html
# performance: https://stackoverflow.com/questions/42074501/python-concurrent-futures-processpoolexecutor-performance-of-submit-vs-map

# can probably use https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable
# to generate chained iterable generators
# https://docs.python.org/3/library/itertools.html#itertools.chain

# locks in threads  https://stackoverflow.com/questions/16369382/with-statement-and-python-threading

# map in python:
# In [228]: def f(a,b):
#      ...:     return a+b
# In [231]: list(map(f,(10,8),(2,30)))
# Out[231]: [12, 38]


def timeit(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print(f"{method.__name__} => {(end_time-start_time)*1000} ms")

        return result

    return wrapper


def trace_unhandled_exceptions(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            print("Exception in ", func.__name__)
            traceback.print_exc()

    return wrapped_func


@timeit
def download_articles():
    """
    threaded tasks list
    """
    tic = time.time()

    threads = [
        threading.Thread(target=SimpleCrawler._fetch_url, args=(url, True, timeout))
        for url in urls
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=30)

    toc = time.time()
    print(f"Downloaded: {(toc - tic):.2f} seconds")
    # import pdb
    #
    # pdb.set_trace()
    # futures = {url: html_res for url, html_res in zip(urls, res)}

    # for url in futures:
    #     url, html_res = list(item._result.items())[0]
    #     SimpleCrawler._results[url] = html_res
    #
    results = copy.deepcopy(SimpleCrawler._results)
    SimpleCrawler._results = {}
    return results
    # return futures


def callback(result):
    print("success", result)


def callback_error(result):
    print("error", result)


def go():
    print(1)
    raise Exception()
    print(2)


@trace_unhandled_exceptions
def go_handled():
    # https://stackoverflow.com/a/25384934/1332401
    print(1)
    raise Exception()
    print(2)


def mpc_pool():
    p = Pool()
    p.apply_async(go, callback=callback, error_callback=callback_error)
    # p.close()
    # p.join()

    p = Pool(1)
    p.apply_async(go_handled)
    p.close()
    p.join()


def extract_info_from_articles(results):
    """
    process pooling with futures
    CPU intensive tasks on separate CPU cores.
    Doesn't share context unless the method it calls dumps it to a file/db
    or a shared context is passed using either of
        - multiprocessing.Manager https://stackoverflow.com/a/55816091/1332401

    """

    tic = time.time()

    # needed to call shutdown after workers are done with the jobs
    # https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown
    with cf.ProcessPoolExecutor(60) as exec:
        # # futures = []
        # # for url in urls:
        # #     futures.append(exec.submit(SimpleCrawler._fetch_url, url, True, timeout))
        # futures = [
        #     exec.submit(SimpleCrawler._fetch_url, url, True, timeout)
        #     for url in urls
        # ]
        futures = {
            exec.submit(NewsPlease.from_html, results[url], url, download_date): url
            for url in results
        }

        # # # we used exec.submit because we wanna be able to catch errors later
        # # using cf.as_completed() for each future individually
        # # https://stackoverflow.com/a/53346191/1332401
        # # https://stackoverflow.com/a/59638692/1332401
        # # However, map maintains the order of url -> futures
        # nprocs = len(os.sched_getaffinity(0))
        # slice_len = len(urls)/nprocs
        # args = [(results[url], url, download_date) for url in results]
        # results = {
        #     url: html_res
        #     for url, html_res in zip(
        #         urls,
        #         exec.map(
        #             NewsPlease.from_html, *zip(*args), chunksize=slice_len,
        #         ),
        #     )
        # }
        # or
        # exec.map(lambda p: _fetch_url(*p), args)

        # # ways to wrap a function for taking in single argument
        # from functools import partial
        # func = partial(_fetch_url, url, timeout)
        # res = exec.map(SimpleCrawler._fetch_url, *zip(*args))
        # zip(urls, exec.map(_fetch_url, *zip(*args)))
        # exec.map(SimpleCrawler._fetch_url, *zip(*args))

    for fut in cf.as_completed(futures):
        url = futures[fut]
        try:
            results[url] = fut.result(timeout=timeout)
        except Exception as err:
            print(err, url)
            results[url] = []
            # optionally, cancel all jobs on first exception encountered
            if fut.exception() is not None:
                for f in futures:
                    f.cancel()
                msg = "..cancelled all jobs. FIRST_EXCEPTION encountered"
                print(msg)
                break
    toc = time.time()
    print(f"Extracted from HTML: {(toc - tic):.2f} seconds")
    return results


def process_pooling_with_futures():
    tic = time.time()

    with cf.ProcessPoolExecutor() as exec:
        futures = {
            exec.submit(NewsPlease.from_html, results[url], url, download_date): url
            for url in results
        }

    for fut in cf.as_completed(futures):
        url = futures[fut]
        try:
            results[url] = fut.result(timeout=timeout)
        except Exception as err:
            print(err, url)
            results[url] = []

    # for url in results:
    #     results[url] = NewsPlease.from_html(results[url], url, download_date)

    toc = time.time()
    print(f"Extracted from HTML: {(toc - tic):.2f} seconds")
    return results
