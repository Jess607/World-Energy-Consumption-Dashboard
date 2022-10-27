from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


#read in data 
df=pd.read_csv('df_countries.csv')



#Initialize dash app
app=Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server=app.server


#Create app layout
app.layout=dbc.Container([ 
            dbc.Row([
                dbc.Col(html.H3('World Energy Consumption'), width=6)],
             justify='center'),


            dbc.Row([
                dbc.Col(
                    dcc.Markdown(id='markdown', children=''), width=12, className='text-center'),

                    dbc.Col(
                    dcc.Graph(id='choro-fig', figure={}),
                    width=12, 
                     ),
                     
                    ]),

            dbc.Row([
                dbc.Col([
                    dbc.Col(html.H6('Select Energy Source'), width=6),
                    dbc.RadioItems(id='radio-items',
                    options=[{'label': 'Primary Energy Consumption', 'value': 'primary_energy_consumption'},
                            {'label': 'Coal Consumption', 'value': 'coal_consumption'},
                            {'label': 'Gas Consumption', 'value': 'gas_consumption'},
                            {'label': 'Renewables Consumption', 'value': 'renewables_consumption'},
                            {'label': 'Wind Consumption', 'value': 'wind_consumption'}
                            ], value='primary_energy_consumption')]),

                ])

        ])

          
#create a function that returns needed variables of dataframe for visualization
def grouped(df, var, year):
    data=df.groupby(['year', 'country']).sum()[var].to_frame().reset_index()
    df_1=data[data['year']==year]
    return df_1

#Create app callback decorator
@app.callback(
    [Output(component_id='markdown', component_property='children'),
    Output(component_id='choro-fig', component_property='figure')], 
    Input(component_id='radio-items', component_property='value')
)

def update_graph(user_input):
        if user_input=='primary_energy_consumption':
            dataframe=grouped(df=df, var='primary_energy_consumption', year=2019)
            fig=px.choropleth(dataframe, locations='country',
                        locationmode="country names", color='primary_energy_consumption', scope="world")
            fig.update_layout(paper_bgcolor="white")
            fig.update_layout(autosize=True, margin=dict(l=0, r=60, t=50, b=50))
            header= 'Primary Energy Consumption In Terrawatts-hr'
            return header, fig 

        elif user_input=='coal_consumption':
            dataframe=grouped(df=df, var='coal_consumption', year=2019)
            fig=px.choropleth(dataframe, locations='country',
                        locationmode="country names", color='coal_consumption', scope="world")
            fig.update_layout(paper_bgcolor="white")
            fig.update_layout(margin=dict(l=0, r=60, t=50, b=50))
            header= 'Total Coal Consumption In Terrawatts-hr'
            return header, fig 

        
        elif user_input=='gas_consumption':
            dataframe=grouped(df=df, var='gas_consumption', year=2019)
            fig=px.choropleth(dataframe, locations='country',
                        locationmode="country names", color='gas_consumption', scope="world")
            fig.update_layout(paper_bgcolor="white")
            fig.update_layout(margin=dict(l=0, r=60, t=50, b=50))
            header= 'Total Gas Consumption In Terrawatts-hr'
            return header, fig 

        elif user_input=='renewables_consumption':
            dataframe=grouped(df=df, var='renewables_consumption', year=2019)
            fig=px.choropleth(dataframe, locations='country',
                        locationmode="country names", color='renewables_consumption', scope="world")
            fig.update_layout(paper_bgcolor="white")
            fig.update_layout(margin=dict(l=0, r=60, t=50, b=50))
            header= 'Renewables Energy Consumption In Terrawatts-hr'
            return header, fig 

        elif user_input=='wind_consumption':
            dataframe=grouped(df=df, var='wind_consumption', year=2019)
            fig=px.choropleth(dataframe, locations='country',
                        locationmode="country names", color='wind_consumption', scope="world")
            fig.update_layout(paper_bgcolor="white")
            fig.update_layout(margin=dict(l=0, r=60, t=50, b=50))
            header= 'Total Wind Consumption In Terrawatts-hr'
            return header, fig 

 

# Run dash app
if __name__ == '__main__':
    app.run_server(port=4050)

