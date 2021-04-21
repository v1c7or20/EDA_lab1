from sklearn.neighbors import KNeighborsClassifier
import time

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

read_dataset("d1.txt")
k = int(input("Numero de vecinos: "))
inp = input("Ingresa coordenadas separadas por espacio: ")
x, y = inp.split()
total_time = time.time()
model = KNeighborsClassifier(n_neighbors=k)
fit_time = time.time()
model.fit(features,labels)
fit_time = time.time() - fit_time
knn_time = time.time()
predicted= model.kneighbors([[int(x), int(y)]])
knn_time = time.time() - knn_time
total_time = time.time() - total_time
print("--- Fit time: %s seconds ---" % (fit_time))
print("--- KNN time: %s seconds ---" % (knn_time))
print("--- Total time: %s seconds ---" % (total_time))
for prediction in predicted[1][0]:
    print(labels[prediction])
