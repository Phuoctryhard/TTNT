import numpy as np
import random
import time

# Câu 2 (2 điểm): Cho 4 tọa độ như hình và trả lời các câu hỏi sau:
# a) (1 điểm) Mô tả thuật toán hoặc hàm thực thi thuật toán k-means
# b)  (1 điểm) Nếu sử dụng thuật toán k-means với k = 2 thì kết quả phân nhóm 
# sẽ như thế nào? (các điểm thuộc mỗi nhóm, trọng tâm của mỗi nhóm). 
def calc_time_taken(method):
    def wrapper(*args):
        start = time.time()
        result = method(*args)
        end = time.time()
        print("Time taken: {:.4f} s".format(end - start))
       
    return wrapper


def dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def cal_centroids(clusters, precision):
    centroids = []
    for cluster in clusters:
        ele = len(cluster[0])
        c_item = []
        for i in range(ele):
            c_item.append(round(np.mean([point[i]
                          for point in cluster]), precision))
        centroids.append(c_item)
    return centroids


def compare_lists(list_1, list_2):
    return all(item in list_2 for item in list_1)


@calc_time_taken
def runner(data, k, prec=5):
    indices = random.sample(range(len(data)), k)
    centroids = [data[index] for index in indices]

    counter = 0
    while True:
        counter += 1
        clusters = [[] for _ in range(k)]

        for point in data:
            distances = [dist(point, centroid) for centroid in centroids]
            clusters[np.argmin(distances)].append(point)

        new_centroids = cal_centroids(clusters, prec)
       
        print(centroids)
        print(new_centroids)

        if compare_lists(centroids, new_centroids):
            break

        centroids = new_centroids
        print(counter)

    print(centroids)
    for i, cluster in enumerate(clusters):
        print(cluster)
        print(len(cluster))


if __name__ == '__main__':
    data_set = [[2, 0], [3, 0], [0, 3], [1, 4]]
    k_value = 2
    precision = 5
    runner(data_set, k_value, precision)
