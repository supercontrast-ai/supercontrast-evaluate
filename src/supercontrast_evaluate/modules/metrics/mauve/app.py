import sys

import supercontrast_evaluate
from supercontrast_evaluate.utils import launch_gradio_widget


sys.path = [p for p in sys.path if p != "/home/user/app"]
module = supercontrast_evaluate.load("mauve")
sys.path = ["/home/user/app"] + sys.path

launch_gradio_widget(module)
