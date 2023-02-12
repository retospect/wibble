__version__ = "0.0.1"


def main(argv=None):
    print("Got Main")
    for dist in __import__("pkg_resources").working_set:
        print(dist.project_name.replace("Python", ""))
