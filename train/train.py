import json
from pathlib import Path


class Train:
    def __init__(
        self,
        config,
        output_dir: Path,
        variables: dict,
        secrets: dict = None,
    ):
        self.config = config
        self.output_dir = output_dir
        self.variables = variables
        self.secrets = secrets

    def train(self):
        print("variables", self.variables)
        print("secrets", self.secrets["super_secret"])
        with open(self.output_dir / "test_out.txt", "w", encoding="utf-8") as f:
            f.writelines(["You should see these output in s3"])
            json.dump(self.variables, f, indent=4)
