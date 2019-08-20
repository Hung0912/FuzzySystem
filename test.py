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
light = fuzz.triangular2(weight, 30, 50, 65)
heavy = fuzz.triangular2(weight, 50, 70, 90)

#Output Universe
BMI = np.arange(0, 50, 0.1)
#Output membership function
under_weight = fuzz.triangular2(BMI, 0., 8., 20.)
normal = fuzz.triangular2(BMI, 18.0, 21.0, 27.0)
over_weight = fuzz.triangular2(BMI, 25.0, 27.0, 33.0)
obese = fuzz.triangular2(BMI, 30.0, 32.0, 38.0)
extremly_obese = fuzz.triangular2(BMI, 35.0, 40.0, 50.0)

#Fuzzy inputs
def height_category(height_in):
    height_cat_tall = fuzz.gaussian(height_in, 1.8, 0.2)
    height_cat_average = fuzz.gaussian(height_in, 1.65, 0.2)
    height_cat_short = fuzz.gaussian(height_in, 1.40, 0.2)
    return dict(short = height_cat_short, average = height_cat_average, tall = height_cat_tall)

def weight_category(weight_in):
    weight_cat_light = fuzz.gaussian(weight_in, 40, 10)
    weight_cat_heavy = fuzz.gaussian(weight_in, 70, 10)
    return dict(light = weight_cat_light, heavy = weight_cat_heavy)

#Fuzzy outputs
def bmi_category(bmi_in):
    bmi_under_weight = fuzz.triangular(bmi_in, 0., 8., 20.)
    bmi_normal = fuzz.triangular(bmi_in, 18.0, 21.0, 27.0)
    bmi_over_weight = fuzz.triangular(bmi_in, 25.0, 27.0, 33.0)
    bmi_obese = fuzz.triangular(bmi_in, 30.0, 32.0, 38.0)
    bmi_extremly_obese = fuzz.triangular(bmi_in, 35.0, 40.0, 50.0)
    return dict(under_weight = bmi_under_weight, normal = bmi_normal, over_weight = bmi_over_weight, obese = bmi_obese, extremly_obese = bmi_extremly_obese)


class Person:
    name = str()
    height = float()
    weight = float()

    def __init__(self, name, height, weight):
        self.name = name
        self.weight = weight
        self.height = height
    
    def getBMI(self):
        return self.weight/(self.height * self.height)

#RULES
rules = [
    #if height is short and weight is light then 

    #if height is short or weight is heavy then 

    #if height is average, weight is light then 

    #if height is average, weight is heavy then 

    #if height is tall, weight is light then 

    #if height is tall, weight is heavy then 
]

#Define MF of fuzzy relation beetween height, short and result
 

def print_result(person):
    print("----------Hello " + person.name + "-------------")
    print "For height: ", height_category(person.height)
    print "For weight: ", weight_category(person.weight)
    print "BMI: ", person.getBMI()
    print "For BMI", bmi_category(person.getBMI())

#main
if __name__ == '__main__':
    person1 = Person("Hung", 1.4, 90)
    print_result(person1)
    
