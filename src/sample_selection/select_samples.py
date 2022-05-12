import random as rd
import csv

# total numbers of students in each grade level
N_09 = 337
N_10 = 311
N_11 = 308
N_12 = 358
N_ALL = [N_09, N_10, N_11, N_12]
N_TOTAL = sum(N_ALL)

def generate_samples(counts: list[int], n: int):
    samples = []
    for i in range(len(counts)):
        samples.append(rd.sample([i+1 for i in range(counts[i])], 30))
    
    return samples

def check_samples(samples: list[list[int]]):
    for i in range(len(samples)):
        for j in range(len(samples[i])):
            pass
