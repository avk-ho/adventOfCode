# https://adventofcode.com/2022/day/7


class Directory():
    def __init__(self, name, prev_dir):
        self.name = name
        self.size = 0
        self.prev_dir = prev_dir
        self.content = []
    
    def update_size(self):
        size = 0
        for content in self.content:
            size += content.size

        self.size = size

        if self.prev_dir is not None:
            self.prev_dir.update_size()

    def add_content(self, content):
        if content in self.content:
            return
        self.content.append(content)
        self.update_size()

    def access_inner_dir(self, dir_name):
        for content in self.content:
            if content.name == dir_name and type(content) == Directory:
                return content


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


def format_report(report):
    formatted_report = report.split("\n")
    for line in formatted_report:
        if line == "$ ls":
            formatted_report.remove(line)

    return formatted_report


def build_directories_tree(report):
    formatted_report = format_report(report)

    current_dir = None
    root_dir = None
    for line in formatted_report:
        # go to prev dir
        if ("$ cd .." in line) and (current_dir is not None):
            current_dir = current_dir.prev_dir

        # check dir
        elif "$ cd " in line:
            dir_name = line.replace("$ cd ", "")
            
            if current_dir is None:
                current_dir = Directory(name=dir_name, prev_dir=None)
                root_dir = current_dir
            else:
                current_dir = current_dir.access_inner_dir(dir_name)

        # inner dir
        elif "dir " in line:
            dir_name = line.replace("dir ", "")
            new_dir = Directory(name=dir_name, prev_dir=current_dir)
            current_dir.add_content(new_dir)
        
        # file
        else:
            file_info = line.split()
            new_file = File(name=file_info[1], size=int(file_info[0]))
            current_dir.add_content(new_file)
        
    return root_dir

def sum_sizes_of_directories_below_100k(root_dir):
    def sum_sizes_helper(directory):
        if directory.size <= 100000:
            sum_sizes.append(directory.size)

        for content in directory.content:
            if type(content) == Directory:
                sum_sizes_helper(content)

    sum_sizes = []
    sum_sizes_helper(root_dir)

    return sum(sum_sizes)


target = 95437
report = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k\
"""

root_dir = build_directories_tree(report)
# print(sum_sizes_of_directories_below_100k(root_dir))

if sum_sizes_of_directories_below_100k(root_dir) == target:
    print("Success")