*** Settings ***
Documentation     An example resource file
Library           page_objects.py
Library           keywords.py

*** Variables ***
${URL}            https://atomcream.com/
${BROWSER}        chrome

*** Test Cases ***
Smoke home
    [Documentation]    Detailed info about test
    Open Browser    ${URL}  ${BROWSER}
