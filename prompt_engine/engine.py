import os
import yaml
from jinja2 import Template
from .models import PromptTemplate
from .exceptions import MissingVariableError

class PromptEngine:
    def __init__(self, templates_dir: str):
        self.templates = {}
        self.load_templates(templates_dir)

    def load_templates(self, templates_dir: str):
        for file in os.listdir(templates_dir):
            if file.endswith(".yaml") or file.endswith(".yml"):
                path = os.path.join(templates_dir, file)
                with open(path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    template = PromptTemplate(**data)
                    self.templates[template.name] = template

    def render(self, template_name: str, variables: dict) -> str:
        template = self.templates[template_name]

        for var in template.input_variables:
            if var not in variables:
                raise MissingVariableError(var, template_name)

        prompt_text = template.template

        # Few-shot examples
        if template.examples:
            examples_text = ""
            for ex in template.examples:
                examples_text += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
            prompt_text = examples_text + prompt_text

        jinja_template = Template(prompt_text)
        return jinja_template.render(**variables)

    def chain(self, steps):
        context = {}
        output = None

        for template_name, vars in steps:
            vars = {**vars, **context}
            output = self.render(template_name, vars)
            context["previous_output"] = output

        return output
