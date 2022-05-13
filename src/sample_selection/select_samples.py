import random as rd
import csv

# total numbers of students in each grade level
N_09 = 337
N_10 = 311
N_11 = 308
N_12 = 358
N_ALL = [N_09, N_10, N_11, N_12]
N_TOTAL = sum(N_ALL)

class Student:
    """Student class."""

    def __init__(self, index: int, grade: int, gr_index: int):
        """Student constructor.
        
        Takes in 0-based indices, and creates an object with 1-based indices and zero-based indices."""

        self.zero_based_index = index
        self.index = index + 1
        self.grade = grade
        self.zero_based_gr_index = gr_index
        self.gr_index = gr_index + 1

def population_data_from_csv(path: str) -> list[Student]:
    _population = []
    with open(path, "r") as _file:
        _reader = csv.reader(_file)
        for i, row in enumerate(_reader):
            _population.append(Student(i, int(row[1]), int(row[2])))
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
    _samples = []
    for grade in grade_populations:
        _samples.append(rd.sample(grade, 30))

def check_samples(samples: list[list[int]]): # redo once the new system is set up
    for i in range(len(samples)):
        for j in range(len(samples[i])):
            _gr_c = lambda x: x + 9
            _gr = _gr_c(i)
            _br = False
            while (not _br):
                _res = input(f"{str(_gr).zfill(2)}-{samples[i][j]} (j+1: {j+1}) ok? (y/n) ")
                if _res.lower() == "n":
                    samples[i][j] = rd.randint(1, N_ALL[i])
                elif _res.lower() == "y":
                    _br = True
                elif _res.lower() != "n" and _res.lower() != "y":
                    print("Invalid input")

if __name__ == "__main__":
    samples = generate_samples(N_ALL, 30)
    check_samples(samples)
    with open("../../data/samples/samples.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(samples)
