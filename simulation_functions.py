from dataclasses import dataclass
import math
import matplotlib.pyplot as plot
import numpy as np
import random


def one_step(weighted_dgraph,particles,time):
    outparticles = particles
    shell_transfers_from = weighted_dgraph.transfers_from
    for i in range(len(particles)):
        item = particles[i]
        specific_transfers_from = shell_transfers_from[item]
        selected_weight_list = []
        for j in specific_transfers_from:
            scaled_weight = j[2]*time
            selected_weight_list.append(scaled_weight)
        rate_sum = sum(selected_weight_list)
        survival_chance = 1-(math.e)**-rate_sum
        survival_seed = random.random()
        if survival_seed < survival_chance:
            population_indices = range(len(selected_weight_list))
            chosen_index = random.choices(population_indices, weights=selected_weight_list, k=1)[0]
            specific_transfer = specific_transfers_from[chosen_index]
            outparticles[i] = specific_transfer[1]
    return outparticles