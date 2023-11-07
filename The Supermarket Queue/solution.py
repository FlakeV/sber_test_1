from typing import List


def queue_time(queue: List[int], tills_count: int) -> int:
    tills_dict = {}
    for i in range(1, tills_count + 1):
        tills_dict[i] = 0

    for customer in queue:
        minimal_time = min(tills_dict, key=tills_dict.get)
        tills_dict[minimal_time] += customer

    return tills_dict[max(tills_dict, key=tills_dict.get)]
