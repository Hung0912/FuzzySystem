import numpy as np
import matplotlib.pyplot as plt
import fuzzylogic as fuzz

#Input Universe functions
height = np.arange(1.35, 2.0, 0.05)
weight = np.arange(30, 90, 5)

#Input membership functions
#Height
short = fuzz.gaussian2(height, 1.40, 2.0)
average = fuzz.gaussian2(height, 1.65, 2.0)
tall = fuzz.gaussian2(height, 1.8, 2.0)
#Weight
skin = fuzz.triangular2(weight, 30, 50, 65)
fat = fuzz.triangular2(weight, 50, 70, 90)

#Output Universe
size = np.arange(0, 10, 0.1)
#Output membership function
sizeS = fuzz.triangular2(size, 0, 2, 5)
sizeM = fuzz.triangular2(size, 4, 6, 8)
sizeL = fuzz.triangular2(size, 6, 8, 10)

#Apply inputs
def height_category(height_in):
    height_cat_tall = fuzz.gaussian(height_in, 1.8, 0.5)
    height_cat_average = fuzz.gaussian(height_in, 1.65, 0.5)
    height_cat_short = fuzz.gaussian(height_in, 1.40, 0.5)
    return dict(short = height_cat_short, average = height_cat_average, tall = height_cat_tall)

def weight_category(weight_in):
    weight_cat_skin = fuzz.triangular(weight_in, 30., 50., 65.)
    weight_cat_fat = fuzz.triangular(weight_in, 50., 70., 90.)
    return dict(skin = weight_cat_skin, fat = weight_cat_fat)

person1 = {
    "name": "Hung",
    "height": 1.69,
    "weight": 60
}

rules = [
    #if height is short and weight is thin then size S

    #if height is short or weight is fat then size M

    #if height is short, weight is thin then size S

    #if height is short, weight is thin then size S

    #if height is short, weight is thin then size S
]
#main
if __name__ == '__main__':
    print("Hello " + person1["name"])
    print "for height: ", height_category(person1["height"])
    print "for weight: ", weight_category(person1["weight"])
    