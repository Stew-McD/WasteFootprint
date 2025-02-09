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
                        style=dict(textAlign='left', fontSize=60, marginBottom=20, marginTop=10),
                        children = [
                            html.B("Concurrent research"),
                            html.H3("Rafael Laurenti et.al. (2023)"),
                            # html.H3(""),html.Br(),
                            # html.H3(""),
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=25, marginBottom=15),
                        children = [
                            html.B("'Analyzing the relationship between product waste footprints and environmental damage:"), html.Br(),html.I("A life cycle analysis of 1,400+ products'", style=dict(fontSize=25)),html.Br(),
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=23, marginTop=20),
                        children = [
                            html.Br(),
                            html.B('* Method based on solving demand vectors'),html.Br(),html.I(''),html.Br(),
                            html.B('* Found correlation of LCIA methods to waste footprints'),html.Td(''),html.I('(esp. human health, material demand)', style=dict(fontSize=15)),html.Br(),html.Br(),
                            html.B("* Calculated simple measures of 'waste hazardousness' and 'circularity' "),html.I(),html.Br(),html.Br(),
                            html.B("* But.... The method is slow, inconvienient and leads to multiple counting"),html.I(),html.Br(),

                            ])], align="center"),
                dbc.Col(
                    html.Div(
                        style=dict(align="right", paddingLeft=50, fontSize=20, marginTop=0),
                        children=[
                            html.Img(
                                style=dict(height="80%",width="80%", position="right"),
                                src=app.get_asset_url('rl_poo.jpg')), 
                            # dcc.Markdown('''[source](https://research.chalmers.se/publication/519861/file/519861_Fulltext.pdf)''')
                            #
                    ]), align="center"),]),            
        dbc.Row(style=dict(height="auto", position="auto", paddingTop=100, margin="60px"), children=
            [
                dbc.Col(
                    html.Div(
                        style=dict(align="right", marginTop=20, fontSize=20, color='blue'),
                        children=[
                            dcc.Markdown('''Ratios of 'waste hazardousness' and 'circularity' for 1,400+ products (that is, the sum of relevant categories)/total-waste'''),
                            html.Img(
                                style=dict(height="100%",width="100%"),
                                src=app.get_asset_url('rl_ratios.jpg')), 
                            dcc.Markdown('''[source](https://doi.org/10.1016/j.scitotenv.2022.160405)''')]),
                            align="left"
                            ),
            ])])