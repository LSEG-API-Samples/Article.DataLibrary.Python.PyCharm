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
import pandas as pd
import matplotlib.pyplot as plt
import refinitiv.data as rd
from refinitiv.data.content import historical_pricing
from refinitiv.data.content.historical_pricing import Intervals


if __name__ == '__main__':
    # Open Platform Session
    rd.open_session(name='platform.rdp')
    # Getting Data
    universe = 'META.O'
    response = historical_pricing.summaries.Definition(
        universe=universe,
        interval=Intervals.DAILY,  # Supported intervals: DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY.
        count=10,
        fields=['BID', 'ASK', 'OPEN_PRC', 'HIGH_1', 'LOW_1', 'TRDPRC_1']
    ).get_data()

    # Preparing data for plotting a graph
    # Add RIC name to be Dataframe column
    response.data.df['Instrument'] = universe
    # Reset index
    response.data.df.reset_index(level=0, inplace=True)
    # Plotting Graph
    dataPlot = pd.DataFrame(response.data.df,
                            columns=['Instrument', 'Date', 'BID', 'ASK', 'OPEN_PRC', 'TRDPRC_1', 'HIGH_1', 'LOW_1'])
    dataPlot.sort_values('Date', ascending=True, inplace=True)
    dataPlot.plot(x='Date', y=['BID', 'ASK', 'OPEN_PRC', 'TRDPRC_1', 'HIGH_1', 'LOW_1'], figsize=(14, 7))
    plt.show()
    # Close session
    rd.close_session()
