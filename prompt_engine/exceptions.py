class PromptEngineError(Exception):
    pass

class MissingVariableError(PromptEngineError):
    def __init__(self, variable: str, template_name: str):
        super().__init__(
            f'Missing required variable "{variable}" for template "{template_name}"'
        )
