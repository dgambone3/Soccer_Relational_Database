from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


df1 = pd.read_csv('https://data.heroku.com/dataclips/oelkwsoearfkimaiwcvvclqlydxt.csv')
fig1 = px.bar(df1,x='club', y=['wins', 'losses','draws'])
df2 = pd.read_csv('https://data.heroku.com/dataclips/vuauqzvkgdpakdrhqorvioayxxtj.csv')
fig2 = px.bar(df2,x='club', y='managers')
df3 = pd.read_csv('https://data.heroku.com/dataclips/qpjgeenvjwcptrzbuigldpbsvvar.csv')
fig3 = px.bar(df3,x='player', y='conversion_rate')
df4 = pd.read_csv('https://data.heroku.com/dataclips/hhfumvcpodmosvhhqolavkffnrtb.csv')
fig4 = px.bar(df4,x='home', y='goal_differential')
df5 = pd.read_csv('https://data.heroku.com/dataclips/ylwuifcpwtcedgrwkhdngfkzdyoa.csv')
fig5 = px.bar(df5,x='team_name', y='championships',color='league')
df6 = pd.read_csv('https://data.heroku.com/dataclips/iihooevwifxklrdluwpxjsttjumg.csv')
fig6 = px.line(df6,x='year', y='days_duration', color='league_name', markers=True)





app.layout = html.Div([
    dash_table.DataTable(
        id='datatable1',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df1.columns
        ],
        data=df1.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        style_table = {'width': '50%','margin': 'auto'},
        style_cell={
        'height': 'auto',
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
        }
    ),
    html.Div(
        dcc.Graph(
        id='example-graph1',
        figure=fig1,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    ),
    dash_table.DataTable(
        id='datatable2',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df2.columns
        ],
        data=df2.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        style_table = {'width': '50%','margin': 'auto'},
        style_cell={
        'height': 'auto',
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
        }
    ),
    html.Div(
        dcc.Graph(
        id='example-graph2',
        figure=fig2,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    ),
    dash_table.DataTable(
        id='datatable3',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df3.columns
        ],
        data=df3.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        style_table = {'width': '50%','margin': 'auto'},
        style_cell={
        'height': 'auto',
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
        }
    ),
    html.Div(
        dcc.Graph(
        id='example-graph3',
        figure=fig3,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    ),
    dash_table.DataTable(
        id='datatable4',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df4.columns
        ],
        data=df4.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        style_table = {'width': '50%','margin': 'auto'},
        style_cell={
        'height': 'auto',
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
        }
    ),
    html.Div(
        dcc.Graph(
        id='example-graph4',
        figure=fig4,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    ),
    dash_table.DataTable(
        id='datatable5',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df5.columns
        ],
        data=df5.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        style_table = {'width': '50%','margin': 'auto'},
        style_cell={
        'height': 'auto',
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
        }
    ),
    html.Div(
        dcc.Graph(
        id='example5',
        figure=fig5,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    ),
    dash_table.DataTable(
        id='datatable6',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df6.columns
        ],
        data=df6.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        style_table = {'width': '50%','margin': 'auto'},
        style_cell={
        'height': 'auto',
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
        }
    ),
    html.Div(
        dcc.Graph(
        id='example-graph6',
        figure=fig6,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    )
])

