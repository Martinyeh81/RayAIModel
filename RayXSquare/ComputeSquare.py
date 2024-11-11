import ray
import random

ray.init(address="ray://127.0.0.1:10001")

@ray.remote
def compute(x):
    return x * x

if __name__ == '__main__':

    # input data
    data = [random.randint(1, 100) for i in range(100)]

    # square
    square_result = [compute.remote(x) for x in data]

    # collect all task
    results = ray.get(square_result)

    # result
    print("Squared results:", results)