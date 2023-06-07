import yaml


def yml_data_with_file(file_name):
    with open("./data/" + file_name + ".yml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    print(yml_data_with_file("login_data"))
