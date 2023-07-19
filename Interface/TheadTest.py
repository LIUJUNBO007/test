import concurrent.futures
import time


def worker(n):
    print(f"{n} 开始执行")
    time.sleep(1)
    print(f"{n} 执行完毕")
    return n * n


if __name__ == "__main__":
    # 创建线程池，最大线程数为3
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务到线程池
        tasks = [executor.submit(worker, i) for i in range(10)]
        # 获取任务结果
        for future in concurrent.futures.as_completed(tasks):
            result = future.result()
            print(f"任务返回值: {result}")
