
def find_max_int(arr):
    if len(arr) < 2:
        return 0

    start_idx, end_idx = 0, 0
    start_val, end_val = arr[start_idx], arr[end_idx]

    local_max = 0
    # track local

    for idx, val in enumerate(arr):
        if idx == 0:
            continue

        if val < start_val:
            # need to track of local max
            # buto nly reset it if cur local max is bigger
            cur_local_max = end_val - start_val
            if cur_local_max > local_max:
                local_max = cur_local_max

            #reset the start_ptr, and end_ptr
            start_idx = idx
            start_val = arr[idx]

            end_idx = idx
            end_val = arr[idx]
        else:
            # only increase the end_ptr if its val greater
            if val > end_val:
                end_ptr = idx
                end_val = val

    cur_local_max = end_val - start_val
    if cur_local_max > local_max:
        local_max = cur_local_max
    return local_max

def find_max_sum_two_intervals(arr):
    max_sum = 0
    for idx, val in enumerate(arr):
        if idx == 0:
            continue

        left = arr[:idx]
        right = arr[idx:]

        cur_sum = find_max_int(left) + find_max_int(right)
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum
