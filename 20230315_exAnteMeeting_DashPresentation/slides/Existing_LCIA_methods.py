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
        dbc.Row(style=dict(height="auto", position="auto", margin="60px"), children=
            [
                dbc.Col(
                    html.Div(
                        style=dict(align="right", marginTop=200, fontSize=20),
                        children=[
                            html.Img(
                                style=dict(height="100%",width="100%", position="sticky"),
                                src=app.get_asset_url('swiss.png')), 
                            dcc.Markdown('''[source](https://www.bafu.admin.ch/bafu/en/home/topics/economy-consumption/economy-and-consumption-publications/publications-economy-and-consumption/eco-factors-switzerland.html)''')]
                            ), width=2, align="left"
                        ),
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='center', fontSize=70, marginBottom=30, marginTop=20),
                        children = [
                            html.B("Related methods in LCIA"),
                            html.H2("Mostly material-demand focussed")
                            
                            ]),
                    html.Div(
                        style=dict(textAlign='center', fontSize=40, marginBottom=20),
                        children = [
                            html.B('But:'), html.I('   "waste is not a service!"'),html.Br(),
                            ]),
                    html.Div(
                        style=dict(textAlign='center', fontSize=30),
                        children = [
                            html.B('* Swiss Eco Factors 2020'),html.Br(),html.I('waste to landfill (invented units)', style=dict(fontSize=20)),html.Br(),
                            html.B('* EDIP 2003/EN1584'),html.Br(),html.I('focus on radioactive/hazardous (kg)', style=dict(fontSize=20)),html.Br(),html.Br(),
                            html.B("* Crustal scarcity indicator / abiotic depletion"),html.Br(),html.I('(looking from the reversed perspective)', style=dict(fontSize=20)),html.Br(),html.Br(),
                            html.B("There is currently no convienient and flexible way to calculate waste flows in LCA..."),html.I(''),html.Br(),
                            html.B('')
                            ])], align="center"),
                dbc.Col(
                    html.Div(
                        style=dict(align="right", fontSize=20, marginTop=200),
                        children=[
                            html.Img(
                                style=dict(height="100%",width="100%", position="sticky"),
                                src=app.get_asset_url('crustal.png')), 
                            dcc.Markdown('''[source](https://research.chalmers.se/publication/519861/file/519861_Fulltext.pdf)''')]
                            ), width=2, align="right"
                        ),
            ],
            justify="center"
            
)])