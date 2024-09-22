import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


module = supercontrast_evaluate.load("indic_glue", "wnli")
launch_gradio_widget(module)
