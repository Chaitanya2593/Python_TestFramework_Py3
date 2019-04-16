*** Settings ***
Documentation     Example to show the test cases in framework
...
Variables         ../../AllFolders_location.py
Variables         ../../commonVariables.py
Library           ../../TestsAll/Allkeywords/WebApplicationKeywords.py
Library           ../../TestsAll/Allkeywords/WinAppKeywords.py

*** Variables ***
${env_from_CMD_line}    TEC
${testexecution_key}    ${EMPTY}
${env_name}       SAN

*** Test Cases ***
CommonPlaceMasterExcel
    ${source}    Catenate    SEPARATOR=    ${cmtTestDataFolder}    MASTER_SFTP.xlsx
    ${destination}    Catenate    SEPARATOR=    ${cmtTableDataFolder}    MASTER.xlsx
    place master excel in table data folder    ${source}    ${destination}

CreateCSVFilesValidDataForAllTables
    [Documentation]    Creats the csv files
    [Setup]    Env_variableS
    The Master excel file should be created with Valid Data    50000    CONSUMER|OPTIN|CHILD|EXTERNALIDENTITY|CONSUMERINTEREST|PET|ASSET|CONSUMERTAG|CONSUMERSCORE|CONSUMERRELATIONSHIP
    Convert the Excel sheets to CSVs    ${cmtTableDataFolder}    ${cmtEncryptedFilesFolder}

DCMTT-455_TestCase_name
    [Documentation]    Test Case :: DCMTT-455_TestCase_name
    ...
    ...    Jira ID:: DCMTT-455
    [Setup]    Env_variableS
    ${drvr}=    step1    ${parameter1}    ${parameter12}    ${parameter13}
    ${drvr1}=    step2    ${parameter1}    ${parameter12}    ${parameter13}
    [Teardown]    Clear_IOParameters


*** Keywords ***
UploadtoSFTP
    [Arguments]    ${ftpSRVRname}    ${ftpUname}    ${ftpPword}    ${EncryptedfilePATH}    ${ftpRemoteFoldername}
    [Documentation]    This Keyword to send the file to the SFTP server
    Upload a File to FTP    ${ftpSRVRname}    ${ftpUname}    ${ftpPword}    ${EncryptedfilePATH}    ${ftpRemoteFoldername}

PGPfileEncryption
    [Arguments]    ${encryptiontoolEXEpath}    ${keyRINGfilepath}    ${tobeEncryptedfilepath}
    PGP encryption of File    ${encryptiontoolEXEpath}    Encrypt file    ${tobeEncryptedfilepath}
    ${EncryptedfilePATH}=    Catenate    SEPARATOR=    ${tobeEncryptedfilepath}    .pgp
    [Return]    ${EncryptedfilePATH}

Check records in SFMC
    [Arguments]    ${drvr}    ${table_name}    ${table_primary_key}
    ${drvr2}=    Select the Table in Data Extensions    ${drvr}    ${table_name}    Records
    ${drvrkey3}=    Validate Record data in SFMC    ${drvr2}    ${table_name}    ${table_primary_key}
    [Return]    ${drvrkey3}

Env_variableS
    Set Global Variable    ${CLIENTSECRET}
    ${EnvVar}=    Get_env_Variables    ${env_name}
    ${SFMC_USERNAME}=    Evaluate    $EnvVar.get('GMAIL_USERNAME')
    Set Global Variable    ${SFMC_USERNAME}
    ${SFMC_APIURL}=    Evaluate    $EnvVar.get('GMAIL_APIURL')
    Set Global Variable    ${SFMC_APIURL}
    ${SFMC_SFTP}=    Evaluate    $EnvVar.get('GMAIL_SFTP')
    Set Global Variable    ${SFMC_SFTP}
    ${SFMC_PASSWORD}=    Evaluate    $EnvVar.get('GMAIL_PASSWORD')
    Set Global Variable    ${SFMC_PASSWORD}

Xray_StatusUpate

    Update The Jira Xray Status    DCMTT-DCMTT-455_TestCase_name    ${TEST_STATUS}    ${testexecution_key}

TestCase_Teardown
    Xray_StatusUpate
    Clear_IOParameters
