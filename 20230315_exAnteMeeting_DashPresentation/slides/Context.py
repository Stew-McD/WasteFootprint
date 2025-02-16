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
        dbc.Row(style=dict(height="auto", position="auto"), 
            children=[
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='center', fontSize=80, marginBottom=20, marginTop=20),
                        children = [
                            html.B("Context"),
                            html.H2("The 'circular economy', supply-risk of critical raw materials, etc.")
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=50, marginBottom=15),
                        children = [
                            html.B(''),
                            ]),
                    html.Div(
                        style=dict(textAlign='center', fontSize=35, marginTop=50),
                        children = [
                            html.B('To promote circularity we need to measure circularity', style=dict(color='navy', marginBottom=10)),html.I(''),html.Br(),
                            html.B('To measure circularity we need to understand waste flows', style=dict(color='navy', marginBottom=10)),html.I(''),html.Br(),html.Br(),
                            html.P("Dozens of metrics have been proposed for calculating 'circularity'", style=dict(color='navy', marginBottom=5)),html.I('(but we need to quantify and classify the waste first!)', style=dict(fontSize=30, color='#CC5500', marginBottom=30)),html.Br(),html.Br(),
                            html.B("Waste ---> secondary raw material (SRM)"),html.Br(),html.I('Data is not good right now, but getting better', style=dict(fontSize=25)),html.Br(),
                            html.B("Ongoing work by CML et.al. - modelling EU's SRM system to 2050",style=dict(fontSize=30)),html.Br(),html.I('FutuRaM project (H2020): aiming to improve circularity and SRM availability',style=dict(fontSize=25)),html.Br(),
                            html.B('')
                            ])]),
                dbc.Col([
                    html.Div(
                        style=dict(align="right", paddingRight=50, marginTop=100, fontSize=20),
                        children=[
                            html.Img(
                                style=dict(marginBottom=50, height="100%",width="100%", position="sticky"),
                                src=app.get_asset_url('crms.png')), 
                            dcc.Markdown('''[source](https://www.futuram.eu/)'''),
                            html.Img(
                                style=dict(height="100%",width="100%", position="sticky"),
                                src=app.get_asset_url('futuram.jpg')),
                            dcc.Markdown('''[source](https://rmis.jrc.ec.europa.eu/?page=crm-list-2020-e294f6)''')])
                ], width=2, align="right"), 
                        
                        ], align="right", justify="center"),
        dbc.Row(style=dict(height="auto", position="left", paddingRight=150), children=[
            html.Div(
                        style=dict(align="left", color='red', fontSize=25, marginTop=60, marginLeft=300),
                        children=[
                            html.B("Current recycling rates are mostly very low!"),
                            html.Br(),
                            html.Img(
                                style=dict(height="60%",width="90%", position="left"),
                                src=app.get_asset_url('recycling.png')),
                            dcc.Markdown('''[source](https://www.euchems.eu/wp-content/uploads/2019/01/The-Periodic-Table-and-us-Handley-European-Commission.pdf)''')
                            ]
                            )], align="left"
            
        )])