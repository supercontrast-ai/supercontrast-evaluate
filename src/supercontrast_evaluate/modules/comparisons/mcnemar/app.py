import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


module = supercontrast_evaluate.load("mcnemar", module_type="comparison")
launch_gradio_widget(module)
