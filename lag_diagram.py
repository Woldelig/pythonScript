import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.array([1, 2, 3])
    y = np.array([1.300, 0.185, 0.029])
    plt.plot(x,y, marker='o', color='r')
    plt.ylabel('Størrelse i gigabyte')
    plt.axis([0, 4, 0, 1.4])
    xl = np.array(['Rådata', 'Script', 'Excel'])
    plt.xticks(x, xl)
    plt.xticks(rotation='vertical')
    plt.title('Filstørrelses reduksjon i rengjøringsfasen')
    plt.tight_layout()

    plt.savefig('størrelsesReduksjonGraf.png', dpi=1500)