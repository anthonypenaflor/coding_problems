def task_assignment(k, tasks):
    # Write your code here.
    paired_tasks = []
    task_duration_to_idx = get_task_durations(tasks)

    sorted_tasks = sorted(tasks)
    for idx in range(k):
        task_one_duration = sorted_tasks[idx]
        indices_with_task_one_duration = task_duration_to_idx[task_one_duration]
        task_one_index = indices_with_task_one_duration.pop()

        task_two_sorted_index = len(tasks) - 1 - idx
        task_two_duration = sorted_tasks[task_two_sorted_index]
        indices_with_task_two_duration = task_duration_to_idx[task_two_duration]
        task_two_index = indices_with_task_two_duration.pop()

        paired_tasks.append([task_one_index, task_two_index])

    return paired_tasks


def get_task_durations(tasks):
    task_durations_to_idx = {}

    for idx, task_duration in enumerate(tasks):
        if task_duration in task_durations_to_idx:
            task_durations_to_idx[task_duration].append(idx)
        else:
            task_durations_to_idx[task_duration] = [idx]

    return task_durations_to_idx


if __name__ == '__main__':

    """You're given an integer num representing a number of workers and an array of positive integers representing
    duration of tasks that must be completed by the workers. Each worker must complete two unique tasks adn can only
    work on one task at a time. The number of tasks will always be equal to 2k such that each worker always has two
    tasks to complete. All tasks are independent of one another and can be completed in any order. Workers
    will complete their assigned tasks in parallel, and the time taken to complete all tasks will be equal to the time 
    taken to complete the longest pair of tasks (see the sample output for an explanation). Write a function that 
    returns the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible. Your 
    function should return a list of pairs, where each pair stores the indices of the tasks that should be completed by
    one worker. The pairs should be in the following format: [task, task2] , where the order of task1 and task2 doesn't
    matter. Your function can return the pairs in any order. If multiple optimal assignments exist, any correct answer
    will be accepted.
    Note: you'll always be given at least one worker (l..., k will always be greater than 0)."""

    num = 3
    task = [1, 3, 5, 3, 1, 4]

    task_assignment(num, task)
