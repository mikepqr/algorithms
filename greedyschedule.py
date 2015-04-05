def read_jobs(file):
    j = []
    with open(file, 'r') as f:
        next(f)	 # discard first line
        for i, l in enumerate(f):
            weight, length = int(l.split()[0]), int(l.split()[1])
            j.append([weight, length])
    return j


def bad_score_jobs(jobs):
    for j in jobs:
        j.append(j[0] - j[1])

    return jobs


def score_jobs(jobs):
    for j in jobs:
        j.append(float(j[0])/j[1])

    return jobs


def sort_jobs(jobs):
    # Goal is to sort on score (decreasing), using weight as a tie-breaker
    sorted_jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    sorted_jobs = sorted(sorted_jobs, key=lambda x: x[2], reverse=True)
    return sorted_jobs


def calculate_completion_times(jobs):
    c = 0
    for j in jobs:
        c += j[1]
        j.append(c)

    return jobs


def sum_weighted_completion_times(jobs):
    s = 0
    for j in jobs:
        s += j[0] * j[3]

    return s


def solve_question(filename='scheduling_tests/jobs.txt', question=1):
    if question == 1:
        score_function = bad_score_jobs
    else:
        score_function = score_jobs

    jobs = read_jobs(filename)
    jobs = score_function(jobs)
    jobs = sort_jobs(jobs)
    jobs = calculate_completion_times(jobs)
    return jobs, sum_weighted_completion_times(jobs)


def test_solve_question():
    assert solve_question("scheduling_tests/test1.txt", question=1)[1] == 31814
    assert solve_question("scheduling_tests/test1.txt", question=2)[1] == 31814

    assert solve_question("scheduling_tests/test2.txt", question=1)[1] == 61545
    assert solve_question("scheduling_tests/test2.txt", question=2)[1] == 60213

    assert solve_question("scheduling_tests/test3.txt", question=1)[1] == 688647
    assert solve_question("scheduling_tests/test3.txt", question=2)[1] == 674634

    print "Question 1: {}".format(solve_question(question=1)[1])
    print "Question 2: {}".format(solve_question(question=2)[1])
