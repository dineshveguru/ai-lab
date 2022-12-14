import numpy as np


def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))


def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_point, centroids[index_of_minimum]]


def compute_new_centroids(cluster_label, centroids):
    return np.array(cluster_label + centroids)/2


def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)

    for iteration in range(0, total_iteration):
        for index_point in range(0, total_points):
            distance = {}
            for index_centroid in range(0, k):
                distance[index_centroid] = compute_euclidean_distance(
                    data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(
                distance, data_points[index_point], centroids)
            centroids[label[0]] = compute_new_centroids(
                label[1], centroids[label[0]])

            if iteration == (total_iteration - 1):
                cluster_label.append(label)

    return [cluster_label, centroids]


def print_label_data(result):
    print("Result of k-Means Clustering: \n")
    for data in result[0]:
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))


def create_centroids():
    centroids = []
    centroids.append([5.0, 0.0])
    centroids.append([45.0, 70.0])
    centroids.append([50.0, 90.0])
    return np.array(centroids)


if __name__ == "__main__":
    # filename = "table_data.csv"
    # data_points = np.genfromtxt(
    #     filename, delimiter=",", usecols=np.arange(0, 1))
    # print(data_points)
    data_points = [[15, 16],
                   [16, 18.5],
                   [17, 20.2],
                   [16.4, 17.12],
                   [17.23, 18.12],
                   [43, 43],
                   [44.43, 45.212],
                   [45.8, 54.23],
                   [46.313, 43.123],
                   [50.21, 46.3],
                   [99, 99.22],
                   [100.32, 98.123],
                   [100.32, 97.423],
                   [102, 93.23],
                   [102.23, 94.23]]
    centroids = create_centroids()
    total_iteration = 100

    [cluster_label, new_centroids] = iterate_k_means(
        data_points, centroids, total_iteration)
    print_label_data([cluster_label, new_centroids])
    print()
