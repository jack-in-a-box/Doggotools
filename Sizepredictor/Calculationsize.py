# Reference:WALTHAM International Science Symposium: Nature, Nurture, and the Case for Nutrition
# Body-Weight Changes during Growth in Puppies of Different Breeds1
# Amanda J. Hawthorne,2 Derek Booles, Pat A. Nugent, George Gettinby,* and Joy Wilkinson
# WALTHAM Centre for Pet Nutrition, Waltham-on-the-Wolds, Leicestershire, UK and *Department of Statistics and Modelling Science, University of Strathclyde, Glasgow, UK
#Waltham has been used as a base for the mathematical equation to calculate the dog's size and to form the different factors from averages of the research results

import math
import numpy as np
import matplotlib.pyplot as plt

# growthfactor = "1/b"; average calculated; variation not taken in consideration; giant class includes great dane, irish wolfhound and newfoundland; St.Bernard and english mastiff has been included in large with labrador retriever
# agefactor = x0, average calculated; variation not taken in consideration
# a = adult weight, unknown factor

def calculate_weight(adultweight, growthfactor, agefactor, age):
    return adultweight / (1 + math.exp(-(age - agefactor) / (1 / growthfactor)))

def calculate_adultweight(agefactor,growthfactor,weight,age):
    adultweight = weight
    delta = weight
    upper_found = False
    epsilon = 0.01

    while True:
        testweight = calculate_weight(adultweight, growthfactor, agefactor, age)
        #print("if adult weight is {:.2f}, weight at {:.0f} weeks would be {:.2f} kg (actual {:.2f} kg)".format(adultweight, age, testweight, weight))

        if abs(testweight - weight) < epsilon:
            return adultweight
        elif testweight < weight and not upper_found:
            delta = delta * 2
            adultweight = adultweight + delta
        elif testweight < weight and upper_found:
            delta = delta / 2
            adultweight = adultweight + delta
        elif testweight > weight:
            upper_found = True
            delta = delta / 2
            adultweight = adultweight - delta

def bodyweights(a, b_inv, x0):
    return lambda x: a / (1 + math.exp(-(x - x0) / (1 / b_inv)))

def main():
    weight = 0
    while weight <= 0:
        try:
            weight = float(input("What is your dog's weight in kg?\n"))
            if weight <= 0:
                print("Your dog's weight must be more than 0 kg")
        except:
            print("Please, insert integer or desimal numbers only")
    age = 0
    while age >= 78 or age <= 0:
        try:
            age = float(input("What is your dog's age in weeks?\n"))
            if age >= 78:
                print("Error in dog's age, your dog is most definitely already the size it will be as an adult, try again with another age in weeks")
            elif age <= 0:
                print("Error in dog's age, your dog must be more than 0 weeks old")
        except:
            print("Please, enter integer or desimal number only")

    print("What predictive size describes your dog the most? As an adult your dog would be...")
    print("1 - Toy size")
    print("2 - Small")
    print("3 - Medium")
    print("4 - Large")
    print("5 - Giant")
    dogfactor = 0
    while dogfactor < 1 or  dogfactor >5:
        try:
            dogfactor = int(input("Give the closest describing size-category as an integer:\n"))
        except:
            print("Enter integer between 1 and 5")
    if dogfactor == 1:
        growthfactor = 15
        agefactor = 11.1
    elif dogfactor == 2:
        growthfactor = 16.37
        agefactor = 15.4
    elif dogfactor == 3:
        growthfactor = 17.65
        agefactor = 14.55
    elif dogfactor == 4:
        growthfactor = 12.6
        agefactor = 21.13
    else:
        growthfactor = 15.17
        agefactor = 18.57

    growthfactor = growthfactor / 100
    adultsize = calculate_adultweight(agefactor, growthfactor, weight, age)
    print("Your dog's adultsize should be {:.2f}".format(adultsize))

#plotting
    data_x = np.linspace(0, 80, 100)
    data_y = np.vectorize(bodyweights(adultsize, growthfactor, agefactor))(data_x)
    plt.plot(data_x, data_y)
    plt.title("Your dog's growthrate until adultsize")
    plt.ylabel("Dog's weight in kg")
    plt.xlabel("Dog's age in weeks")
    plt.grid(True)
    plt.gca().minorticks_on()
    plt.gca().locator_params(tight=True, nbins=16)
    plt.show()

main()
