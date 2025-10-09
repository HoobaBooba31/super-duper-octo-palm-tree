import matplotlib.pyplot as plt
import numpy as np


def results_from_py():
    with open('analyse_results.txt', 'r', encoding='utf-8') as file:
        file.readline()
        
        axis =[[],[],[]]

        for line in file:
            theta, d_times, d_db = map(float, file.readline().split())
            axis[0].append(theta)
            axis[1].append(d_db)
            axis[2].append(d_times)
        
        return axis


def results_from_CST():
    with open('resFF.txt', 'r', encoding='utf-8') as file:
        file.readline()
        file.readline()

        axis = [[],[],[]]

        for line in file:
            Theta, Phi, Direction, d_db, Phase, Phi, Phase_Phi, Ratio = map(float, file.readline().split())
            axis[0].append(np.deg2rad(Theta))
            axis[1].append(d_db)
            axis[2].append(10**(d_db/10))
        
        return axis


def creating_plot(cst, python):
        
    fig = plt.figure(figsize=(12, 10))
    fig.suptitle('Difference between\nPython and CST')


    ax1 = fig.add_subplot(2, 2, 1)  
    ax2 = fig.add_subplot(2, 2, 2)  

    ax1.plot(cst[0], cst[1], label='CST')
    ax1.plot(python[0], python[1], label='Python')
    ax1.set_title('D, dBi')
    ax1.set_xlabel("Theta")
    ax1.set_ylabel("dBi")
    ax1.grid(True)
    ax1.legend()

    ax2.plot(cst[0], cst[2], label='CST')
    ax2.plot(python[0], python[2], label='Python')
    ax2.set_title('D, times')
    ax2.set_xlabel("Theta")
    ax2.set_ylabel("times")
    ax2.grid(True)
    ax2.legend()

    ax3 = fig.add_subplot(2, 2, 3, polar=True)
    ax4 = fig.add_subplot(2, 2, 4, polar=True)

    ax3.plot(cst[0], cst[1], label='CST')
    ax3.plot(python[0], python[1], label='Python')
    ax3.set_title('D, dBi (polar)')
    ax3.grid(True)
    ax3.legend()

    ax4.plot(cst[0], cst[2], label='CST')
    ax4.plot(python[0], python[2], label='Python')
    ax4.set_title('D, times (polar)')
    ax4.grid(True)
    ax4.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
    plt.savefig("task2var1.png")


def main():
    creating_plot(cst=results_from_CST(), python=results_from_py())


if __name__=='__main__':
    main()

