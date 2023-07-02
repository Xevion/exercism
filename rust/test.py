#!/usr/bin/env python3

from pathlib import Path
import re
from subprocess import Popen, PIPE
from colored import Fore, Style
from typing import List, Tuple

CURRENT_DIR = Path(__file__).parent


def main() -> None:
    # Find all tests
    test_directories: List[Path] = [x for x in CURRENT_DIR.iterdir(
    ) if x.is_dir() and x.joinpath("Cargo.toml").exists()]

    for directory_path in test_directories:
        passed, total = test_directory(directory_path)

        passed_color = Fore.GREEN
        if passed != total:
            if passed == 0:
                passed_color = Fore.RED
            else:
                passed_color = Fore.YELLOW
        
        total_color = Fore.BLUE

        print(f"{directory_path.name} {passed_color}{passed}{Style.reset}/{total_color}{total}{Style.reset}")


def test_directory(path: Path) -> Tuple[int, int]:
    targets = list(
        filter(
            lambda target: target.suffix == ".rs",
            path.joinpath("tests").iterdir()
        )
    )

    passed, total = 0, 0

    for target in targets:
        results = test_target(path, target)
        passed += results[0]
        total += results[1]

    return passed, total


def test_target(base_directory: Path, target: Path) -> Tuple[int, int]:
    process = Popen(["cargo", "test", "--no-fail-fast", "--test", target.stem, "--", "--include-ignored"], cwd=base_directory, stdout=PIPE, stderr=PIPE)
    process.wait()

    stdout = process.stdout.read().decode("utf-8").strip().split("\n")
    
    total_tests = int(re.match(r"running (\d+) tests?", stdout[0]).group(1))
    results_match = re.search(r"test result: (.+). (\d+) passed;", stdout[-1])
    passed_tests = int(results_match.group(2))
    test_status = results_match.group(1)

    # Unstable
    if total_tests == passed_tests:
        assert test_status == "ok"
    else:
        assert test_status != "ok"

    return passed_tests, total_tests


if __name__ == "__main__":
    main()
