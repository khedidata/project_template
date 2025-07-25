import toml

def get_dependencies(dependencies_file: str = "pyproject.toml",
                     output_dependencies_file: str = "requirements.txt") -> None:
    # load pyproject.toml file
    pyproject = toml.load(dependencies_file)

    # getting access to dependencies 
    dependencies = pyproject.get("project", {}).get("dependencies", [])

    # write dependencies in a requirements.txt file
    with open(output_dependencies_file, "w") as f:
        for dep in dependencies:
            f.write(dep + "\n")

if __name__ == "__main__":
    get_dependencies()