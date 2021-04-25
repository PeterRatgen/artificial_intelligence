import random


p_mutation = 0.3
num_of_generations = 30


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            print("mother " + str(mother) + " father: " + str(father))
            child = reproduce(mother, father)
            print("child " + str(child))

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''

    mother = list(mother)
    father = list(father)

    child = []

    crossover = random.randrange(0, len(mother))
    for i in range(len(mother)):
        if i < crossover:
            child.append(mother[i])
        else:
            child.append(father[i])


    return tuple(child)


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''

    mutation = list(individual)

    i = random.randrange(len(mutation))

    if (mutation[i] == 0):
      mutation[i] = 1
    elif (mutation[i] == 1):
      mutation[i] = 0

    return tuple(mutation)

def random_selection(population, fitness_fn):
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
        fitness_list.append(fitness_fn(chromosome))

    total_score = sum(fitness_list)

    selected  = []

    for i in range(2):
        r = random.randrange(total_score)
        score_counter = 0
        for i in range(len(fitness_list)):
            score_counter += fitness_list[i]
            if score_counter >= r:
                selected.append(ordered_population[i])
                break

    return selected[0], selected[1]


def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual
    '''

    individual = list(individual)

    fitness = 0.0

    if individual[0] == 1:
        fitness += 4
    if individual[1] == 1:
        fitness += 2
    if individual[2] == 1:
        fitness += 2

    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 7

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (1, 1, 0),
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0)
    }
    #initial_population = get_initial_population(3, 4)

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " with fitness " + str(fitness_function(fittest)))


if __name__ == '__main__':
    pass
    main()
