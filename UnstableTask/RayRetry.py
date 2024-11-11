import numpy as np
import ray
import time
from ray.util.state import summarize_tasks


ray.init(address="ray://127.0.0.1:10001")

class RandomError(Exception):
    pass

@ray.remote(max_retries=3, retry_exceptions=True)
def unstable_task(failure_probability):
    time.sleep(0.2)
    if np.random.random() < failure_probability:
        print('FAILURE')
        raise RandomError("Task failed!")
    return 0


if __name__ == '__main__':
    for _ in range(10):
        try:
            # If this task crashes, Ray will retry it up to one additional
            # time. If either of the attempts succeeds, the call to ray.get
            # below will return normally. Otherwise, it will raise an
            # exception.
            ray.get(unstable_task.remote(0.5))
            print('SUCCESS')
        except ray.exceptions.WorkerCrashedError:
            print('FAILURE')
        # finally:
        #     # print(list_tasks(detail=True))
        #     print(summarize_tasks())