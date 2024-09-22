import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


module = supercontrast_evaluate.load("perplexity", module_type="metric")
launch_gradio_widget(module)
