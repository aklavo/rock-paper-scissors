# make a rock paper scissors app using the dash package
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='player1', type='text', value='Player 1'),
    dcc.Input(id='player2', type='text', value='Player 2'),
    html.Button(id='submit', n_clicks=0, children='Submit'),
    html.Div(id='output')
    ])

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('submit', 'n_clicks')],
    [dash.dependencies.State('player1', 'value'),
     dash.dependencies.State('player2', 'value')])
def update_output(n_clicks, player1, player2):
    return 'Player 1: {} \n Player 2: {}'.format(player1, player2)

if __name__ == '__main__':
    app.run_server(debug=True)
    
