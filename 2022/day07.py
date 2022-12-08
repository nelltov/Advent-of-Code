import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- terminal output"""
    return puzzle_input_str.splitlines()


def part1(data: List[str]):
    """Solve part 1 -- Find all the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?"""
    cur_path = "/"
    # a dictionary of the directories we encounter and their sizes
    dir_sizes = dict()
    dir_sizes["/"] = 0
    seen_files = set()
    for command in data[1:]:
        command_portions = command.split(" ")
        if command_portions[0] == "$":
            # update the current directory based on the cd commands
            if command_portions[1] == "cd":
                next_dir = command_portions[2]
                if next_dir == "..":
                    cur_path = "\\".join((cur_path.split("\\"))[:-1])
                elif next_dir == "/":
                    cur_path = "/"
                else:
                    cur_path += f"\\{next_dir}"
                    # add a newly-seen directory to the dictionary
                    if cur_path not in dir_sizes:
                        dir_sizes[cur_path] = 0
        elif command_portions[0] != "dir":
            # as you find a file, take all the directories in the current path and update their sizes
            size = int(command_portions[0])
            new_file = cur_path + f"\\{command_portions[1]}"
            if new_file not in seen_files:
                dir_sizes[cur_path] += size
                dirs = cur_path.split("\\")
                for i in range(1, len(dirs)):
                    dir_sizes[("\\".join((cur_path.split("\\"))[:-i]))] += size
                seen_files.add(new_file)

    # loop through the dictionary and count everything with size <= 100000
    dir_list = []
    for cur_dir in dir_sizes:
        dsize = dir_sizes[cur_dir]
        if dsize <= 100000:
            dir_list.append(dsize)
    return sum(dir_list), dir_sizes


def part2(dir_sizes) -> int:
    """Solve part 2 -- Find the smallest directory that, if deleted, would free up enough space
    on the filesystem to run the update. What is the total size of that directory?"""
    free_space_available = 70000000 - dir_sizes["/"]
    free_space_needed = 30000000 - free_space_available
    if free_space_needed <= 0:
        return 0
    sufficient_dirs = dict(filter(lambda elem: elem[1] >= free_space_needed, dir_sizes.items()))
    return min(sufficient_dirs.values())


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        x, d = part1(puzzle_data)
        print(f"solution 1: {x}")
        print(f"solution 2: {part2(d)}")
