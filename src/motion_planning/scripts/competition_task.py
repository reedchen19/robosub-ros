from task import Task
from combination_tasks import ListTask
from move_tasks import MoveToPoseGlobalTask

class CompetitionTask(Task):
    """
    High level competition level task, contains a list of tasks for each competition task.
    """

    def __init__(self, *args, **kwargs):
        super(CompetitionTask, self).__init__(*args, **kwargs)

        self.list_task = ListTask([ MoveToPoseGlobalTask(2, 0, 0, 0, 0, 0, *args, **kwargs) ])

    def _on_task_run(self):
        self.list_task.run()

        if self.list_task.finished:
            self.finish()