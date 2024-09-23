import importlib.util
import os
from typing import Optional, Union

from .module import EvaluationModule


def load(
    path: str,
    config_name: Optional[str] = None,
    module_type: Optional[str] = None,
    **kwargs,
) -> EvaluationModule:
    if os.path.isfile(path):
        # If path is a file, load it directly
        module_name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        # If path is not a file, try to import it as a module
        if module_type is None:
            for mt in ["metrics", "comparisons", "measurements"]:
                try:
                    module_path = f"supercontrast_evaluate.modules.{mt}.{path}.{path}"
                    module = importlib.import_module(module_path)
                    module_type = mt
                    break
                except ImportError:
                    continue
            if module_type is None:
                raise ValueError(
                    f"Could not find module '{path}' in any module type directory."
                )
        else:
            module_path = f"supercontrast_evaluate.modules.{module_type}.{path}"
            try:
                module = importlib.import_module(module_path)
            except ImportError:
                raise ImportError(
                    f"Could not import module '{path}' from {module_path}"
                )

    # Get the main class from the module
    main_class = getattr(module, path.capitalize(), None)
    if main_class is None:
        raise AttributeError(f"Could not find main class in module '{path}'")

    # Initialize and return the evaluation module
    return main_class(config_name=config_name, **kwargs)
