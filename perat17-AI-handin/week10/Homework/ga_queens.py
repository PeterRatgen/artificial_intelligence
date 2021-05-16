import random
from queens_fitness import fitness_fn_positive


p_mutation = 1
num_of_generations = 150
crossover_rate = 0.9


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation) + " " + str(len(population)))
        #print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population)
            
            if random.uniform(0, 1) < crossover_rate:
                child1, child2 = reproduce(mother, father, fitness_fn)

                if random.uniform(0, 1) < p_mutation:
                    child1 = mutate(child1)

                if random.uniform(0, 1) < p_mutation:
                    child2 = mutate(child2)

                new_population.add(child1)
                new_population.add(child2)

        # Add new population to population, use union to disregard
        # duplicate individuals

        population = population.union(new_population)

        population = prune_population(population)

        fittest_individual = get_fittest_individual(population, sorter)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population)

    return fittest_individual

def sorter(individual):
    return individual[1]


def prune_population(population):
    
    list_population = list(population)

    print("Before: " + str(len(list_population)))

    list_population.sort(key=sorter, reverse = True)

    length = len(list_population)

    if (length > 130 ):
        place = int(1/2 * length) 
    else: 
        place = 130

    list_population = list_population[0: place]
    print("After: " + str(len(list_population)))


    return set(list_population)


        

def print_population(population):
    for individual in population:
        fitness = individual[1]
        print("{} - fitness: {}".format(individual[0], fitness))


def reproduce(mother, father, fitness_fn):
    '''
    Reproduce two individuals with single-point crossover
    Two children are returned.
    '''

    mother = list(mother[0])
    father = list(father[0])
    
    child1 = []
    child2 = []

    crossover = random.randrange(0, len(mother))
    for i in range(len(mother)):
        if i < crossover:
            child1.append(mother[i])
            child2.append(father[i])
        else:
            child1.append(father[i])
            child2.append(mother[i])

    return (tuple(child1), fitness_fn((child1, 0))), (tuple(child2), fitness_fn([child2, 0]))


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''

    mutation = list(individual)

    index = random.randrange(len(mutation))
    if (mutation[index] == 0):
      mutation[index] = 1
    elif (mutation[index] == 1):
      mutation[index] = 0

    return tuple(mutation)


def random_selection(population):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)

    fitness_list = []

    for chromosome in ordered_population:
        fitness_list.append(chromosome[1])

    total_score = sum(fitness_list)

    selected  = []

    for i in range(2):
        r = random.randrange(total_score * 100) / 100
        score_counter = 0
        for chromosome in ordered_population:
            score_counter += chromosome[1]
            if score_counter >= r:
                selected.append(chromosome)
                break

    return selected[0], selected[1]



def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randrange(0, n) for _ in range(n))
        for _ in range(count)
    ])

def calculate_fitness(population, fitness_fn):
    
    pop = list(population)
    setpop = []

    for i in pop:
        setpop.append((i, fitness_fn((i, 0))))

    return set(setpop)



def main():
    minimal_fitness = 28

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary

    initial_population = get_initial_population(8, 8)

    initial_population = calculate_fitness(initial_population, fitness_fn_positive)

    fittest = genetic_algorithm(initial_population, fitness_fn_positive, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " with fitness " + str(fitness_fn_positive(fittest)))


if __name__ == '__main__':
    pass
    main()
