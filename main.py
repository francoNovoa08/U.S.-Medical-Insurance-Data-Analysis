import csv

class InsuranceData:
    def __init__(self, people):
        self.age = []
        self.sex = []
        self.bmi = []
        self.children = []
        self.smoker = []
        self.region = []
        self.charges = []
        
        for person in people:
            self.age.append(int(person["age"]))
            self.sex.append(person["sex"])
            self.bmi.append(float(person["bmi"]))
            self.children.append(int(person["children"]))
            self.smoker.append(person["smoker"] == "yes")
            self.region.append(person["region"])
            self.charges.append(float(person["charges"]))

    
    def _calc_median(self, ordered_list):
        list_len = len(ordered_list)
        mid = list_len // 2
        if list_len % 2 == 0:
            # Even list
            return (ordered_list[mid - 1] + ordered_list[mid]) / 2
        else:
            # Odd list
            return ordered_list[mid]
        
    
    def _calc_std_deviation(self, list, list_mean):
        difference_mean_values = 0
        for item in list:
            difference_mean_values += (item - list_mean) ** 2
        
        return (difference_mean_values / len(list)) ** 0.5

    
    def analyse_age(self):
        if not self.age:
            print("No age data to analyse.")
            return
        
        # Mean analysis
        age_mean = sum(self.age) / len(self.age)
        print(f"Age mean: {age_mean:.2f}")

        # Median analysis
        ages_sorted = sorted(self.age)
        print(f"Age median: {self._calc_median(ages_sorted):.2f}")

        #Standard deviation analysis
        print(f"Age standard deviation: {self._calc_std_deviation(self.age, age_mean):.2f}")
    

    def analyse_bmi(self):
        if not self.bmi:
            print("No BMI data to analyse.")
            return
        
        # Mean analysis
        bmi_mean = sum(self.bmi) / len(self.bmi)
        print(f"BMI mean: {bmi_mean:.2f}")

        # Median analysis
        bmi_sorted = sorted(self.bmi)
        print(f"BMI median: {self._calc_median(bmi_sorted):.2f}")

        #Standard deviation analysis
        print(f"BMI standard deviation: {self._calc_std_deviation(self.age, bmi_mean):.2f}")


    def analyse_children(self):
        if not self.children:
            print("No children data to analyze.")
            return
        
        # Mean analysis
        children_mean = sum(self.children) / len(self.children)
        print(f"Mean number of children: {children_mean:.2f}")

        # Median analysis
        children_sorted = sorted(self.children)
        print(f"Median number of children: {self._calc_median(children_sorted):.2f}")

        #Standard deviation analysis
        print(f"Number of children standard deviation: {self._calc_std_deviation(self.children, children_mean):.2f}")


    def analyse_charges(self):
        if not self.charges:
            print("No insurance charges data to analyze.")
            return
        
        # Mean analysis
        charges_mean = sum(self.charges) / len(self.charges)
        print(f"Mean insurance cost: {charges_mean:.2f}")

        # Median analysis
        charges_sorted = sorted(self.charges)
        print(f"Median insurance cost: {self._calc_median(charges_sorted):.2f}")

        #Standard deviation analysis
        print(f"Insurance cost standard deviation: {self._calc_std_deviation(self.age, charges_mean):.2f}")


    def analyse_sex(self):
        if not self.sex:
            print(f"No sex data to analyse")
            return
        
        # Count
        male_count = 0
        female_count = 0
        for person in self.sex:
            if person == "male":
                male_count += 1
            else:
                female_count += 1
        
        print(f"Male count: {male_count}")
        print(f"Female count: {female_count}")
        print(f"Male percentage: {male_count * 100 / len(self.sex):.2f}")
        print(f"Female percentage: {female_count * 100 / len(self.sex):.2f}")


    def analyse_smoker(self):
        if not self.smoker:
            print("No smoker data to analyse")
            return
        
        # Count
        smoker_count = 0
        non_smoker_count = 0
        for person in self.smoker:
            if person:
                smoker_count += 1
            else:
                non_smoker_count += 1
        
        print(f"Smoker count: {smoker_count}")
        print(f"Non-smoker count: {non_smoker_count}")
        print(f"Smoker percentage: {smoker_count * 100 / len(self.smoker):.2f}")
        print(f"Non-smoker percentage: {non_smoker_count * 100 / len(self.smoker):.2f}")


    def analyse_region(self):
        if not self.region:
            print("No region data to analyse")
            return
        
        # Count
        nw_count = 0
        ne_count = 0
        sw_count = 0
        se_count = 0
        for person in self.region:
            match person:
                case "northwest":
                    nw_count += 1
                case "northeast":
                    ne_count += 1
                case "southwest":
                    sw_count += 1
                case "southeast":
                    se_count += 1
        
        print(f"Northwest count: {nw_count}")
        print(f"Northwest percentage: {nw_count * 100 / len(self.region):.2f}")
        print(f"Northeast count: {ne_count}")
        print(f"Northeast percentage: {ne_count * 100 / len(self.region):.2f}")
        print(f"Southwest count: {sw_count}")
        print(f"Southwest percentage: {sw_count * 100 / len(self.region):.2f}")
        print(f"Southeast count: {se_count}")
        print(f"Southeast percentage: {se_count * 100 / len(self.region):.2f}")


def main():
    people = []
    try:
        with open("insurance.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                people.append(row)

        if not people:
            print("No data in CSV")
            return
    
        data = InsuranceData(people)
        data.analyse_age()
        data.analyse_bmi()
        data.analyse_children()
        data.analyse_charges()
        data.analyse_sex()
        data.analyse_smoker()
        data.analyse_region()
    except FileNotFoundError:
        print("The file 'insurance.csv' was not found")
    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    main()