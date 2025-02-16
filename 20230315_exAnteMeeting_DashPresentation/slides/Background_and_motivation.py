W# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

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
                            html.B("Background and Motivation"),
                            ]),
                    # write a series of dot points
                    html.Div(
                        style=dict(textAlign='left', fontSize=30, paddingBottom=20, paddingLeft=100),
                        children=[
                            html.Ul([
                                html.Li("To continue to improve our future state models, we need to consider waste backgrounds"),
                                html.Br(),
                                html.Li("This is a worthwhile challenge given that Reinhard et.al. (2019) demonstrates that a relatively large proportion of environmental impacts on all product systems in ecoinvent come from background waste processes "),
                                html.Br(),
                                html.Li("Also, as the EU continues to implement specific waste goals related to the circular economy and the prioritization of particular waste treatments, it is clear that the “current state” scenario will rapidly lose relevance "),
                            ])
                        ]),
                ], width=9, align="left", )
            ]
        )
    ]
)

