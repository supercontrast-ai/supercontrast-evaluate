import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


module = supercontrast_evaluate.load("label_distribution", module_type="measurement")
launch_gradio_widget(module)
