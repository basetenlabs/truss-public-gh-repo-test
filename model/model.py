from typing import Dict, List
import time


class Model:
    def __init__(self, **kwargs) -> None:
        pass

    def load(self):
        pass


    def predict(self, request: Dict) -> Dict[str, List]:
        def inner():
            for i in range(5):
                time.sleep(1)
                print(str(i))
        return inner()
