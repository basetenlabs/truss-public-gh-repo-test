from typing import Dict, List
import time


class Model:
    def __init__(self, **kwargs) -> None:
        self._data_dir = kwargs["data_dir"]
        if (self._data_dir / 'test_blob').exists():
            print('External blob found')
        else:
            print('External blob not found')
        self._config = kwargs["config"]
        self._model = None
    
    def load(self):
        print("LOADING MODEL 3")
        print("foobyfooo")
        time.sleep(20)


    def predict(self, request: Dict) -> Dict[str, List]:
        response = {}

        inputs = request["inputs"]  # noqa
        if inputs == [1]:
            raise Exception("you did a bad")
        # Invoke model and calculate predictions here.
        response["predictions"] = inputs
        return response
