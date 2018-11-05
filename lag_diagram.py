import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

if __name__ == '__main__':

    x = np.array([1, 2, 3])
    x2 = np.array([1, 2])
    y = np.array([4, 0.545, 0.081])
    y2 = np.array([4, 0.0047])

    plt.plot(x,y, marker='o', color='r')
    plt.plot(x2, y2, marker='o', color='g')
    plt.ylabel('Størrelse i gigabyte')
    plt.axis([0, 4, 0, 4.5])

    xl = np.array(['Rådata', 'Script', 'Excel'])
    l1 = mpatches.Patch(color='red', label='Analysedata')
    l2 = mpatches.Patch(color='green', label='Geodata')

    plt.legend(handles= [l1,l2])
    plt.xticks(x, xl)
    plt.xticks(rotation='vertical')
    plt.title('Datareduksjon i rengjøringsfasen')
    plt.tight_layout()
    plt.grid()

    plt.savefig('størrelsesReduksjonGraf.png', dpi=1500)