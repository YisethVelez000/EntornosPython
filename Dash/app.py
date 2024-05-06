# Importamos las bibliotecas necesarias para el proyecto de dash
from dash import Dash, html, dash_table,dcc
import pandas as pd
import plotly.express as px 
import dash_bootstrap_components as dbc


# Incorporamos la data del api de robos 
df = pd.read_json("https://www.datos.gov.co/resource/9vha-vh9n.json?")

# Iniciamos la app
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout app
app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(html.H2("Robos"), width=12)
        ]
    ),
    dbc.Row([
        dbc.Col(dash_table.DataTable(data=df.to_dict('records'), page_size=10))
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.bar(df, x='municipio', y='fecha_hecho', title='Robos por municipio y fecha de hecho')))
    ])    
])

# Corremos la app 
if __name__ == '__main__':
    app.run(debug=True)