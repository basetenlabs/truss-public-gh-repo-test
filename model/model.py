from typing import Dict, List


class Model:
    def __init__(self, **kwargs) -> None:
        self._data_dir = kwargs["data_dir"]
        self._config = kwargs["config"]
        self._model = None

    def predict(self, request: Dict) -> Dict[str, List]:
        response = {}
        inputs = request["inputs"]  # noqa
        # Invoke model and calculate predictions here.
        response["predictions"] = inputs
        return response
