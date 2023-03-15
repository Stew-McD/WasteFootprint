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
                        style=dict(align="right", fontSize=20),
                        children=[
                            html.Img(
                                style=dict(marginTop=80, height="100%",width="100%", position="sticky"),
                                src=app.get_asset_url('wastefootprint.png')), 
                            dcc.Markdown('''[source](https://www.colorado.edu/ecenter/2020/12/10waste-and-its-contribution-climate-change)''')]
                            ), width=3, align="right"
                        ),
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='left', fontSize=90, paddingBottom=80, marginTop=60),
                        children=[
                            html.B("Waste footprints in LCA"),
                            html.H3("      Liz and Stewart, with Felipe and Stefano")
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=50, marginBottom=15),
                        children = [
                            html.B('How much waste is hidden in supply chains?'),
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=40),
                        children = [
                            html.B('   Where does it go?'),html.I('   (incineration, landfill..)', style=dict(fontSize=20)),html.Br(),
                            html.B('   Where are the hotspots?'),html.I('   (construction, mining, energy?)', style=dict(fontSize=20)),html.Br(),
                            html.B('   Where could be opportunities for improvement?'),html.Br(),
                            html.B('   Why should we care?')
                            ])], align="left"),
            ],
            justify="center"
            
)])