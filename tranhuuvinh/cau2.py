# Câu 2 (2 điểm): Cho không gian Oxyz với 10 điểm có tọa độ tương ứng (0,4,1), (4,1,0) (3,2,0),(2,3,2),(2,4,1) 
# (2,3,4), (4,2,6), (4,1,2), (3,1,2) và (3,0,2) 
 
# a) (1 điểm) Viết hàm thực thi thuật toán k-mean
import random as rd 
import operator 
 
D = [(0, 4, 1), (4, 1, 0), (3, 2, 0), (2, 3, 2), 
     (2, 4, 1), (2, 3, 4), (4,2,6), (4,1,2), (3,1,2), (3,0,2)]
def distance(x, y): 
    sum = 0 
    for i in range(len(x)): 
        sum += (x[i] - y[i])**2 
    return sum 
 
def argmin(x, mu): 
    r = 0 
    dis = -1 
    for i in range(len(mu)): 
        d = distance(x, mu[i]) 
        if dis == -1 or dis > d: 
            r = i 
            dis = d 
    return r 
 
print(D) 
 
def kmeans(D, k): 
    # bước 1: Chọn ngẫu nhiên k phần tử trong dữ liệu D để làm k trọng tâm 
    mu = rd.sample(D, k) 
    n = len(D) 
    label = [0]*n 
    while True: 
        c = [(0, 0, 0)]*k 
        sl = [0]*k 
        # bước 2: Gán dữ liệu vào nhóm có trọng tâm gần nhất 
        cothaydoi = False 
        for i in range(n): 
            newlabel = argmin(D[i], mu) 
            if label[i] != newlabel: 
                label[i] = newlabel 
                cothaydoi = True 
        if not cothaydoi: 
            break 
        # bước 3: Tính lại trọng tâm của từng nhóm 
        for i in range(n): 
            c[label[i]] = tuple(map(operator.add, c[label[i]], D[i])) 
            sl[label[i]] += 1 
        for i in range(k): 
            if sl[i] != 0: 
                c[i] = tuple(map(operator.floordiv, c[i], [sl[i] 
                             for _ in range(len(c[i]))])) 
            else: 
                c[i] = rd.sample(D, 1) 
        mu = c[:] 
        # bước 4: Quay lại bước 2 nếu có thay đổi. 
    return mu, label
print (kmeans([(0, 4, 1), (4, 1, 0), (3, 2, 0), (2, 3, 2), 
     (2, 4, 1), (2, 3, 4), (4,2,6), (4,1,2), (3,1,2), (3,0,2)],2))