from bisect import bisect


class SnapshotArray:
    """
    We want to implement some object so that everytime we take a "snapshot", we save off the current state
    of the current array.
    """

    def __init__(self, length: int):
        self.length = length
        self.total_arrays = [{0: 0} for _ in range(length)]
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        self.total_arrays[index][self.snap_count] = val

    def snap(self) -> int:
        temp = self.snap_count
        self.total_arrays
        self.snap_count += 1
        return temp

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.total_arrays[index]:
            return self.total_arrays[index][snap_id]
        else:
            # Need to get the index as close to the snap_id as possible. Could use bisect module here!
            keys_list = list(self.total_arrays[index].keys())
            lower_index = bisect(keys_list, snap_id) - 1
            key = keys_list[lower_index]
            return self.total_arrays[index][key]


if __name__ == '__main__':
    obj = SnapshotArray(4)
    obj.snap()
    obj.snap()
    obj.get(3, 1)
    obj.set(2, 4)
    obj.snap()
    obj.set(1, 4)
