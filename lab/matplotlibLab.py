import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.scatter(10, 10, c='b',label="a")
    plt.scatter(20, 20, c='g',label="b")
    plt.scatter(25, 25, c='g',s=30,label="b")
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")
    handles, labels = plt.gca().get_legend_handles_labels()
    legendLabel = dict(zip(labels, handles))
    plt.legend(legendLabel.values(), legendLabel.keys())
    plt.show()