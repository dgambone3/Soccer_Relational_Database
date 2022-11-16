from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df3 = pd.read_csv('https://data.heroku.com/dataclips/qpjgeenvjwcptrzbuigldpbsvvar.csv')
fig3 = px.bar(df3,x='player', y='conversion_rate')
app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
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
        id='example-graph',
        fig3ure=fig3,
        style={'height':'500'}
        ),
        style = {
            'width': '50%',
            'margin': 'auto'
            }
    )
])

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    Input('datatable-interactivity', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]



if __name__ == '__main__':
    app.run_server(debug=True)