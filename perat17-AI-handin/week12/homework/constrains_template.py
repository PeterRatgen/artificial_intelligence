from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result != False:
                    return result
                assignment.pop(var)

        return False


    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_south_america():
    gf, sr, gy, ve, co, ec = 'Guyane (FR)', 'Suriname', 'Guyana', 'Venezuela', 'Colombia', 'Ecuador'
    pe, cl, bo, br, py = 'Peru', 'Chile', 'Bolivia', 'Brazil', 'Paraguay'
    ar, uy = 'Argentina', 'Uruguay'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [gf, sr, gy, ve, co, ec, pe, cl, bo , br, py, ar ,uy]
    domains = {
        gf: values[:],
        sr: values[:],
        gy: values[:],
        ve: values[:],
        co: values[:],
        ec: values[:],
        pe: values[:],
        cl: values[:],
        bo: values[:],
        br: values[:],
        py: values[:],
        ar: values[:],
        uy: values[:],
    }
    neighbours = {
        gf: [sr, br],
        sr: [gf, gy, br],
        gy: [ve, sr, br],
        ve: [co, gy, br],
        co: [ec, pe, ve, br],
        ec: [co, pe],
        pe: [co, ec, br],
        cl: [pe, bo, ar],
        bo: [pe, cl, ar, py],
        br: [gf, sr, gy, ve, co, pe, bo , py, uy],
        py: [bo, ar, uy, br],
        ar: [cl, bo, py, uy],
        uy: [ar, py, br],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        gf: constraint_function,
        sr: constraint_function,
        gy: constraint_function,
        ve: constraint_function,
        co: constraint_function,
        ec: constraint_function,
        pe: constraint_function,
        cl: constraint_function,
        bo: constraint_function,
        br: constraint_function,
        py: constraint_function,
        ar: constraint_function,
        uy: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_south_america()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
