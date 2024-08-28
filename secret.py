import os


def read_env(file=True):
    """Load environment variables from a .env file or from the system."""
    if file:
        env_vars = {}
        path = os.path.join(os.getcwd(), ".env")
        with open(path, "r") as file:
            for line in file:
                if line.strip() and not line.startswith("#"):
                    k, v = line.strip().split("=")
                    env_vars[k] = v
        return env_vars
    return os.environ


def get_secret_by_name(name: str, default:str=None, env_file = True) -> str:
    vars = read_env(env_file)
    result = vars.get(name, default)
    if result is None:
        raise ValueError(f"Error initializing env variable: {name}")
    return str(result)


if __name__=="__main__":
    TEST = get_secret_by_name("TEST_VAR")
    print(TEST)
