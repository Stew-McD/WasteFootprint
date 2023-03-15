# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
import dash
import dash_bootstrap_components as dbc
from server import app

# custom imports
# ...

content = html.Div(
    [
        dbc.Row(style=dict(height="auto", position="auto", margin="60px"), 
                children=
                [
                # dbc.Col(
                #     html.Div(
                #         style=dict(align="right", marginTop=200, fontSize=20),
                #         children=[
                #         #     html.Img(
                #         #         style=dict(height="100%",width="100%", position="sticky"),
                #         #         src=app.get_asset_url('swiss.png')), 
                #         #     dcc.Markdown('''[source](https://www.bafu.admin.ch/bafu/en/home/topics/economy-consumption/economy-and-consumption-publications/publications-economy-and-consumption/eco-factors-switzerland.html)''')]
                #         #     ), width=2, align="left"
                #         # ),
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='left', fontSize=60, marginBottom=0, marginTop=10),
                        children = [
                            html.B("Our WasteFootprint Tool"),
                            html.H4("functions with the Brightway2 framework in Python"),
                            # html.H3(""),html.Br(),
                            # html.H3(""),
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=25, marginTop=10),
                        children = [
                            html.Br(),
                            html.B('* Based on identifying waste exchanges'),html.Br(),html.I(''),html.Br(),
                            html.B('* Exchanges are edited and custom methods written'),html.I(),html.Br(),html.Br(),
                            html.B("* Waste flows transformed into 'pseudo-biosphere' flows"),html.I(),html.Br(),html.Br(),
                            html.B("* Waste footprint calculations can be performed as with any standard LCIA method"),html.I(""),html.Br(),html.Br(),
                            html.B("* 14 methods are created for the waste categories"),html.Br(),html.Td(''),html.I('e.g. incineration, recycling, composting, open-burning, radioactive', style=dict(fontSize=20)),html.Br(),

                            ])], align="top"),
                dbc.Col(
                    html.Div(
                        style=dict(align="right", paddingLeft=100,fontSize=20, marginTop=50),
                        children=[
                            html.Img(
                                style=dict(height="80%",width="80%", position="right"),
                                src=app.get_asset_url('Flowchart_WasteFootprint.png')), 
                            # dcc.Markdown('''[source](https://research.chalmers.se/publication/519861/file/519861_Fulltext.pdf)''')
                            #
                    ]), align="center"),]),            
        # dbc.Row(style=dict(height="auto", position="auto", margin="60px"), children=
        #     [
        #         dbc.Col(
        #             html.Div(
        #                 style=dict(align="right", marginTop=20, fontSize=20, color='blue'),
        #                 children=[
        #                     dcc.Markdown('''Ratios of 'waste hazardousness' and 'circularity' for 1,400+ products'''),
        #                     html.Img(
        #                         style=dict(height="100%",width="100%"),
        #                         src=app.get_asset_url('rl_ratios.jpg')), 
        #                     dcc.Markdown('''[source](https://doi.org/10.1016/j.scitotenv.2022.160405)''')]),
        #                     align="left"
        #                     ),
            ])