import math

data = list(map(int, input().split()))
n = data[0]
m = data[1]
data = data[2:]


def h(state):
    return 2 * math.ceil((m - state[2]) / max(data))


def AStar():
    begin_state = (0, [0 for _ in data], 0, [])

    heap = [begin_state]

    while (len(heap) > 0):
        heap.sort(key=lambda e: e[0] + h(e))
        state = heap.pop(0)

        step_num = state[0]
        cans = state[1]
        current = state[2]
        trace = state[3]

        # print(state)

        if current == m:
            return trace

        for i, can in enumerate(cans):
            if can == data[i]:
                continue
            _cans = cans[:]
            _cans[i] = data[i]
            next_trace = trace[:]

            next_trace.append((-2, i))
            heap.append((step_num + 1, _cans, current, next_trace))

        for i, can in enumerate(cans):
            if can == 0:
                continue

            if current + can > m:
                continue

            val = cans[i]
            _cans = cans[:]
            _cans[i] = 0
            next_trace = trace[:]

            next_trace.append((i, -1))
            heap.append((step_num + 1, _cans, current + val, next_trace))

        for i, can1 in enumerate(cans):
            for j, can2 in enumerate(cans):
                if i == j:
                    continue
                if can1 == 0:
                    continue
                if can2 == data[j]:
                    continue

                last_can1, last_can2 = trace[-1]
                if i == last_can2 and j == last_can1:
                    continue

                dif = min([can1, data[j] - can2])

                _cans = cans[:]

                _cans[i] -= dif
                _cans[j] += dif

                next_trace = trace[:]
                next_trace.append((i, j))
                heap.append((step_num + 1, _cans, current, next_trace))

        for i, can in enumerate(cans):

            if can == 0:
                continue

            a, b = trace[-1]

            if a == -2 and b == i:
                continue
            _cans = cans[:]
            _cans[i] = 0
            next_trace = trace[:]

            next_trace.append((i, -2))
            heap.append((step_num + 1, _cans, current, next_trace))
    return False


result = AStar()
if not result:
    print("Khong co dap an")
else:
    state = [0 for _ in data]
    current = 0
    for step in result:
        a, b = step
        an = 'bo song' if a == - \
            2 else 'be nuoc' if a == -1 else f'gao nuoc {a}'
        bn = 'bo song' if b == - \
            2 else 'be nuoc' if b == -1 else f'gao nuoc {b}'

        if a == -2:
            state[b] = data[b]
        elif b == -1:
            current += state[a]
            state[a] = 0
        else:
            dif = min([state[a], data[b] - state[b]])
            state[a] -= dif
            state[b] += dif

        print(f'{an} -> {bn}, be nuoc: {current}, trang thai: {state}')

# Trả lời: Hãy giải thích hàm h’ (hàm khoảng cách trong thuật toán A* ở chương trình trên. (0.5 điểm)

# h’ là hàm heuristic, nó được sử dụng để ước lượng khoảng cách từtrạng thái hiện tại đến trạng thái mục
# tiêu.Trong bài toán này, hàm h’ được định nghĩa bằng cách tính tổng khoảng cách tuyệt đối giữa lượng
# nước trong các gáo của trạng thái hiện tại và trạng thái mục tiêu. Khoảng cách này được sửdụng để
# đánh giá ưu tiên các trạng thái trong hàng đợi ưu tiên.
