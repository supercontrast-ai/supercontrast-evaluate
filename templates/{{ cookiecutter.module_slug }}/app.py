import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


module = supercontrast_evaluate.load(
    "{{ cookiecutter.namespace }}/{{ cookiecutter.module_slug }}"
)
launch_gradio_widget(module)
