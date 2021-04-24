import random
from queens_fitness import fitness_fn_positive


p_mutation = 0.3
num_of_generations = 20


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation) + " " + str(len(population)))
        #print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            #print("mother " + str(mother) + " father: " + str(father))
            child1, child2 = reproduce(mother, father)
            #print("child " + str(child))

            if random.uniform(0, 1) < p_mutation:
                child1 = mutate(child1)

            if random.uniform(0, 1) < p_mutation:
                child2 = mutate(child2)

            new_population.add(child1)
            new_population.add(child2)

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
    Two children are returned.
    '''

    mother = list(mother)
    father = list(father)

    child1 = []
    child2 = []

    if random.random() < 0.9:
        crossover = random.randrange(0, len(mother))
        for i in range(len(mother)):
            if i < crossover:
                child1.append(mother[i])
                child2.append(father[i])
            else:
                child1.append(father[i])
                child2.append(mother[i])
    else:
        child = mother


    return tuple(child1), tuple(child2)


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''

    mutation = list(individual)

    for i in range(len(mutation)):
      if (random.random() < 0.05):
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
        r = random.randrange(total_score * 100) / 100
        score_counter = 0
        for i in range(len(fitness_list)):
            score_counter += fitness_list[i]
            if score_counter >= r:
                selected.append(ordered_population[i])
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


def main():
    minimal_fitness = 28

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary

    initial_population = get_initial_population(8, 2)

    #print(fitness_fn_positive((7, 1, 3, 0, 6, 4, 2, 5)))

    fittest = genetic_algorithm(initial_population, fitness_fn_positive, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " with fitness " + str(fitness_fn_positive(fittest)))


if __name__ == '__main__':
    pass
    main()
