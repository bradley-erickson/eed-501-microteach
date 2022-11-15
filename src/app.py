# package imports
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.JOURNAL,
        dbc.icons.FONT_AWESOME
    ],
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1'
        }
    ],
    title='EED 501 - Microteach'
)

loops = {
    'while': {
        'code': 'time_left = 15\nwhile time_left > 0:\n    teach_for_one_minute()\n    time_left -= 1',
        'name': 'While'
    },
    'for': {
        'code': 'loops = ["while", "for", "do-while"]\nfor loop in loops:\n    create_loop_card(loop)',
        'name': 'For'
    },
    'do-while': {
        'code': '',
        'name': 'Do While'
    }
}

def create_loop_card(loop):
    l = loops[loop]
    card = dbc.Col(
        [
            dbc.Card(
                [
                    html.H3(l['name'], className='text-center'),
                    dcc.Markdown(f'```python\n{l["code"]}\n```'),
                    html.Img(
                        src=f'assets/{loop} loop.png',
                        width='100%'
                    )
                ],
                body=True
            )
        ],
        md=4,
        xl=3
    )
    return card


types_of_loops = ['while', 'for', 'do-while']
tol_cards = dbc.Row(
    [create_loop_card(loop) for loop in types_of_loops],
    justify='center'
)

def serve_layout():
    return dbc.Container(
        [
            tol_cards
        ],
        fluid=True
    )

app.layout = serve_layout
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
