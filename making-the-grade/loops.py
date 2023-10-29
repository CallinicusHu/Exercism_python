"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    for index, scores in enumerate(student_scores):
        student_scores[index] = int(round(
            scores))  # elolvastam 10x a feladatot begépeltem külön terminalba mire észrevettem hogy a legközelebbi kerekhez kell kerekíteni nem kerekre, nagyon kerestem mi a forom baja

    # for scores in student_scores:
    #    scores = int(round(scores)) #elolvastam 10x a feladatot begépeltem külön terminalba mire észrevettem hogy a legközelebbi kerekhez kell kerekíteni nem kerekre, nagyon kerestem mi a forom baja
    # valamiért úgy érzem működnie kéne az enumeratees indexelés nélkül is valahogy de még mindig nem vagyok biztos benne hogy értem a fort amikor ezt írom

    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    count = 0   

    for scores in student_scores:
        if scores <= 40:
            count += 1

    # van egy olyan method hogy count és próbáltam rájönni, hátha jó erre, de nem sikerült megfejtenem

    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    count = []

    for scores in student_scores:
        if scores >= threshold:
            count.append(scores)

    return count


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    incr = int((highest - 40) / 4)
    fix = incr
    dcba = [41]

    for next in range(1, 4):
        step = 41 + incr
        incr += fix
        dcba.append(step)

    return dcba


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    new_list = []

    for index, word in enumerate(student_scores):
        k = f"{str(index + 1)}. {student_names[index]}: {str(student_scores[index])}"
        new_list.append(k)

    # szinte biztos vagyok benne, hogy valahogy tudom ugyanazokra az indexekre valahogy csinisebben számosítani és egymás mellé tenni a listák elemeit, de most nem találtam meg

    return new_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    x = []

    for perf in student_info:
        if perf[1] == 100:
            x = perf
            break

    return x

    # https: // stackoverflow.com / questions / 1156087 / search - in -lists - of - lists - by - given - index
    # ebből másoltam de ezt a sublist[1] nem értem mit csinál és hogy működik
    # talán a listában lévő listák 1-es indexén néz meg valamit?
    # szerk azt értem hogy a neve bármi lehet, (pl perf) és a sublist nem valami az [1]ben nem vagyok biztos :-)
