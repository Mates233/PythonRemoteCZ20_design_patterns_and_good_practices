"""
Composite je návrhový vzor, který lze použít, pokud jsme schopni reprezentovat objekty jako stromy.
Takový strom se skládá z uzlů, které jsou z pohledu uživatele samostatnými objekty.

Abychom mohli použít kompozit, potřebujeme následující prvky:

běžné rozhraní nebo základní třída pro objekty ve stromu se často nazývá component (komponenta).
třída představující jeden objekt na větvi (což je component). Takový objekt,
který neobsahuje žádné potomky, často nazývané list (leaf)
složená třída, která je také component, obsahující množinu listů (leafs).
"""


from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass


class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=0):
        print(' ' * indent + f"File: {self.name}, Size: {self.size} bytes")


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(' ' * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)


def main():
    # Create files
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    # Create directories and add files to them
    dir1 = Directory("dir1")
    dir1.add(file1)

    dir2 = Directory("dir2")
    dir2.add(file2)
    dir2.add(file3)

    # Create a root directory and add directories and files to it
    root_dir = Directory("root")
    root_dir.add(dir1)
    root_dir.add(dir2)
    root_dir.add(File("file4.txt", 400))

    # Display the file system structure
    root_dir.display()

if __name__ == "__main__":
    main()
