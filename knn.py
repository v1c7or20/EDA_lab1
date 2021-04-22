from sklearn.neighbors import KNeighborsClassifier
import time
import random
features = []
labels = []
def read_dataset(name):
    f = open(name, "r")
    for i in f:
        x, y = i.split()
        point = [int(x), int(y)]
        features.append(point)
        labels.append(x+", "+y)
    f.close()

read_dataset("dataset_a.txt")
#k = int(input("Numero de vecinos: "))
tests = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 50000]
for k in tests:
    x = random.randint(0, 1500)
    y = random.randint(0, 1500)
    total_time = time.time()
    model = KNeighborsClassifier(n_neighbors=k)
    fit_time = time.time()
    model.fit(features,labels)
    fit_time = time.time() - fit_time
    knn_time = time.time()
    predicted= model.kneighbors([[x, y]])
    knn_time = time.time() - knn_time
    total_time = time.time() - total_time
    #print("--- Fit time: %s seconds ---" % (fit_time))
    #print("--- KNN time: %s seconds ---" % (knn_time))
    #print("--- Total time: %s seconds ---" % (total_time))
    print(total_time, end=", ")
#for prediction in predicted[1][0]:
 #   print(labels[prediction])
