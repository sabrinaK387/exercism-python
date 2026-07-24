"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    rounded_scores = []
    
    while student_scores:
        score = student_scores.pop(0)
        score_rounded = round(score,0)
        rounded_scores.append(score_rounded)
        
    return rounded_scores
        


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    failed_students = 0

    for student_score in student_scores:
        if student_score <= 40:
            failed_students = failed_students + 1

    return failed_students


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    scores_above_threshold = []

    for student_score in student_scores:
        if student_score >= threshold:
            scores_above_threshold.append(student_score)

    return scores_above_threshold

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    letter_grades_value = []
    grade_F = 40
    grade_interval = int((highest - grade_F)/4)
    
    for grade in range(41,highest,grade_interval):
        letter_grades_value.append(grade)
    
    return letter_grades_value

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    rank = 1
    ranking_list = []

    for index, name in enumerate(student_names):
        ranking_list.append(f'{rank}. {name}: {student_scores[index]}')
        rank = rank + 1

    return ranking_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """


    for student_score in student_info:
        if 100 in student_score:
            return student_score
    return []