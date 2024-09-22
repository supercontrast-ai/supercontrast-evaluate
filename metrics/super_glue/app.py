import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


module = supercontrast_evaluate.load("super_glue", "copa")
launch_gradio_widget(module)
