# pip3 install matplotlib
import matplotlib.pyplot as plt


def chineseFont():
    # Set font to a Chinese-supporting font
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] 
    plt.rcParams['axes.unicode_minus'] = False  # Fix negative sign display issue

    # Example plot
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.title('中文標題')  # Chinese title
    plt.xlabel('X軸')      # Chinese x-axis label
    plt.ylabel('Y軸')      # Chinese y-axis label
    plt.show()


if __name__ == '__main__':
    language()
    # plt.scatter(10, 10, c='b',label="a")
    # plt.scatter(20, 20, c='g',label="b")
    # plt.scatter(25, 25, c='g',s=30,label="b")
    # plt.xlabel("Average Pulse")
    # plt.ylabel("Calorie Burnage")
    # handles, labels = plt.gca().get_legend_handles_labels()
    # legendLabel = dict(zip(labels, handles))
    # plt.legend(legendLabel.values(), legendLabel.keys())
    # plt.show()