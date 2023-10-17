from ansible.module_utils.basic import AnsibleModule
import requests
import time
import json

with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
    data = json.load(f)

vm_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': '',
    'referer': 'https://voicemail.ca.sunlife/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

def vm_login():
    data = {
    'password': data['VM_USERNAME'],
    'username': data['VM_PASSWORD']
    }

    #Login to voicemail
    response = requests.post(data['VM_LOGIN'], json = data, verify = False)
    jwt = str(response.json()['jwt'])
    auth = f'jwt {jwt}'

    return(auth)


def vm(first_name, last_name, email, extension, acf2):
    auth = vm_login()
    vm_headers.update({'authorization': auth})

    #general options
    data = {
        "ID":0,
        "MailboxNo": extension,"FGroupID":5,"CompanyID":0,
        "UserName": extension,"MailboxType":0,"NumericPassword":"194750","NumericPasswordCrypt":0,
        "MailPassword":f"{extension}a","MailPasswordCrypt":0,"PasswordExpiryDate":"",
        "LastName": last_name,
        "FirstName": first_name,"DepartmentID":3,"Department":"null","OperatorMbxID":0,"VoiceMenuActive":True,"VoiceMenuID":109,"CustMailbox":False,"CustMailboxMenuID":0,"ActiveGreeting":0,"Tutorial":True,"DIDTrunk":"","SayDateTime":False,"LIFO":False,"CascadeNotification":False,"CascadeNotificationLoopBack":False,"VoiceMailNotify":0,"EMailNotify":0,"MessageLampStatus":False,"FaxMailNotify":False,"FaxMailOptions":"","MessageFwdDelete":False,"LAP":0,"LapType":0,"LapBaudRate":0,"LapCapCode":"","CallFwd":False,"CallFwdMailboxID":0,"CallFwdOneLevel":False,"DesktopStatus":0,"LanTalk":False,"ShowSendList":False,"CallerIDType":0,"CallScreening":False,"PrePaging":False,"PostPaging":False,"CallQueuing":False,"MassRecall":False,"DoOCR":False,"Info":{"TotalNumOfMsgs":0,"NumOfReadMsgs":0,"NumOfUnreadMsgs":0,"NumOfUrgentMsgs":0,"NumOfVoiceMsgs":0,"NumOfReadVoiceMsgs":0,"NumOfUnreadVoiceMsgs":0,"NumOfEmailMsgs":0,"NumOfReadEmailMsgs":0,"NumOfUnreadEMailMsgs":0,"NumOfFaxMsgs":0,"NumOfReadFaxMsgs":0,"NumOfUnreadFaxMsgs":0,"NumOfMeetReqMsgs":0,"NumOfReadMeetReqMsgs":0,"NumOfUnreadMeetReqMsgs":0,"NumOfUnreadMsgsInbox":0,"NumOfReadMsgsInbox":0},"AccountCode":"","imapName":"","imapPswd":"","MbxIMAPServerID":0,"TSEAccount":"","imapLogErr":0,"imapConErr":0,"StorageMode":0,"IMAPFilter":False,"IMAPFilterTime":"","SendBusinessCard":False,"ReceiveBusinessCard":False,"ChangeGreetingOnMeeting":False,"MbxCreateDate":"null","MbxModifyDate":"null","MbxExtObjectID":"","MbxSyncLanguage":0,"MbxDateFormat":"YYYYMMDD","MbxNTAccount":"","MbxCapability":0,"MbxRecordInboundCalls":False,"MbxRecordOutboundCalls":False,"MbxSpecialVMGreetingID":0,"MbxSpecialVMGreetingLngID":0,"MbxWebClient":True,"MbxASRContacts":0,"MbxLocFollowCurrent":0,"MbxLocCurLocID":0,"MbxLocCurAvailability":0,"MbxLocCurAddress":"","MbxLocCurAddressType":0,"MbxLocCurDisableBehFilters":False,"MbxLocCurUnavOnNoCallerID":False,"MbxLocCurStayOpt":0,"MbxLocCurStayUntil":"","MbxCampOn":False,"MbxLocked":False,"MbxLockedTime":"","MbxPBXNodeID":0,"MbxShowToolTips":False,"MbxShowGettingStarted":False,"MbxGender":0,"MbxDNDToLocation":0,"MbxDNDLocID":0,"MbxDNDLocAvailability":0,"MbxFwdToLocation":0,"MbxFwdLocID":0,"MbxFwdLocAvailability":0,"MbxCollaboration":"","MbxUseMbxIMAP":False,"MbxSpeechMenus":False,"MbxForcedEnrollment":False,"Enrolled":False,"MbxVoiceVerification":0,"TranscribeOutboundMsg":False,"TranscribeOutboundUrgentMsg":False,"TranscribeInboundMsg":False,"TranscribeInboundDeliveryMode":0,"TranscribeInboundUnReadAfterTrans":False,"LastSyncInbox":"null","LastContactsSync":"null","LastCalendarSync":"null","ImapSyncVFormat":0,"FaxDetection":True,"WebTutorial":True,"ExternalUID":"","SpatialData":False,"SecondCallAsBusy":False,"PictureUrl":"https://www.onesna.com/norevimages/noimage.jpg","MsgSyncSourceID":"null","MsgSyncSourceAccount":"","MsgSyncSourcePassword":"","OperPhoneNo":"undefined","MbxPassNumChangedDate":"","MbxPassMailChangedDate":"","MbxPassImapChangeDate":"","LoginDelayUntil":"null","MultiLangOption":"0","LangID":0,"OperatorMbxNo":f"{extension} {first_name} {last_name}","IsGroupMbx":False,"SMGRList":"","Addresses":[],"userGroupMailboxNo":"","OperatorMbxInvalid":"","SecondaryLng":0,
        "MailPasswordConfirm":f"{extension}a","NumericPasswordConfirm":"194750","COMPANYID":"1"
    }

    response = requests.post(data['VM_GENERAL'], headers = vm_headers, json = data, verify = False)
    id = response.json()['ID']
    address_id = response.json()['Addresses'][2]['ID']

    #advanced
    data = {
        "ID": id,
        "MailboxNo": extension,"FGroupID":5,"CompanyID":0,
        "UserName": extension,"MailboxType":0,"NumericPassword":"194750","NumericPasswordCrypt":0,
        "MailPassword":f"{extension}a","MailPasswordCrypt":0,"PasswordExpiryDate":"",
        "LastName": last_name,
        "FirstName": first_name,"DepartmentID":3,"Department":"null","OperatorMbxID": id,"VoiceMenuActive":True,"VoiceMenuID":109,"CustMailbox":False,"CustMailboxMenuID":0,"ActiveGreeting":0,"Tutorial":True,"DIDTrunk":"","SayDateTime":False,"LIFO":False,"CascadeNotification":False,"CascadeNotificationLoopBack":False,"VoiceMailNotify":0,"EMailNotify":0,"MessageLampStatus":False,"FaxMailNotify":False,"FaxMailOptions":"","MessageFwdDelete":False,"LAP":0,"LapType":0,"LapBaudRate":0,"LapCapCode":"","CallFwd":False,"CallFwdMailboxID":0,"CallFwdOneLevel":False,"DesktopStatus":0,"LanTalk":False,"ShowSendList":False,"CallerIDType":0,"CallScreening":False,"PrePaging":False,"PostPaging":False,"CallQueuing":False,"MassRecall":False,"DoOCR":False,"Info":{"TotalNumOfMsgs":0,"NumOfReadMsgs":0,"NumOfUnreadMsgs":0,"NumOfUrgentMsgs":0,"NumOfVoiceMsgs":0,"NumOfReadVoiceMsgs":0,"NumOfUnreadVoiceMsgs":0,"NumOfEmailMsgs":0,"NumOfReadEmailMsgs":0,"NumOfUnreadEMailMsgs":0,"NumOfFaxMsgs":0,"NumOfReadFaxMsgs":0,"NumOfUnreadFaxMsgs":0,"NumOfMeetReqMsgs":0,"NumOfReadMeetReqMsgs":0,"NumOfUnreadMeetReqMsgs":0,"NumOfUnreadMsgsInbox":0,"NumOfReadMsgsInbox":0},"AccountCode":"","imapName":"","imapPswd":"","MbxIMAPServerID":0,"TSEAccount":"","imapLogErr":0,"imapConErr":0,"StorageMode":0,"IMAPFilter":False,"IMAPFilterTime":"","SendBusinessCard":False,"ReceiveBusinessCard":False,"ChangeGreetingOnMeeting":False,"MbxCreateDate":"null","MbxModifyDate":"null","MbxExtObjectID":"","MbxSyncLanguage":0,"MbxDateFormat":"YYYYMMDD","MbxNTAccount":f"ML\\{acf2}","MbxCapability":2,"MbxRecordInboundCalls":False,"MbxRecordOutboundCalls":False,"MbxSpecialVMGreetingID":0,"MbxSpecialVMGreetingLngID":0,"MbxWebClient":True,"MbxASRContacts":0,"MbxLocFollowCurrent":0,"MbxLocCurLocID":0,"MbxLocCurAvailability":0,"MbxLocCurAddress":"","MbxLocCurAddressType":0,"MbxLocCurDisableBehFilters":False,"MbxLocCurUnavOnNoCallerID":False,"MbxLocCurStayOpt":0,"MbxLocCurStayUntil":"","MbxCampOn":False,"MbxLocked":False,"MbxLockedTime":"","MbxPBXNodeID":0,"MbxShowToolTips":False,"MbxShowGettingStarted":False,"MbxGender":0,"MbxDNDToLocation":0,"MbxDNDLocID":0,"MbxDNDLocAvailability":0,"MbxFwdToLocation":0,"MbxFwdLocID":0,"MbxFwdLocAvailability":0,"MbxCollaboration":"","MbxUseMbxIMAP":False,"MbxSpeechMenus":False,"MbxForcedEnrollment":False,"Enrolled":False,"MbxVoiceVerification":0,"TranscribeOutboundMsg":False,"TranscribeOutboundUrgentMsg":False,"TranscribeInboundMsg":False,"TranscribeInboundDeliveryMode":0,"TranscribeInboundUnReadAfterTrans":False,"LastSyncInbox":"null","LastContactsSync":"null","LastCalendarSync":"null","ImapSyncVFormat":0,"FaxDetection":True,"WebTutorial":True,"ExternalUID":"","SpatialData":False,"SecondCallAsBusy":False,"PictureUrl":"https://www.onesna.com/norevimages/noimage.jpg","MsgSyncSourceID":"null","MsgSyncSourceAccount":"","MsgSyncSourcePassword":"","OperPhoneNo":"undefined","MbxPassNumChangedDate":"","MbxPassMailChangedDate":"","MbxPassImapChangeDate":"","LoginDelayUntil":"null","MultiLangOption":"0","LangID":0,"OperatorMbxNo":f"{extension} {first_name} {last_name}","IsGroupMbx":False,"SMGRList":"","Addresses":[],"userGroupMailboxNo":"","OperatorMbxInvalid":"","SecondaryLng":0,
        "MailPasswordConfirm":f"{extension}a","NumericPasswordConfirm":"194750","COMPANYID":"1"
    }

    response = requests.post(data['VM_ADVANCED'] + id + '?syslng=0', headers = vm_headers, json = data, verify = False)

    #mailbox options
    data = {
        "ID": id,
        "MailboxNo": extension,"FGroupID":5,"CompanyID":0,
        "UserName": extension,"MailboxType":0,"NumericPassword":"194750","NumericPasswordCrypt":0,
        "MailPassword":f"{extension}a","MailPasswordCrypt":0,"PasswordExpiryDate":"",
        "LastName": last_name,
        "FirstName": first_name,"DepartmentID":3,"Department":"null","OperatorMbxID": id,"VoiceMenuActive":True,"VoiceMenuID":109,"CustMailbox":False,"CustMailboxMenuID":0,"ActiveGreeting":0,"Tutorial":True,"DIDTrunk":"","SayDateTime":False,"LIFO":True,"CascadeNotification":False,"CascadeNotificationLoopBack":False,"VoiceMailNotify":0,"EMailNotify":0,"MessageLampStatus":False,"FaxMailNotify":False,"FaxMailOptions":"","MessageFwdDelete":False,"LAP":0,"LapType":0,"LapBaudRate":0,"LapCapCode":"","CallFwd":False,"CallFwdMailboxID":0,"CallFwdOneLevel":False,"DesktopStatus":0,"LanTalk":False,"ShowSendList":False,"CallerIDType":0,"CallScreening":False,"PrePaging":False,"PostPaging":False,"CallQueuing":False,"MassRecall":False,"DoOCR":False,"Info":{"TotalNumOfMsgs":0,"NumOfReadMsgs":0,"NumOfUnreadMsgs":0,"NumOfUrgentMsgs":0,"NumOfVoiceMsgs":0,"NumOfReadVoiceMsgs":0,"NumOfUnreadVoiceMsgs":0,"NumOfEmailMsgs":0,"NumOfReadEmailMsgs":0,"NumOfUnreadEMailMsgs":0,"NumOfFaxMsgs":0,"NumOfReadFaxMsgs":0,"NumOfUnreadFaxMsgs":0,"NumOfMeetReqMsgs":0,"NumOfReadMeetReqMsgs":0,"NumOfUnreadMeetReqMsgs":0,"NumOfUnreadMsgsInbox":0,"NumOfReadMsgsInbox":0},"AccountCode":"","imapName":"","imapPswd":"","MbxIMAPServerID":0,"TSEAccount":"","imapLogErr":0,"imapConErr":0,"StorageMode":0,"IMAPFilter":False,"IMAPFilterTime":"","SendBusinessCard":False,"ReceiveBusinessCard":False,"ChangeGreetingOnMeeting":False,"MbxCreateDate":"null","MbxModifyDate":"null","MbxExtObjectID":"","MbxSyncLanguage":0,"MbxDateFormat":"YYYYMMDD","MbxNTAccount":f"ML\\{acf2}","MbxCapability":2,"MbxRecordInboundCalls":False,"MbxRecordOutboundCalls":False,"MbxSpecialVMGreetingID":0,"MbxSpecialVMGreetingLngID":0,"MbxWebClient":True,"MbxASRContacts":0,"MbxLocFollowCurrent":0,"MbxLocCurLocID":0,"MbxLocCurAvailability":0,"MbxLocCurAddress":"","MbxLocCurAddressType":0,"MbxLocCurDisableBehFilters":False,"MbxLocCurUnavOnNoCallerID":False,"MbxLocCurStayOpt":0,"MbxLocCurStayUntil":"","MbxCampOn":False,"MbxLocked":False,"MbxLockedTime":"","MbxPBXNodeID":0,"MbxShowToolTips":False,"MbxShowGettingStarted":False,"MbxGender":0,"MbxDNDToLocation":0,"MbxDNDLocID":0,"MbxDNDLocAvailability":0,"MbxFwdToLocation":0,"MbxFwdLocID":0,"MbxFwdLocAvailability":0,"MbxCollaboration":"","MbxUseMbxIMAP":False,"MbxSpeechMenus":False,"MbxForcedEnrollment":False,"Enrolled":False,"MbxVoiceVerification":0,"TranscribeOutboundMsg":False,"TranscribeOutboundUrgentMsg":False,"TranscribeInboundMsg":False,"TranscribeInboundDeliveryMode":0,"TranscribeInboundUnReadAfterTrans":False,"LastSyncInbox":"null","LastContactsSync":"null","LastCalendarSync":"null","ImapSyncVFormat":0,"FaxDetection":False,"WebTutorial":True,"ExternalUID":"","SpatialData":False,"SecondCallAsBusy":False,"PictureUrl":"https://www.onesna.com/norevimages/noimage.jpg","MsgSyncSourceID":"null","MsgSyncSourceAccount":"","MsgSyncSourcePassword":"","OperPhoneNo":"undefined","MbxPassNumChangedDate":"","MbxPassMailChangedDate":"","MbxPassImapChangeDate":"","LoginDelayUntil":"null","MultiLangOption":"0","LangID":0,"OperatorMbxNo":f"{extension} {first_name} {last_name}","IsGroupMbx":False,"SMGRList":"","Addresses":[],"userGroupMailboxNo":"","OperatorMbxInvalid":"","SecondaryLng":0,
        "MailPasswordConfirm":f"{extension}a","NumericPasswordConfirm":"194750","COMPANYID":"1"
    }

    response = requests.post(data['VM_ADVANCED'] + id + '?syslng=0', headers = vm_headers, json = data, verify = False)

    #addresses
    data = {
        '$type': "DBDriver.EEAM.Address, DBDriver",
        'Addr': email,
        'Addr2': email,
        'AddrAlternateID': False,
        'AddrCountryID': '0',
        'AddrPbxNodeId': '0',
        'AddressLabel': "",
        'AddressType': '14',
        'CTIMonitored': False,
        'ExternalUID': "",
        'ID': address_id,
        'MWI': False,
        'MailboxID': id,
        'Phantom': False,
        'VVIdentification': False,
        'VVTrusted': False,
        'isDefault': True
    }

    response = requests.post(data['VM_ADVANCED'] + id + '/addresses/' + address_id, headers = vm_headers, json = data, verify = False)

    data = {
        'Addr': email,
        'Addr2': email,
        'AddressType': '4',
        'ID': '0',
        'MailboxID': id,
        'isDefault': True
    }
    response = requests.post(data['VM_ADVANCED'] + id + '/addresses/', headers = vm_headers, json = data, verify = False)

    return('success')




def main():
    new_install_voicemail('automation', 'test', 'automation.test@sunlife.com', '3319716', 'zz99')

    module = AnsibleModule(
        argument_spec=dict(
            first_name=dict(type='str', required=True),
            last_name=dict(type='str', required=True),
            email=dict(type='str', required=True),
            extension=dict(type='str', required=True),
            acf2=dict(type='str', required=True)

        ),
        supports_check_mode=True
    )
    first_name = module.params['first_name']
    last_name = module.params['last_name']
    email = module.params['email']
    extension = module.params['extension']
    acf2 = module.params['acf2']


if __name__ == '__main__':
    main()