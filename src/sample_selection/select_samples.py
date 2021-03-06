import random as rd
import csv
import sys

# total numbers of students in each grade level
N_09 = 337
N_10 = 311
N_11 = 308
N_12 = 358
N_ALL = [N_09, N_10, N_11, N_12]
N_TOTAL = sum(N_ALL)

class Student:
    def __init__(self, index: int, grade: int, gr_index: int):
        self.index = index
        self.grade = grade
        self.gr_index = gr_index

def population_data_from_csv(path: str) -> list[Student]:
    _population = []
    with open(path, "r") as _file:
        _reader = csv.reader(_file)
        for i, row in enumerate(_reader):
            if i == 0:
                continue    
            _population.append(Student(int(row[0]), int(row[1]), int(row[2])))
    for student in _population:
        if student.grade == 8:
            _population.remove(student)
    return _population

def grade_populations_from_population(population: list[Student]) -> list[list[Student]]:
    _populations = [[], [], [], []]
    for student in population:
        _populations[student.grade - 9].append(student)
    return _populations

def generate_samples(grade_populations: list[list[Student]]) -> list[list[Student]]:
    _samples: list[list[Student]] = []
    for grade in grade_populations:
        _samples.append(sorted(rd.sample(grade, 30), key=lambda s: s.index))
    return _samples

def check_samples(samples: list[list[Student]], grade_populations: list[list[Student]]) -> list[list[Student]]:
    _samples = samples
    for sample in _samples:
        for i, student in enumerate(sample):
            _student = student
            _br = False
            while not _br:
                _br = False
                _res = input(f"{str(_student.grade).zfill(2)}-{str(_student.gr_index).zfill(3)}: {_student.index} ok? (y/n) ")
                _res = _res.lower().strip()
                if _res == "y":
                    _br = True
                elif _res == "n":
                    _samples[_samples.index(sample)][i] = rd.choice(grade_populations[_samples.index(sample)])
                    _student = _samples[_samples.index(sample)][i]
                else:
                    print("Invalid input.")
    return _samples

index_lists_from_samples: list[list[int]] = lambda samples_checked: [list(map(lambda s: s.index, sample)) for sample in samples_checked]

if __name__ == "__main__":
    population_data = population_data_from_csv("../../data/students/population.csv")
    grade_populations = grade_populations_from_population(population_data)
    samples = generate_samples(grade_populations)
    if len(sys.argv) == 1:
        print("usage: python select_samples.py <check|auto>")
        exit(-1)
    elif sys.argv[1] == "check" or sys.argv[1] == "c":
        samples_checked = check_samples(samples, grade_populations)
        indices = index_lists_from_samples(samples_checked)
    elif sys.argv[1] == "auto" or sys.argv[1] == "a":
        indices = index_lists_from_samples(samples)
    else:
        print("Invalid input.")
        exit(-1)

    with open("../../data/samples/samples.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(indices)
    
    print("Samples saved to data/samples/samples.csv.")
