*** Settings ***
Library      String
Library      Collections
Library      REST                  https://api-dev-dot-waybill-project.appspot.com/
Variables    createItemsWith.py

# Set expectations
#    Expect response    { "status": { "enum": [200, 201, 204, 400] } }
#    Expect response    { "seconds": { "maximum": 2} }

*** Variable ***
${filter}                  {"tender_id":13,"status":"ONROAD"}
${search_waybill_param}    {"method":"searchWaybills","filter":${filter},"integration_token":"YAZAN","limit":1}
${CreateItems}             {"method":"appendWaybillToARClaim","waybill_id":"260819","pa_id":"37","claim_loading_weight":37760,"claim_discharge_weight":"37460","claim_loading_date":"2021-01-16","claim_discharge_date":"2021-01-17","claim_discharge_arrive_date":"2021-01-17","destination_id":"91030008","cargo_id":2010000006,"origin_id":91090000,"item_url":"","cargo_name":"قمح سائب","late_fine":0,"compensation":0,"absence_fine":0,"loss_fine":23.538,"claim_amount":508.123,"tender_id":"13"}
*** Test Cases ***

search_waybill

    POST    /waybill    ${search_waybill_param}

    Output schema    response body data
    Object           response body
    String           response body found_rows    60

Create Items With
    ${Auto}=          call method    ${createItemsWith}    AutoComplete
    Log To Console    ${Auto}
    # POST      /tender_claim    ${AutoComplete}



