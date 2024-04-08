import os
import pathlib

from evalplus.data.humaneval import get_human_eval

if __name__ == "__main__":
    # check existance of ground truth folder
    GT_DIR = pathlib.Path(__file__).parent.parent / "groundtruth" / "humaneval"

    # assert not os.path.exists(
    #     GT_DIR
    # ), "Ground truth folder already exists! If you want to reinitialize, delete the folder first."

    # os.mkdir(GT_DIR)

    def declarationTrim(declaration):
        declaration = declaration.split("def")[1].split("(")[0].strip()
        return declaration

    human_eval = get_human_eval()
    for i, k in enumerate(human_eval):
        task = human_eval[k]
        incomplete = (
            task["prompt"]
            + task["canonical_solution"]
            + "\n\n"
            + task["test"]
        )
        with open(
            os.path.join(GT_DIR, f"{str(i).zfill(3)}_{declarationTrim(task['declaration'])}.py"),
            "w", encoding="utf-8"
        ) as f:
            f.write(incomplete)
