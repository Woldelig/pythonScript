import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

if __name__ == '__main__':

    x = np.array([1, 2, 3])
    x2 = np.array([1, 2])
    y = np.array([1.300, 0.185, 0.029])
    y2 = np.array([1.300, 0.0017])

    plt.plot(x,y, marker='o', color='r')
    plt.plot(x2, y2, marker='o', color='g')
    plt.ylabel('Størrelse i gigabyte')
    plt.axis([0, 4, 0, 1.4])

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