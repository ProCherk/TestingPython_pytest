import requests
from configuration import SERVICE_URL
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)  # get
    response = Response(r)

    response.assert_status_code(200).validate(POST_SCHEMA)

    # print(response.json())
    # print(len(response.json()))




'''
    Check response include json data

    print('response: 👉️', response)  # response: 👉️ <Response [204]>
    print('response.text: 👉️', response.text)  # response.text: 👉️ ""

    # response.status_code: 👉️ 204
    print('response.status_code: 👉️', response.status_code)

    print('response.headers: 👉️', response.headers)

    if (response.status_code != 204
            and 'content-type' in response.headers
            and 'application/json' in response.headers['content-type']):
        parsed = response.json()
        print('✅ parsed response: 👉️', parsed)
    else:
        # 👇️ this runs
        print('⛔️ conditions not met')
'''
