import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#membership function
def triangular(x, a, b, c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)), 0)

# define Universe of Discourse
U = np.arange(25,220,1)

height = {
    'Very Small': [25.0, 25.1, 50.0],
    'Small': [25., 50., 75.],
    'Short': [50., 90., 130.],
    'Medium': [90., 130., 175.],
    'High': [130., 175., 220.],
    'Very High': [175., 220., 220.1]    
}

# plt.figure(figzise = (15,7))

lines = []

for key in height.keys():
    memberships = [triangular(x, *height[key]) for x in U]
    #plot the chart
    tmp, = plt.plot(U, memberships, label = key)
    lines.append(tmp)

def showPlot():
    # plt.legend(handles= lines)
    plt.xl                 abel("Height")
    plt.ylabel("Membership value")
    plt.show()

def test(h):
    print("with heihgt %.1f"%h)
    for key in height.keys():
        # print(height[key])   
        print(key,triangular(h, *height[key]))

if __name__ == '__main__':
    test(163)
    showPlot()