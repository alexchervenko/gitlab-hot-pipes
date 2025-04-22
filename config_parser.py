def init_properties() -> dict:
    result_dict = {}
    envs = {}
    with open("config.properties", "r") as f:
        for line in f:
            l = line.strip()
            temp_entry_list = []
            if not l.startswith("#"):
                temp_entry_list = l.split(sep="=", maxsplit=1)
                if len(temp_entry_list) == 2:
                    if temp_entry_list[0].isupper():
                        envs[f"variables[{temp_entry_list[0]}]"] = temp_entry_list[1]
                    else: 
                        result_dict[temp_entry_list[0]] = temp_entry_list[1]
    return result_dict, envs