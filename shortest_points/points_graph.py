import matplotlib.pyplot as plt

# x = []
# y = []

# with open('shortest_points_0to100000.txt','r') as f:
#     data = f.readlines()
#     for line in data:
#         x.append(int(line.split(",")[0]))
#         y.append(float(line.split(",")[1].split(" ")[1].split("\n")[0]))

# plt.semilogy(x[1:],y[1:],"kx")
# plt.xlabel("k")
# plt.ylabel("d(k)")
# plt.show()
with open('distances_2mil.txt','r') as f:
    data = f.readlines()

print(data)