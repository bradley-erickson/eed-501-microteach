# package imports
import base64
import dash
from dash import html, dcc, clientside_callback, ClientsideFunction, Output, Input, State
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.JOURNAL,
        dbc.icons.FONT_AWESOME,
        '//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/default.min.css'
    ],
    external_scripts=[
        '//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js'
    ],
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1'
        }
    ],
    title='EED 501 - Microteach'
)


intro = dbc.Row(
    dbc.Card(
        [
            html.H1('Loops'),
            'Bradley Erickson'
        ],
        class_name='border-0 text-center'
    ),
    id='home',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)

overview = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H2('Purpose'),
                    'Repeat some ',
                    html.Div('code', className='d-inline-block bg-info p-1 text-white border border-dark mb-1'),
                    ' whenever a ',
                    html.Div('condition', className='d-inline-block bg-primary border rounded-opposites p-1 text-white border-dark'),
                    ' is true.'
                ],
                body=True,
                class_name='text-center mb-4'
            ),
            md=5,
            xl=4
        ),
        dbc.Col(
            dbc.Card(
                [
                    html.H2('Types'),
                    html.Ul(
                        [
                            html.Li('While'),
                            html.Li('For'),
                            html.Li('Do While')
                        ]
                    )
                ],
                body=True
            ),
            md=5,
            xl=4
        )
    ],
    id='overview',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


loops = {
    'while': {
        'code': 'int i = 0;\nwhile (i < 5) {\n\trepeatedCode();\n\ti++;\n}',
        'name': 'While',
        'purpose': 'Run code any number of times [0, ∞)',
        'use-cases': [
            'Listening for events',
            'Connecting to servers',
            'Parsing text with unknown lenght'
        ]
    },
    'for': {
        'code': 'for (int i = 0; i < 5; i++) {\n\trepeatedCode();\n}',
        'name': 'For',
        'purpose': 'Run code a set number of times [0, X]',
        'use-cases': [
            'Create visuals for each item'
        ]
    },
    'do-while': {
        'code': 'int i = 0;\ndo {\n\trepeatedCode();\n\ti++;\n} while (i < 5);',
        'name': 'Do While',
        'purpose': 'Run code at least once, but can repeat any number of times [1, ∞)',
        'use-cases': ''
    }
}


def create_loop_card(loop):
    l = loops[loop]
    card = dbc.Col(
        [
            dbc.Card(
                [
                    html.H2(l['name'], className='text-center'),
                    html.H4('Purpose:'),
                    html.P(l['purpose']),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4('Structure:'),
                                    html.Img(
                                        src=b64_image(f'assets/{loop} loop.png'),
                                        width='100%'
                                    )
                                ],
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.H4('Example Code:'),
                                    dcc.Markdown(f'```java\n{l["code"]}\n```'),
                                    html.H4('Use Cases:'),
                                    html.Ul([html.Li(u) for u in l['use-cases']]) if type(l['use-cases']) == list else html.P(l['use-cases'])
                                ],
                                md=6
                            )
                        ]
                    )
                ],
                body=True
            )
        ],
        md=8,
        xl=6
    )
    return card


types_of_loops = ['while', 'for', 'do-while']
tol_cards = html.Div(
    [
        dbc.Row(
            create_loop_card(loop),
            id=loop,
            justify='center',
            align='center',
            class_name='h-100 w-100'
        ) for loop in types_of_loops
    ]
)

next = dbc.Button(
    html.I(className='fas fa-chevron-right'),
    id='next',
    n_clicks=0,
    class_name='btn-circle btn-xl position-fixed top-50 end-0 me-2',
    color='light'
)

prev = dbc.Button(
    html.I(className='fas fa-chevron-left'),
    id='prev',
    n_clicks=0,
    class_name='btn-circle btn-xl position-fixed top-50 ms-2',
    color='light'
)

def serve_layout():
    return dbc.Container(
        [
            dcc.Location(id='location'),
            dbc.Row(
                [
                    intro,
                    overview,
                    tol_cards
                ],
                class_name='flex-nowrap',
                style={'height': '95vh'}
            ),
            next,
            prev
        ],
        fluid=True,
    )


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='change_pages'),
    Output('location', 'hash'),
    Input('prev', 'n_clicks'),
    Input('next', 'n_clicks'),
    State('location', 'hash')
)

app.layout = serve_layout
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
