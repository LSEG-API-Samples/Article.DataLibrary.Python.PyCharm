#|-----------------------------------------------------------------------------
#|            This source code is provided under the MIT license             --
#|  and is provided AS IS with no warranty or guarantee of fit for purpose.  --
#|                See the project's LICENSE.md for details.                  --
#|           Copyright Refinitiv 2023.       All rights reserved.            --
#|-----------------------------------------------------------------------------

"""
Example Code Disclaimer:
ALL EXAMPLE CODE IS PROVIDED ON AN “AS IS” AND “AS AVAILABLE” BASIS FOR ILLUSTRATIVE PURPOSES ONLY. REFINITIV MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, AS TO THE OPERATION OF THE EXAMPLE CODE, OR THE INFORMATION, CONTENT, OR MATERIALS USED IN CONNECTION WITH THE EXAMPLE CODE. YOU EXPRESSLY AGREE THAT YOUR USE OF THE EXAMPLE CODE IS AT YOUR SOLE RISK.
"""

import json
import refinitiv.data as rd



if __name__ == '__main__':
    rd.open_session(name='platform.rdp')


    request_definition = rd.delivery.endpoint_request.Definition(
        url="/data/news/v1/headlines",
        method=rd.delivery.endpoint_request.RequestMethod.GET,
        query_parameters={"query": "Thai Election"}
    )

    response = request_definition.get_data()
    # print(response.data.raw)
    headline = response.data.raw['data'][0]['newsItem']['itemMeta']['title'][0]['$']
    storyId = response.data.raw['data'][0]['storyId']
    print(headline)

    story_url = 'https://api.refinitiv.com/data/news/v1/stories/{storyId}'
    request_definition = rd.delivery.endpoint_request.Definition(
        url=story_url,
        method=rd.delivery.endpoint_request.RequestMethod.GET,
        path_parameters={"storyId": storyId}
    )
    response = request_definition.get_data()
    story = response.data.raw['newsItem']['contentSet']['inlineData'][0]['$']
    print(story)

    rd.close_session()

