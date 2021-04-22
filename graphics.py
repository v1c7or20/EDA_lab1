import matplotlib.pyplot as plt
import numpy

index = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 50000]
# microsegundos, dataset probado en c++ min heap
ds_cpp_a = [29384, 29431, 32215, 30562, 28560, 27838, 27930, 29165, 27668, 29015, 43173, 30857, 34220, 55707, 75645, 104426, 98433]
ds_cpp_b = [25480, 31097, 36528, 24132, 30283, 42496, 40451, 30954, 30839, 30584, 26401, 34652, 37395, 38218, 67875, 82416, 142165]
ds_cpp_c = [34995, 36619, 33353, 31709, 35642, 32527, 34621, 29734, 28985, 54567, 50711, 56861, 46009, 65375, 79251, 79411, 113009]
# segundos, dataset probado en python sklearn
ds_py_a = [0.1121, 0.108, 0.1114, 0.115, 0.1074, 0.1165, 0.1085, 0.1105, 0.1147, 0.1233, 0.1114, 0.1134, 0.1088, 0.1193, 0.1206, 0.0939, 0.1459]
ds_py_b = [0.1139, 0.1092, 0.1158, 0.1187, 0.1185, 0.1146, 0.1133, 0.1116, 0.1233, 0.1183, 0.1151, 0.1125, 0.1126, 0.122, 0.1223, 0.0984, 0.1504]
ds_py_c = [0.1146, 0.1128, 0.1118, 0.1208, 0.1128, 0.1153, 0.1132, 0.1144, 0.1131, 0.1254, 0.1139, 0.1118, 0.1189, 0.113, 0.1132, 0.1022, 0.1596]

for i in range(0, len(ds_cpp_a)):
  ds_cpp_a[i] = ds_cpp_a[i]/1000
  ds_cpp_b[i] = ds_cpp_b[i]/1000
  ds_cpp_c[i] = ds_cpp_c[i]/1000
  ds_py_a[i] = ds_py_a[i]*1000
  ds_py_b[i] = ds_py_b[i]*1000
  ds_py_c[i] = ds_py_c[i]*1000

def generate_graph(x, y, y_, path):
  fig, ax = plt.subplots(figsize=(10,5))
  z = numpy.polyfit(x, y, 1)
  p = numpy.poly1d(z)
  ax.plot(x,p(x),"r--", color="red", linestyle="solid", label="Tendencia del Min Heap")
  z = numpy.polyfit(x, y_, 1)
  p = numpy.poly1d(z)
  ax.plot(x,p(x),"r--", color="blue", linestyle="solid", label="Tendencia de Scikit-learn")

  ax.plot(x, y, linestyle="dashed", color="red", label="C++: Min Heap")
  ax.plot(x, y_, linestyle="dashed", color="blue", label="Python: Scikit-learn")

  ax.set_xlabel("k vecinos", fontdict = {'fontsize':14})
  ax.set_ylabel("Tiempo (ms)", fontdict = {'fontsize':14})
  plt.legend(bbox_to_anchor=(0.8, 0.4),
            bbox_transform=plt.gcf().transFigure, prop={"size":12})
  plt.savefig(path)
  plt.show()

generate_graph(index, ds_cpp_a, ds_py_a, "datasetA.png")
generate_graph(index, ds_cpp_b, ds_py_b, "datasetB.png")
generate_graph(index, ds_cpp_c, ds_py_c, "datasetC.png")