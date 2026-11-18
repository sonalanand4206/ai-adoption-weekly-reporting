"""Generate the weekly report using the code in CS_JP.ipynb."""
import json
from pathlib import Path

project_dir = Path(__file__).resolve().parent
notebook_path = project_dir / "CS_JP.ipynb"


def main():
    # Share variables across code cells, as Jupyter does.
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    for number, cell in enumerate(notebook["cells"], start=1):
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            exec(compile(source, f"{notebook_path.name}, cell {number}", "exec"), namespace)


if __name__ == "__main__":
    main()
