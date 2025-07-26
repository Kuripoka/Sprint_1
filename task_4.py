new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
completed_tasks.append(new_tasks.pop(4))
new_tasks.remove('task_007')
print(new_tasks[-1])
#В последней задаче из списка new_tasks заказчик поднял приоритет, поэтому её нужно будет взять в работу следующей. Выведи её на экран.
