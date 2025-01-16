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
            print("No age data to analyze.")
            return
        
        # Mean analysis
        age_mean = sum(self.age) / len(self.age)
        print(f"Age mean: {age_mean}")

        # Median analysis
        ages_sorted = sorted(self.age)
        print(f"Age median: {self._calc_median(ages_sorted):.2f}")

        #Standard deviation analysis
        print(f"Age standard deviation: {self._calc_std_deviation(self.age, age_mean):.2f}")



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
    except FileNotFoundError:
        print("The file 'insurance.csv' was not found")
    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    main()