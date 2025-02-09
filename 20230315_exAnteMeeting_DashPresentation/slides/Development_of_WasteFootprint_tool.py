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
        dbc.Row(style=dict(height="auto", position="center", paddingLeft=100, justify='center'), children=
            [
            
                dbc.Col([
                    
                    html.Div(
                        style=dict(textAlign='left', fontSize=60, paddingBottom=40, marginTop=60, marginLeft=100, paddingLeft=100),
                        children=[
                            html.B("Development of the WasteFootprint tool"),
                            ]),
                    # write a series of dot points
                    html.Div(
                        style=dict(textAlign='left', fontSize=30, paddingBottom=20, paddingLeft=100),
                        children=[
                            html.Ul([
                                html.Li("Thus, we were motivated to create a flexible and policy-driven approach to understanding a product’s demand on the waste management system both now and in the future to ensure that models of circularity and improvements in technology and policy for waste are included in LCA modeling."),
                                html.Br(),
                                html.Li("Liz developed a protocol and simple program to translate trends in EOL management for future background LCA systems. At this point, Stewart took off with the program to create higher level circularity analysis for waste."),
                                html.Br(),
                            ])
                        ]),
                ], width=9, align="left", )
            ]
        )
    ]
)

