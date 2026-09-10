class SagaOrchestrator:
    """
    Saga Pattern Workflow Orchestrator.
    Executes sequential tasks and triggers backward compensations on failure.
    """
    def __init__(self):
        self.steps = []

    def add_step(self, name, action_fn, compensate_fn):
        self.steps.append((name, action_fn, compensate_fn))

    def execute(self, context):
        executed_steps = []
        for name, action, compensate in self.steps:
            success = action(context)
            if success:
                executed_steps.append((name, compensate))
            else:
                for comp_name, comp_fn in reversed(executed_steps):
                    comp_fn(context)
                return False, f"FAILED_AT_{name}"
        return True, "SAGA_COMPLETED"
