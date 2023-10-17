import paramiko as pm
import json
import time

# Site Admin Commands:
# First Command: change off-pbx-telephone station {extension}
# Values to be entered: Extension, OPS, TAB, TAB, EXTENSION, AAR, 1, ENTER (F3)

'''
Function Name: System Administrator Setup
Function Purpose: Sets up a user in Site Admininstrator
Author: Jona Sahota
Last Update By: Jona Sahota
Update Date: October 2nd, 2023
'''

def ssh_conn(host):
    with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
        creds = json.load(f)
    try:
        client = pm.SSHClient()
        client.set_missing_host_key_policy(pm.AutoAddPolicy())
        client.connect(hostname=str(host), username=creds["cts_username_prod"], password=creds["cts_password_prod"], allow_agent=False, look_for_keys=False)
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


def sa(extension):
    with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
        env_variables = json.load(f)
    cts_host = env_variables["cts_prod_ip"]
    
    # NEW: CHANGE OFF-PBX-TELEPHONE STATION: COMMAND #3
    cts_cmds = ["\n", "autosat\n", "SUNT\n", f"change off-pbx-telephone station {extension}\n",
                "\t", "OPS", '\t', '\t', '\t',f"{extension}", '\t', "AAR", '\t', "1", '\x1b[13~']
    result = execute_cts_commands(cts_host, cts_cmds)


    return result


def main():
    sa(extension="3419573")

if __name__ == "__main__":
    main()
