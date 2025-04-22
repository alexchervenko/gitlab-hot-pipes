import requests
from config_parser import init_properties

config_props, form_data  = init_properties()
url = config_props["base_uri"] + config_props["start_endpoint"].format(project_id=config_props["project.id"])
var_to_override = None
second_var_to_override = None

while(not stand_name):
    var_to_override = input("Input data: ")
    second_var_to_override = input("Input data: ")
    print("\n")

print(f"Starting {var_to_override} {second_var_to_override}\n")

try:
    requests.post(url, data=form_data)
except:
    print("Error while sending. Check conection. \n")
    input("Okay... Press Enter to exit \n")