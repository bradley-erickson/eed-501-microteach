# package imports
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
                    'reason to loop'
                ],
                body=True,
                class_name='text-center'
            ),
            md=4,
            xl=3
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
            md=4,
            xl=3
        )
    ],
    id='overview',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)


loops = {
    'while': {
        'code': 'int i = 0;\nwhile (i < 5) {\n\trepeatedCode();\n\ti++;\n}',
        'name': 'While',
        'use-cases': ''
    },
    'for': {
        'code': 'for (int i = 0; i < 5; i++) {\n\trepeatedCode();\n}',
        'name': 'For',
        'use-cases': ''
    },
    'do-while': {
        'code': 'int i = 0;\ndo {\n\trepeatedCode();\n\ti++;\n} while (i < 5);',
        'name': 'Do While',
        'use-cases': ''
    }
}

def create_loop_card(loop):
    l = loops[loop]
    card = dbc.Col(
        [
            dbc.Card(
                [
                    html.H3(l['name'], className='text-center'),
                    dcc.Markdown(f'```java\n{l["code"]}\n```'),
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
    id='types',
    justify='center',
    align='center',
    class_name='h-100 w-100'
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
            dcc.Location(id='location', hash='home'),
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
