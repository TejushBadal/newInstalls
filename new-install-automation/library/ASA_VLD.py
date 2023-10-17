import paramiko as pm
import json
import time

# Site Admin Commands:
# display station {extension}

'''
Function Name: System Administrator Extension Variations Checker
Function Purpose: Checks for Extension Variations to see if they're being used or not.
Author: Jona Sahota
Last Update By: Jona Sahota
Update Date: October 5th, 2023
'''


def ssh_conn(host):
    with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
        creds = json.load(f)
    try:
        client = pm.SSHClient()
        client.set_missing_host_key_policy(pm.AutoAddPolicy())
        client.connect(hostname=str(host), username=creds["cts_username_prod"],
                       password=creds["cts_password_prod"], allow_agent=False, look_for_keys=False)
        return client, None
    except Exception as error:
        return None, f"The error is the following: {error}"


def execute_cts_commands(host, cts_commands):
    output_str = ''
    client, err = ssh_conn(host)
    if err:
        return err
    try:
        time.sleep(1)
        channel = client.invoke_shell('SUNT')
        for cmd in cts_commands:
            channel.send(cmd)
            time.sleep(1)
        output = channel.recv(999990000)
        output_str += output.decode("utf-8")
        print(output_str)
    except Exception as e:
        return f'Error during SSH session: {e}'
    finally:
        client.close()
    return "Success"


def sa(extension, command):
    with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
        env_variables = json.load(f)
    cts_host = env_variables["cts_prod_ip"]

    if command == "change":
        cts_cmds = ["\n", "autosat\n", "SUNT\n", f"change off-pbx-telephone station {extension}\n",
                    "\t", "OPS", '\t', '\t', '\t', f"{extension}", '\t', "AAR", '\t', "1", '\x1b[13~']
    elif command == "display":
        cts_cmds = [f"display station {extension}\n"]
    else:
        return "Invalid command"

    result = execute_cts_commands(cts_host, cts_cmds)
    return result


prefix_rows = [
    ["335", "435", "360", "460"],
    ["343", "443", "360", "460"],
    ["333", "433", "360", "460"],
    ["331", "432", "332", "431", "360", "460"],
    ["341", "441", "342", "442", "360", "460"],
    ["342", "442", "341", "441", "360", "460"],
    ["200", "400"],
    ["307", "407", "308", "408"],
    ["344", "444", "380", "480"],
    ["355", "455", "380", "480"],
    ["350", "450", "380", "480"],
    ["312", "412", "380", "480"],
    ["388", "488", "380", "480"],
    ["306", "406", "380", "480"],
    ["303", "403", "380", "480"],
    ["304", "404", "380", "480"]
]



def main(extension):
    last_4_digits = extension[-4:]

    for prefixes in prefix_rows:
        for prefix in prefixes:
            # Generate the full extension using the prefix and the last 4 digits
            full_extension = prefix + last_4_digits
            print(f"Running 'display station' for extension {full_extension}")
            print(sa(extension=full_extension, command="display"))


# Run the main function
if __name__ == "__main__":
    main()
