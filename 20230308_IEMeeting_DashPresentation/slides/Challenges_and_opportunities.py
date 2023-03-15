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
        dbc.Row(style=dict(height="auto", position="auto"), children=
            [
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='left', fontSize=45, marginBottom=20, marginTop=10, marginLeft=350),
                        children=[
                            html.B("Challenges & opportunities"),
                            html.H3("")
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=30, marginBottom=-20, marginLeft=300),
                        children = [
                            html.B("Data completeness:"),html.Br(),html.I('95% of waste has no defined end of life', style=dict(fontSize=25)),html.Br(),
                            html.B("Waste is not all the same"),html.Br(),html.I("Sometimes 'inert-waste' is just moving some rocks around", style=dict(fontSize=25)),html.Br(),
                            html.B("Economic allocation "), html.Br(), html.I('waste-footprint ∝ price', style=dict(fontSize=25))
                            ]),
                ],)
            ]),
        dbc.Row(style=dict(height="auto", position="auto", display='none'), children=
            [
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='right', fontSize=45, marginBottom=0, marginTop=0, marginRight=650),
                        children=[
                            html.B("Next steps..."),
                            html.H3("")
                            ]),
                    html.Div(
                        style=dict(textAlign='right', fontSize=30, marginBottom=100, marginRight=600),
                        children = [
                            html.B("Validation of method and robustness checks"),html.Br(),html.I('possible comparison with I/O or MFA?', style=dict(fontSize=25)),html.Br(),
                            html.B("Extension with case studies"),html.Br(),html.I('currently investigating batteries', style=dict(fontSize=25)),html.Br(),
                            html.B("Ex-ante calculations"), html.Br(), html.I('changing the background for energy, steel, etc', style=dict(fontSize=25)),
                            html.P(""),
                            html.B("Much later... integrating FutuRaM's SRM models"), html.Br(), html.I('inc. product level, and consideration of re-X strategies', style=dict(fontSize=25))
                        
                            ]),
                ],)
            ]),
        
        ])