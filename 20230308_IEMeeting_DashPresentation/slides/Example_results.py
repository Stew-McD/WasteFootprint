# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
import dash
import dash_bootstrap_components as dbc
from server import app

# custom imports
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.io import read_json, renderers
renderers.default = "browser"

dir_box = "/home/stew/code/gh/WasteFootprintTestCases/MacroStudy-Markets/results/plotly_box/Methods/"
dir_scat = "/home/stew/code/gh/WasteFootprintTestCases/MacroStudy-Markets/results/plotly_scatter/WasteVSMethod/"
dir_waste = "/home/stew/code/gh/WasteFootprintTestCases/MacroStudy-Markets/results/plotly_box/Waste/"

j_scat = dir_scat + "0.8286R2_market-selection_total-solid_vs_crustal-scarcity-potential-(CSP)_cutoff391_log-log.json"
j_circ = dir_waste + "market-selection_circ_vs_prod_sub_category_cutoff391_log.json"
j_total = dir_waste + "market-selection_total_vs_prod_sub_category_cutoff391_log.json"

[fig_scat, fig_circ, fig_total] = [read_json(j, output_type='Figure', skip_invalid=False, engine=None) for j in [j_scat, j_circ, j_total]]

for fig in [fig_scat, fig_circ, fig_total]:
    ytit = fig.layout.yaxis.title.text.replace("- log", "")
    fig.update_layout(  yaxis_title=ytit,
                        yaxis_title_font_size = 20,
                        xaxis_title_font_size = 20,
                        xaxis_tickfont_size=20,
                        yaxis_ticklabeloverflow="allow",
                        xaxis_title="WasteFootprint (total solid): Specific waste production in supply chain (kg/kg)",
                        title_text=None,
                        showlegend=True,
                        updatemenus=[dict()],
                        autosize=False,
                        minreducedwidth=50,
                        minreducedheight=250,
                        width=1600,
                        height=900,
                        template="ggplot2"
                        )


fig_scat.update_layout(yaxis_title="Crustal scarcity potential (CSP) [kg.Si(eq)/kg]", yaxis_tickfont_size=20, xaxis_tickfont_size=20, yaxis_title_font_size = 20, xaxis_title_font_size = 20)
fig_circ.update_layout(yaxis_showticklabels=False, xaxis_title_text="'Circularity' vs. product category WasteFootprint (total solid)" )
fig_total.update_layout(yaxis_showticklabels=False)



content = html.Div(
    [
        dbc.Row(
            style=dict(paddingLeft=70, marginTop=60, paddingBottom=300), children=
            [
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='left', fontSize=45, marginBottom=40, marginRight=20, marginTop=20),
                        children=[
                            html.B("Application of the WasteFootprint tool"),
                            html.H2("Macro-study in EcoInvent 3.9.1")
                            ]),
                    html.Div(
                        style=dict(textAlign='left', fontSize=25, marginRight=20, marginBottom=20),
                        children = [
    
                            html.P("* Filtered to ~1500 'market activities'"),
                            html.P("* Calculated waste footprints & LCIA methods (~30)"),
                            html.P("Some results:", style=dict(fontWeight="bold", paddingTop=100, fontSize=35)),
                            html.P("* Identified strong correlations between some methods"),
                            html.P("* Identified top waste producing activities"),
                            html.P("* Identified supply-chain hotspots"),
                            html.P("* Learned about cocoons"),
                            ]),

            ]),
                dbc.Col([
                    html.Div(
                        style=dict(textAlign='right', fontSize=40, marginBottom=40, paddingRight=80, marginTop=100),
                        children=[
                            html.Img(
                                style=dict(marginTop=80, height="80%",width="80%", position="sticky"),
                                src=app.get_asset_url('corr.png'))
                            ]),

            ],style=dict(align='right'))
                
                ]),
        dbc.Row(
            style=dict(paddingLeft=100, paddingBottom=200, backgroundColor='white', color='black'), 
            children=[
                html.Div([
                    html.P('WasteFootprint (total solid) vs. product category for 1588 market activities in in the EcoInvent cutoff 3.9.1 database', style=dict(fontSize=25)),
                    dcc.Graph(figure=fig_total, style=dict(marginBottom=200, width="100%"))]),
                html.Div([
                    html.P("'Circularity' vs. product category WasteFootprint (total solid) for 1588 market activities in in the EcoInvent cutoff 3.9.1 database", style=dict(fontSize=25, fontColor='white' , marginBottom=0)),
                    html.I("The 'circularity' is defined as (recycled + composted + digested)/(total waste) as in Laurenti et.al. (2023)", style=dict(fontSize=20, marginBottom=0, fontColor='white'))]),
                    dcc.Graph(figure=fig_circ, style=dict(width="100%",marginBottom=200,height="200%")),
                html.Div([
                    html.P("WasteFootprint (total solid) vs. crustal scarcity potential (CSP) for 1588 market activities in the EcoInvent cutoff 3.9.1 database", style=dict(fontSize=25, marginBottom=0, fontColor='white' ))]),
                    dcc.Graph(figure=fig_scat, style=dict(width="100%",marginBottom=200,height="200%"))]),
    ]
)
