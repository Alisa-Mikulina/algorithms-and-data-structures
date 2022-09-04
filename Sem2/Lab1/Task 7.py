def problem_solver(day_ln, num_boots, boots):
    ordered_boots = sorted(boots)
    how_many = 0
    time_taken = 0
    for i in range(num_boots):
        if time_taken + ordered_boots[i] >= day_ln:
            return how_many
        time_taken += ordered_boots[i]
        how_many += 1
        if how_many == num_boots:
            return how_many


with open ("input_7.txt") as f:
    day_ln, num_boots = f.readline().split()
    day_ln, num_boots = int(day_ln), int(num_boots)
    boots = f.readline().split()
    for i in range(num_boots):
        boots[i] = int(boots[i])

solution = problem_solver(day_ln, num_boots, boots)
print(solution)
