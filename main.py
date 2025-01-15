import csv

class Person:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        if smoker == "yes":
            self.smoker = True
        else:
            self.smoker = False
        self.region = region
        self.charges = charges


def main():
    people = []
    with open("insurance.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for age, sex, bmi, children, smoker, region, charges in reader:
            people.append({
                "age": age, "sex": sex, "bmi": bmi, "children": children, "smoker": smoker, "region":region,
                "charges": charges
            })


if __name__ == "__main__":
    main()