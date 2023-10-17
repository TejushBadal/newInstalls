import requests
import json


# TODO:
# Get in call With Greg, and go over Profile & others...


#headers for sm 
sm_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
    data1 = json.load(f)

def sm_login():
    session = requests.Session()

    payload = {
        "j_username": data1["SM_USERNAME"],
        "j_password": data1["SM_PASSWORD"],
        "clientTZ": 240,
        "clientTZName": "America/New_York"
    }

    response = session.post(data1["SM_LOGIN"], data = payload, verify = False)

    if response.ok and response.text == '':
        cookie = response.cookies.get_dict()

    else:
        return None
    
    try:
        sessionid = cookie['JSESSIONID']
        token = cookie['ctspawksmg01.ca.sunlife']
        LastAuthTime = cookie['LastAuthTime']
        FailedAuthTime = cookie['FailedAuthTime']
    except:
        return None

    return(f'ctspawksmg01.ca.sunlife={token}; JSESSIONID={sessionid}; clientTZ=240; failedHostAddr=10.95.224.162; clientTZName=America/New_York; FailedAuthTime={FailedAuthTime}; LastAuthTime={LastAuthTime}; failedAuthAttempt=0; HostAddr=10.95.65.41; JSESSIONID={sessionid}')

def sm(extension, email, first_name, last_name, location, acf2id ,tn):
        
    #Login to SM and get cookie to use in header
    cookie = sm_login()
    # print(cookie)

    if cookie == None:
        return('failed to login to sm')
    else:
        sm_headers.update({'cookie': cookie})

        # General, Comm Pass and Address
        data = {
            "userXml": f"<tns:users xmlns:ns4=\"http://xml.avaya.com/schema/import1\" xmlns:ns3=\"http://xml.avaya.com/schema/import_csm_agent\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:ns6=\"http://xml.avaya.com/schema/import_scopia\" xmlns:ns5=\"http://xml.avaya.com/schema/presence\" xmlns:ns8=\"http://xml.avaya.com/schema/import_csm_cm\" xmlns:ns7=\"http://xml.avaya.com/schema/import_sessionmanager\" xmlns:ns13=\"http://xml.avaya.com/schema/deltaImport\" xmlns:ns9=\"http://xml.avaya.com/schema/import_csm_b5800\" xmlns:ns12=\"http://xml.avaya.com/schema/import_ce\" xmlns:ns11=\"http://xml.avaya.com/schema/import_csm_mm\" xmlns:ns10=\"http://xml.avaya.com/schema/import_mem_officelinx\" xmlns:tns=\"http://xml.avaya.com/schema/import\" xsi:schemaLocation=\"http://xml.avaya.com/schema/import userimport.xsd\"><tns:user><authenticationType>basic</authenticationType><displayName>{first_name} {last_name}</displayName><displayNameAscii>{first_name} {last_name}</displayNameAscii><isDuplicatedLoginAllowed>false</isDuplicatedLoginAllowed><isEnabled>true</isEnabled><isVirtualUser>false</isVirtualUser><givenName>{first_name}</givenName><givenNameAscii>{first_name}</givenNameAscii><loginName>{email}</loginName><preferredLanguage>en_CA</preferredLanguage><source>local</source><sourceUserKey>none</sourceUserKey><status>provisioned</status><surname>{last_name}</surname><surnameAscii>{last_name}</surnameAscii><timeZone>(-4:0)Eastern Time (US &amp; Canada)</timeZone><userName>{first_name}.{last_name}</userName><userPassword></userPassword><commPassword>444444</commPassword><roles><role>End-User</role></roles><groups></groups><ownedContactLists><contactList><name>list-{first_name}.{last_name}_sunlife.com</name><isPublic>false</isPublic><contactListType>general</contactListType></contactList></ownedContactLists><commProfileSet><commProfileSetName>Primary</commProfileSetName><isPrimary>true</isPrimary><handleList><handle><handleName>{extension}</handleName><handleType>sip</handleType><handleSubType>username</handleSubType><domainName>sunlife.com</domainName></handle><handle><handleName>+1001{extension}</handleName><handleType>sip</handleType><handleSubType>username</handleSubType><domainName>sunlife.com</domainName></handle><handle><handleName>+{extension}</handleName><handleType>sip</handleType><handleSubType>e164</handleSubType><domainName>sunlife.com</domainName></handle></handleList></commProfileSet><isCommPasswordSet>false</isCommPasswordSet></tns:user></tns:users>",
            "loginName": email,
            "groupData":[]
        }

        response = requests.put(data1['SM_UPDATE'], json = data, headers = sm_headers, verify = False)
        # print(response.text)


        #Profiles
        data = {
            "userXml":f"<tns:users xmlns:ns4=\"http://xml.avaya.com/schema/import1\" xmlns:ns3=\"http://xml.avaya.com/schema/import_csm_agent\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:ns6=\"http://xml.avaya.com/schema/import_scopia\" xmlns:ns5=\"http://xml.avaya.com/schema/presence\" xmlns:ns8=\"http://xml.avaya.com/schema/import_csm_cm\" xmlns:ns7=\"http://xml.avaya.com/schema/import_sessionmanager\" xmlns:ns13=\"http://xml.avaya.com/schema/deltaImport\" xmlns:ns9=\"http://xml.avaya.com/schema/import_csm_b5800\" xmlns:ns12=\"http://xml.avaya.com/schema/import_ce\" xmlns:ns11=\"http://xml.avaya.com/schema/import_csm_mm\" xmlns:ns10=\"http://xml.avaya.com/schema/import_mem_officelinx\" xmlns:tns=\"http://xml.avaya.com/schema/import\" xsi:schemaLocation=\"http://xml.avaya.com/schema/import userimport.xsd\"><tns:user><authenticationType>basic</authenticationType><displayName>{first_name} {last_name}</displayName><displayNameAscii>{first_name} {last_name}</displayNameAscii><isDuplicatedLoginAllowed>false</isDuplicatedLoginAllowed><isEnabled>true</isEnabled><isVirtualUser>false</isVirtualUser><givenName>{first_name}</givenName><givenNameAscii>{first_name}</givenNameAscii><loginName>{email}</loginName><employeeNo>{acf2id}</employeeNo><preferredLanguage>en_US</preferredLanguage><source>local</source><sourceUserKey>none</sourceUserKey><status>provisioned</status><surname>{last_name}</surname><surnameAscii>{last_name}</surnameAscii><timeZone>(-4:0)Eastern Time (US &amp; Canada)</timeZone><userName>{email}</userName><userPassword></userPassword><commPassword></commPassword><roles><role>End-User</role></roles><groups></groups><ownedContactLists><contactList><name>list-{first_name}.{last_name}_sunlife.com</name><isPublic>false</isPublic><contactListType>general</contactListType></contactList></ownedContactLists><commProfileSet><commProfileSetName>Primary</commProfileSetName><isPrimary>true</isPrimary><handleList><handle><handleName>{extension}</handleName><handleType>sip</handleType><handleSubType>username</handleSubType><domainName>sunlife.com</domainName></handle><handle><handleName>+1001{extension}</handleName><handleType>sip</handleType><handleSubType>username</handleSubType><domainName>sunlife.com</domainName></handle><handle><handleName>+{extension}</handleName><handleType>sip</handleType><handleSubType>e164</handleSubType><domainName>sunlife.com</domainName></handle></handleList><commProfileList><commProfile xmlns:ns7=\"http://xml.avaya.com/schema/import_sessionmanager\" xsi:type=\"ns7:SessionManagerCommProfXML\"><commProfileType>SessionManager</commProfileType><ns7:primarySM>Waterloo SM</ns7:primarySM><ns7:secondarySM>Toronto SM</ns7:secondarySM><ns7:terminationAppSequence>CTS-EVO</ns7:terminationAppSequence><ns7:originationAppSequence>CTS-EVO</ns7:originationAppSequence><ns7:homeLocation>{location}</ns7:homeLocation><ns7:maxSimultaneousDevices>2</ns7:maxSimultaneousDevices><ns7:blockNewRegistrationWhenMaxActive>false</ns7:blockNewRegistrationWhenMaxActive><ns7:enabledisablecalllog>false</ns7:enabledisablecalllog><ns7:policyType>fixed</ns7:policyType></commProfile><commProfile xmlns:ns8=\"http://xml.avaya.com/schema/import_csm_cm\" xsi:type=\"ns8:xmlStationProfile\"><commProfileType>CM</commProfileType><ns8:cmName>CTS-ACM</ns8:cmName><ns8:prefHandleId>{extension}@sunlife.com</ns8:prefHandleId><ns8:useExistingExtension>false</ns8:useExistingExtension><ns8:extension>{extension}</ns8:extension><ns8:setType>9630</ns8:setType><ns8:securityCode></ns8:securityCode><ns8:port>S203967</ns8:port><ns8:deleteOnUnassign>true</ns8:deleteOnUnassign><ns8:overRideEndpointName>true</ns8:overRideEndpointName><ns8:dualRegistration>false</ns8:dualRegistration><ns8:enhCallrInfodisplay>false</ns8:enhCallrInfodisplay><ns8:lockMessages>false</ns8:lockMessages><ns8:coveragePath1>4</ns8:coveragePath1><ns8:tn>{tn}</ns8:tn><ns8:cor>7</ns8:cor><ns8:cos>1</ns8:cos><ns8:tests>false</ns8:tests><ns8:dataModule>false</ns8:dataModule><ns8:speakerphone>2-way</ns8:speakerphone><ns8:displayLanguage>english</ns8:displayLanguage><ns8:personalizedRingingPattern>1</ns8:personalizedRingingPattern><ns8:messageLampExt>{extension}</ns8:messageLampExt><ns8:muteButtonEnabled>true</ns8:muteButtonEnabled><ns8:ipSoftphone>false</ns8:ipSoftphone><ns8:survivableCOR>internal</ns8:survivableCOR><ns8:survivableTrunkDest>true</ns8:survivableTrunkDest><ns8:voiceMailNumber>7777</ns8:voiceMailNumber><ns8:offPremisesStation>false</ns8:offPremisesStation><ns8:displayModule>false</ns8:displayModule><ns8:remoteOfficePhone>false</ns8:remoteOfficePhone><ns8:lwcReception>spe</ns8:lwcReception><ns8:lwcActivation>true</ns8:lwcActivation><ns8:lwcLogExternalCalls>false</ns8:lwcLogExternalCalls><ns8:cdrPrivacy>false</ns8:cdrPrivacy><ns8:redirectNotification>true</ns8:redirectNotification><ns8:perButtonRingControl>true</ns8:perButtonRingControl><ns8:bridgedCallAlerting>false</ns8:bridgedCallAlerting><ns8:bridgedIdleLinePreference>false</ns8:bridgedIdleLinePreference><ns8:confTransOnPrimaryAppearance>false</ns8:confTransOnPrimaryAppearance><ns8:customizableLabels>true</ns8:customizableLabels><ns8:expansionModule>false</ns8:expansionModule><ns8:ipVideoSoftphone>false</ns8:ipVideoSoftphone><ns8:activeStationRinging>single</ns8:activeStationRinging><ns8:switchhookFlash>false</ns8:switchhookFlash><ns8:ignoreRotaryDigits>false</ns8:ignoreRotaryDigits><ns8:h320Conversion>false</ns8:h320Conversion><ns8:serviceLinkMode>as-needed</ns8:serviceLinkMode><ns8:multimediaMode>enhanced</ns8:multimediaMode><ns8:mwiServedUserType></ns8:mwiServedUserType><ns8:emergencyLocationExt>{extension}</ns8:emergencyLocationExt><ns8:alwaysUse>false</ns8:alwaysUse><ns8:precedenceCallWaiting>false</ns8:precedenceCallWaiting><ns8:autoSelectAnyIdleAppearance>false</ns8:autoSelectAnyIdleAppearance><ns8:coverageMsgRetrieval>true</ns8:coverageMsgRetrieval><ns8:autoAnswer>none</ns8:autoAnswer><ns8:dataRestriction>false</ns8:dataRestriction><ns8:idleAppearancePreference>false</ns8:idleAppearancePreference><ns8:callWaitingIndication>false</ns8:callWaitingIndication><ns8:attCallWaitingIndication>false</ns8:attCallWaitingIndication><ns8:distinctiveAudibleAlert>false</ns8:distinctiveAudibleAlert><ns8:restrictLastAppearance>true</ns8:restrictLastAppearance><ns8:adjunctSupervision>false</ns8:adjunctSupervision><ns8:perStationCpnSendCallingNumber>y</ns8:perStationCpnSendCallingNumber><ns8:busyAutoCallbackWithoutFlash>false</ns8:busyAutoCallbackWithoutFlash><ns8:audibleMessageWaiting>false</ns8:audibleMessageWaiting><ns8:imsFeatureSequencing>false</ns8:imsFeatureSequencing><ns8:displayClientRedirection>false</ns8:displayClientRedirection><ns8:selectLastUsedAppearance>false</ns8:selectLastUsedAppearance><ns8:coverageAfterForwarding>s</ns8:coverageAfterForwarding><ns8:directIpIpAudioConnections>true</ns8:directIpIpAudioConnections><ns8:ipAudioHairpinning>false</ns8:ipAudioHairpinning><ns8:stationSiteData><ns8:headset>false</ns8:headset><ns8:speaker>false</ns8:speaker><ns8:mounting>d</ns8:mounting><ns8:cordLength>0</ns8:cordLength></ns8:stationSiteData><ns8:abbrList><ns8:listType>system</ns8:listType><ns8:number>2</ns8:number></ns8:abbrList><ns8:buttons><ns8:number>1</ns8:number><ns8:type>call-appr</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3>r</ns8:data3><ns8:data4>n</ns8:data4><ns8:data5></ns8:data5><ns8:data6></ns8:data6></ns8:buttons><ns8:buttons><ns8:number>2</ns8:number><ns8:type>call-appr</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3>r</ns8:data3><ns8:data4>n</ns8:data4><ns8:data5></ns8:data5><ns8:data6></ns8:data6></ns8:buttons><ns8:buttons><ns8:number>3</ns8:number><ns8:type>call-appr</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3>r</ns8:data3><ns8:data4>n</ns8:data4><ns8:data5></ns8:data5><ns8:data6></ns8:data6></ns8:buttons><ns8:buttons><ns8:number>4</ns8:number><ns8:type>send-calls</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3></ns8:data3><ns8:data4></ns8:data4><ns8:data5></ns8:data5><ns8:data6></ns8:data6></ns8:buttons><ns8:buttons><ns8:number>5</ns8:number><ns8:type>release</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3></ns8:data3><ns8:data4></ns8:data4><ns8:data5></ns8:data5><ns8:data6></ns8:data6></ns8:buttons><ns8:buttons><ns8:number>6</ns8:number><ns8:type>ec500</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3></ns8:data3><ns8:data4></ns8:data4><ns8:data5></ns8:data5><ns8:data6>n</ns8:data6></ns8:buttons><ns8:buttons><ns8:number>7</ns8:number><ns8:type>extnd-call</ns8:type><ns8:data1></ns8:data1><ns8:data2></ns8:data2><ns8:data3></ns8:data3><ns8:data4></ns8:data4><ns8:data5></ns8:data5><ns8:data6></ns8:data6></ns8:buttons><ns8:nativeName></ns8:nativeName><ns8:buttonModules>0</ns8:buttonModules><ns8:unconditionalInternalDest></ns8:unconditionalInternalDest><ns8:unconditionalInternalActive>false</ns8:unconditionalInternalActive><ns8:unconditionalExternalDest></ns8:unconditionalExternalDest><ns8:unconditionalExternalActive>false</ns8:unconditionalExternalActive><ns8:busyInternalDest></ns8:busyInternalDest><ns8:busyInternalActive>false</ns8:busyInternalActive><ns8:busyExternalDest></ns8:busyExternalDest><ns8:busyExternalActive>false</ns8:busyExternalActive><ns8:noReplyInternalDest></ns8:noReplyInternalDest><ns8:noReplyInternalActive>false</ns8:noReplyInternalActive><ns8:noReplyExternalDest></ns8:noReplyExternalDest><ns8:noReplyExternalActive>false</ns8:noReplyExternalActive><ns8:sacCfOverride>n</ns8:sacCfOverride><ns8:lossGroup>19</ns8:lossGroup><ns8:timeOfDayLockTable></ns8:timeOfDayLockTable><ns8:emuLoginAllowed>false</ns8:emuLoginAllowed><ns8:ec500State>disabled</ns8:ec500State><ns8:muteOnOffHookInSCMode>false</ns8:muteOnOffHookInSCMode><ns8:type3pccEnabled>None</ns8:type3pccEnabled><ns8:calculateRoutePattern>false</ns8:calculateRoutePattern><ns8:enableReachStaDomainControl>s</ns8:enableReachStaDomainControl><ns8:multimediaEarlyAnswer>false</ns8:multimediaEarlyAnswer><ns8:bridgedApprOrigRestr>false</ns8:bridgedApprOrigRestr><ns8:callApprDispFormat>disp-param-default</ns8:callApprDispFormat><ns8:ipPhoneGroupId>{tn}</ns8:ipPhoneGroupId><ns8:xid>false</ns8:xid><ns8:stepClearing>false</ns8:stepClearing><ns8:fixedTei>false</ns8:fixedTei><ns8:endptInit>false</ns8:endptInit><ns8:isShortCallingPartyDisplay>true</ns8:isShortCallingPartyDisplay><ns8:location>{tn}</ns8:location><ns8:displayCallerId>true</ns8:displayCallerId><ns8:callerIdMsgWaitingIndication>false</ns8:callerIdMsgWaitingIndication><ns8:recallRotaryDigit>false</ns8:recallRotaryDigit><ns8:bridgingToneForThisExtension>n</ns8:bridgingToneForThisExtension><ns8:terminalNumberPart1>0</ns8:terminalNumberPart1><ns8:terminalNumberPart2>0</ns8:terminalNumberPart2><ns8:terminalNumberPart3>0</ns8:terminalNumberPart3><ns8:terminalNumberPart4>0</ns8:terminalNumberPart4><ns8:systemId></ns8:systemId><ns8:features></ns8:features><ns8:features2></ns8:features2><ns8:attendant>false</ns8:attendant><ns8:ipHoteling>false</ns8:ipHoteling></commProfile></commProfileList></commProfileSet><isCommPasswordSet>true</isCommPasswordSet></tns:user></tns:users>",
        "loginName":email,
        "groupData":[]
        }

        response = requests.put(data1['SM_UPDATE'], json = data, headers = sm_headers, verify = False)
        # print(response.text)

        data = {
            primarySM":"Waterloo SM","secondarySM":"","thirdSM":"","fourthSM":"","userData":{"tns:users":{"@xmlns:ns4":"http://xml.avaya.com/schema/import1","@xmlns:ns3":"http://xml.avaya.com/schema/import_csm_agent","@xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance","@xmlns:ns6":"http://xml.avaya.com/schema/import_scopia","@xmlns:ns5":"http://xml.avaya.com/schema/presence","@xmlns:ns8":"http://xml.avaya.com/schema/import_csm_cm","@xmlns:ns7":"http://xml.avaya.com/schema/import_sessionmanager","@xmlns:ns13":"http://xml.avaya.com/schema/deltaImport","@xmlns:ns9":"http://xml.avaya.com/schema/import_csm_b5800","@xmlns:ns12":"http://xml.avaya.com/schema/import_ce","@xmlns:ns11":"http://xml.avaya.com/schema/import_csm_mm","@xmlns:ns10":"http://xml.avaya.com/schema/import_mem_officelinx","@xmlns:tns":"http://xml.avaya.com/schema/import","@xsi:schemaLocation":"http://xml.avaya.com/schema/import userimport.xsd","tns:user":{"UserOrganizationDetails":null,"UserProvisionRules":null,"authenticationType":"basic","description":null,"displayName":"Tina Bali-Rampal","displayNameAscii":"Tina Bali-Rampal","dn":null,"isDuplicatedLoginAllowed":false,"isEnabled":true,"isVirtualUser":false,"givenName":"Tina","givenNameAscii":"Tina","honorific":null,"loginName":"tina.bali-rampal@sunlife.com","newLoginName":null,"emailId":null,"employeeNo":null,"department":null,"organization":null,"middleName":null,"managerName":null,"preferredGivenName":null,"preferredLanguage":"en_CA","source":"local","sourceUserKey":"none","status":"provisioned","suffix":null,"surname":"Bali-Rampal","surnameAscii":"Bali-Rampal","timeZone":"(-4:0)Eastern Time (US &amp; Canada)","title":null,"userName":"tina.bali-rampal","userPassword":"","commPassword":"","userType":null,"roles":{"role":"End-User"},"groups":{"group":[]},"localizedNames":null,"address":[],"securityIdentity":null,"ownedContactLists":{"contactList":{"name":"list-tina.bali-rampal_sunlife.com","isPublic":"false","contactListType":"general"}},"ownedContacts":null,"presenceUserDefault":null,"presenceUserACL":null,"presenceUserCLDefault":null,"commProfileSet":[{"commProfileSetName":"Primary","isPrimary":"true","handleList":{"handle":[{"handleName":"3419573","handleType":"sip","handleSubType":"username","domainName":"sunlife.com"},{"handleName":"+10013419573","handleType":"sip","handleSubType":"username","domainName":"sunlife.com"},{"handleName":"+3419573","handleType":"sip","handleSubType":"e164","domainName":"sunlife.com"}]},"commProfileList":{"commProfile":[{"commProfileType":"SessionManager","@xsi:type":"ns7:SessionManagerCommProfXML","@xmlns:ns7":"http://xml.avaya.com/schema/import_sessionmanager","ns7:primarySM":null,"ns7:secondarySM":null,"ns7:terminationAppSequence":null,"ns7:originationAppSequence":null,"ns7:confFactorySet":null,"ns7:survivabilityServer":null,"ns7:homeLocation":null,"ns7:maxSimultaneousDevices":null,"ns7:emergencyTerminationAppSequence":null,"ns7:emergencyOriginationAppSequence":null,"ns7:policyType":"fixed","ns7:thirdSM":null,"ns7:fourthSM":null}]}}],"isCommPasswordSet":true}}}}
        }




        # Session Manager Profile Setup
        response = requests.put(data1["SM_VALIDATE_PRIMARY"],json=data, headers=sm_headers, verify=False )





        return('success')


def main():

    extension = '3419573'
    email = 'tina.bali-rampal@sunlife.com'
    first_name = 'Tina'
    last_name = 'Bali-Rampal'
    location = 'Sun Life Waterloo King'
    tn = '1'

    try:
        result = sm(extension, email, first_name, last_name, location, tn)
        print(result)
    except Exception as e:
        print("Got the following error:", e)


if __name__ == '__main__':
    main()