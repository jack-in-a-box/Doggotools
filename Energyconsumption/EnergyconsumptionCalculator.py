#Reference: https://vet.osu.edu/vmc/companion/our-services/nutrition-support-service/basic-calorie-calculator
#The Ohio State University Veterinary Medical Center
# The University studies has been used as a base to create calculations of the energyconsumption and to find the multipliers of energyconsumption according to different lifes of dogs

#RER = Resting energy requirement

def main():

    kilograms = float(input("How much does your dog weigh in kilograms?\n"))
    RER = (kilograms **(3/4)) * 70

    print("My dog is... (choose the most fitting option): ")
    print("1 - Neutered adult")
    print("2 - Intact adult")
    print("3 - Inactive/obese prone")
    print("4 - In need of weight loss")
    print("5 - In need of weight gain")
    print("6 - Active/working dog")
    print("7 - Puppy 0-4 months old")
    print("8 - Puppy 4 months to adult")
    choise = int(input("Enter your choise as an integer between 1 to 8: "))
    if choise == 1:
        multiplier = 1.6
        energyconsumption = multiplier * RER
        print("Your dog's energy consumption is {:.2f} kcal per day".format(energyconsumption))
    elif choise == 2:
        multiplier = 1.8
        energyconsumption = multiplier * RER
        print("Your dog's energy consumption is {:.2f} kcal per day".format(energyconsumption))
    elif choise == 3:
        multiplierlow = 1.2
        multiplierhigh = 1.4
        energyconsumptionlow = multiplierlow * RER
        energyconsumptionhigh = multiplierhigh * RER
        print("Your dog's energyconsumption is between {:.2f} kcal and {:.2f} kcal per day".format(energyconsumptionlow,energyconsumptionhigh))

    elif choise == 4:
        multiplier = 1
        energyconsumption = multiplier * RER
        print("Your dog's energy consumption is {:.2f} kcal per day".format(energyconsumption))
    elif choise == 5:
        multiplierlow = 1.2
        multiplierhigh = 1.8
        energyconsumptionlow = multiplierlow * RER
        energyconsumptionhigh = multiplierhigh * RER
        print("Your dog's energyconsumption is between {:.2f} kcal and {:.2f} kcal per day".format(energyconsumptionlow,
                                                                                           energyconsumptionhigh))
    elif choise == 6:
        multiplierlow = 2
        multiplierhigh = 5
        energyconsumptionlow = multiplierlow * RER
        energyconsumptionhigh = multiplierhigh * RER
        print("Your dog's energyconsumption is between {:.2f} kcal and {:.2f} kcal per day".format(energyconsumptionlow,
                                                                                           energyconsumptionhigh))
    elif choise == 7:
        multiplier = 3
        energyconsumption = multiplier * RER
        print("Your dog's energy consumption is {:.2f} kcal per day".format(energyconsumption))
    elif choise == 8:
        multiplier = 2
        energyconsumption = multiplier * RER
        print("Your dog's energy consumption is {:.2f} kcal per day".format(energyconsumption))

main()
