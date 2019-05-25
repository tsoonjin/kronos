"""
Kronos: A simple scheduler for graduate training programme

Entities: User, Schedule, Rotation
"""


def assignments2schedule(assignments):
    """ Convert assignment object to overall schedule
    """
    users = {}
    for weekly_assignments in assignments.values():
        for rotationId, rotationAssignments in weekly_assignments.items():
            for userId, assignment in rotationAssignments.items():
                if userId not in users:
                    users[userId] = {}
                if rotationId not in users[userId]:
                    users[userId][rotationId] = {
                        'startDate': assignment[0],
                        'endDate': assignment[1],
                    }
    print(users)
    return users


def generateUserSchedule(user, assignments, scoring_function):
    """ Generate most optimal user schedule
    Parameters:
        user (object): User
        assignments (dict): Time-bounded assignments
        scoring_function (function): scoring function to rank possible assignments

    Returns:
        schedule (list): list of rotations
    """
    return [{"rotationId": "PMO", "startDate": "012018"}]


def getOverallSchedule(users):
    """ Generate overall schedule from individual user's schedule
    Parameters:
        users (list): list of Users

    Returns:
        schedule (dict): overall assignments
    """
    return {}


def getConflictingAssignments(schedule):
    """ Get list of assignments which exceeded rotation capacity
    Parameters:
        schedule (dict): overall assignments

    Returns:
        confictingAssignmentsByRotation (dict): overall schedule with conflicting assignments
    """
    return {}


if __name__ == "__main__":
    pass
