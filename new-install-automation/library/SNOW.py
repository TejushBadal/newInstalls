#!/usr/bin/python3
from base64 import b64encode
import json
import requests

'''
Function Name: Close Tickets Subtasks
Function Purpose: Closes the Tickets Subtasks in Service Now using the SNow REST API once the removal has been completed
Author: Jona Sahota
Last Update By: Jona Sahota
Update Date: October 2nd, 2023
'''

# TODO:
# Closure Reason if required. It's required when when the ticket is completed AFTER the due date of employee's removal.

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

def get_sysid(ritm, data):
    # Extract SYS ID
    url = 'https://sunlife.service-now.com/api/now/table/sc_req_item'
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    params = {
        "sysparm_query": f'number={ritm}'
    }
    response = requests.get(url, auth=(data['snow_fid_username'], data['snow_fid_password']), headers=headers, params=params)
    if response.status_code == 200:
        sys_id = response.json()['result'][0]['sys_id']
        return sys_id
    else:
        return None


def get_subtasks(sys_id, data):
    # Titles to be matched
    titles = ["Telephony Account Administration"]

    url = f"https://sunlife.service-now.com/api/now/table/sc_task"
    headers = {
        "Content-Type": "application/json",
        'Authorization': basic_auth(data['snow_fid_username'], data['snow_fid_password'])
    }
    params = {
        "sysparm_query": f"parent={sys_id}"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return [(item['sys_id'], item['short_description'], item.get('assigned_to')) for item in response.json()['result'] if item['short_description'] in titles]
    else:
        return None



def close_subtask(subtask_sys_id, description, assigned_to, data):
    url = f"https://sunlife.service-now.com/api/now/table/sc_task/{subtask_sys_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": basic_auth(data['snow_fid_username'], data['snow_fid_password'])
    }
    payload = {
        "state": "3",
        "u_smart_tool_updated": "Yes"
    }
    # If the task is "ACE and Zoom Administration" and not assigned, assign to "Y048"
    if description == "ACE and Zoom Administration" and not assigned_to:
        payload["assigned_to"] = "a5a2f384db481340594e3ebd7c9619fe"

    response = requests.put(url, json=payload, headers=headers)
    return response.status_code == 200


def get_user_sysid(username, data):
    url = 'https://sunlife.service-now.com/api/now/table/sys_user'
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    params = {
        "sysparm_query": f'user_name={username}'
    }
    response = requests.get(url, auth=(data['snow_fid_username'], data['snow_fid_password']), headers=headers, params=params)
    if response.status_code == 200 and len(response.json()['result']) > 0:
        sys_id = response.json()['result'][0]['sys_id']
        return sys_id
    else:
        return None

def close_parent_ticket(sys_id, data):
    url = f"https://sunlife.service-now.com/api/now/table/sc_req_item/{sys_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": basic_auth(data['snow_fid_username'], data['snow_fid_password'])
    }
    payload = {
        "state": "3" 
    }
    response = requests.put(url, json=payload, headers=headers)
    return response.status_code == 200


def snow(ritm):
    with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        sys_id = get_sysid(ritm, data)
        subtask_sys_ids = get_subtasks(sys_id, data)
        if subtask_sys_ids:
            all_subtasks_closed = True
            for subtask_sys_id, description, assigned_to in subtask_sys_ids: 
                if not close_subtask(subtask_sys_id, description, assigned_to, data): 
                    all_subtasks_closed = False
                    print(f"Failed to close subtask with Sys ID {subtask_sys_id}")

            if all_subtasks_closed:
                if close_parent_ticket(sys_id, data):
                    print(f"Successfully closed the parent ticket with Sys ID {sys_id}")
                else:
                    print(f"Failed to close the parent ticket with Sys ID {sys_id}")             
        return "Success"

    except Exception as e:
        print(f"Script has failed: {e}")
        return "Failure"


    

def main():
    snow(ritm='RITM1486935')
    # with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
    #     data = json.load(f)
    # username = 'Y048'  # Replace with the actual username
    # user_sysid = get_user_sysid(username, data)
    # if user_sysid:
    #     print(f"The sys_id for user {username} is {user_sysid}")
    # else:
    #     print(f"User {username} not found")

if __name__ == '__main__':
    main()
