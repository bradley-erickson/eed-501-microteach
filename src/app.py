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

outro = dbc.Row(
    dbc.Card(
        html.H2('Questions'),
        class_name='border-0 text-center'
    ),
    id='end',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)

overview = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H3('Purpose'),
                    'Repeat some ',
                    html.Div('code', className='d-inline-block bg-info p-1 text-white border border-dark mb-1'),
                    ' whenever a ',
                    html.Div('condition', className='d-inline-block bg-primary border rounded-opposites p-1 text-white border-dark'),
                    ' is true.'
                ],
                body=True,
                class_name='mb-4'
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

types_header = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H3('Types'),
                    html.Ul(
                        [
                            html.Li('While'),
                            html.Li('For')
                        ]
                    )
                ],
                body=True
            ),
            md=4,
            xl=3
        )
    ],
    id='types',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)

activity_1 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H3('Activity'),
                    'Think about a use case when you might want to repeat something'
                ],
                body=True,
            ),
            md=4,
            xl=3
        )
    ],
    id='activity-1',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)

activity_2 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H3('Activity'),
                    'Which type of loop does your use case use?'
                ],
                body=True,
            ),
            md=4,
            xl=3
        )
    ],
    id='activity-2',
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
            'Parsing user input'
        ],
        'special-versions': html.Div(
            [
                html.H4('Do while'),
                'Runs the code first, then checks the condition [1, ∞)'
            ],
            className='mb-3'
        )
    },
    'for': {
        'code': 'for (int i = 0; i < 5; i++) {\n\trepeatedCode();\n}',
        'name': 'For',
        'purpose': 'Run code a set number of times [0, X]',
        'use-cases': [
            'Iterating over items in a list',
            'Counting to a specific number'
        ],
        'special-versions': html.Div(
            [
                html.H4('For Each'),
                'Provides easy access to each item in a variable'
            ],
            className='mb-3'
        )
    }
}


def create_loop_card(loop):
    l = loops[loop]
    card = dbc.Col(
        [
            dbc.Card(
                [
                    html.H3(l['name']),
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
                                    html.Div(html.Small('Java code'), className='text-end'),
                                    dcc.Markdown(f'```java\n{l["code"]}\n```'),
                                    l['special-versions'],
                                    html.H4('Use Cases:'),
                                    html.Ul([html.Li(u) for u in l['use-cases']]) if type(l['use-cases']) == list else html.P(l['use-cases']),
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


types_of_loops = ['while', 'for']
tol_cards = [
    dbc.Row(
        create_loop_card(loop),
        id=loop,
        justify='center',
        align='center',
        class_name='h-100 w-100'
    ) for loop in types_of_loops
]
tol_cards.insert(0, types_header)
tol_cards.insert(
    0,
    dbc.Row(
        dbc.Card(
            html.H2('Types of loops'),
            class_name='border-0 text-center'
        ),
        id='section-2',
        justify='center',
        align='center',
        class_name='h-100 w-100'
    )
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

table_of_contents = dbc.ButtonGroup(
    [
        dbc.Button(html.I(id='toc-home-icon'), id='toc-home', color='secondary'),
        dbc.Button(html.I(id='toc-what-is-icon'), id='toc-what-is', color='secondary'),
        dbc.Button(html.I(id='toc-types-icon'), id='toc-types', color='secondary'),
        dbc.Button(html.I(id='toc-examples-icon'), id='toc-examples', color='secondary'),
        dbc.Button(html.I(id='toc-end-icon'), id='toc-end', color='secondary'),
    ],
    size='sm',
    class_name='position-fixed top-0 ms-2 mt-2'
)

what_is_contents = [
    dbc.Row(
        dbc.Card(
            html.H2('What is a loop?'),
            class_name='border-0 text-center'
        ),
        id='section-1',
        justify='center',
        align='center',
        class_name='h-100 w-100'
    ),
    overview,
    activity_1
]


while_examples = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H3('While Examples'),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4('Connect to server'),
                                    html.P('Attempt to connect to a server until connected with 1 second intervals', className='mb-0'),
                                    html.Div(html.Small('Python code'), className='text-end'),
                                    dcc.Markdown(f'```python\nconnection = False\nwhile !connection:\n\tconnection = connect(credentials)\n\ttime.sleep(1)\n```')
                                ],
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.H4('Respond to input'),
                                    html.P('Read each character of user input, stop when a number is inputted', className='mb-0'),
                                    html.Div(html.Small('Java code'), className='text-end'),
                                    dcc.Markdown('```java\nScanner scan = new Scanner(System.in);\nChar input = "";\ndo {\n\tinput = scan.next();\n\ti++;\n} while (!Character.isDigit(input));\n```')
                                ],
                                md=6
                            )
                        ]
                    )
                ],
                body=True,
                class_name='mb-4'
            ),
            md=10,
            xl=8
        )
    ],
    id='while-examples',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)

for_examples = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    html.H3('For Examples'),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4('Adding numbers'),
                                    html.P('Iterate over a range of numbers and sum them', className='mb-0'),
                                    html.Div(html.Small('Python code'), className='text-end'),
                                    dcc.Markdown(f'```python\ntotal = 0\nfor i in range(5):\n\ttotal += i\n# total = 10\n```')
                                ],
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.H4('Iterate over list'),
                                    html.P('Reset the grade of each student in this class', className='mb-0'),
                                    html.Div(html.Small('Python code'), className='text-end'),
                                    dcc.Markdown('```python\nstudents = eed501.students\nfor student in students:\n\tstudent.grade = "A+"\n```')
                                ],
                                md=6
                            )
                        ]
                    )
                ],
                body=True,
                class_name='mb-4'
            ),
            md=10,
            xl=8
        )
    ],
    id='for-examples',
    justify='center',
    align='center',
    class_name='h-100 w-100'
)


example_contents = [
    dbc.Row(
        dbc.Card(
            html.H2('Examples'),
            class_name='border-0 text-center'
        ),
        id='section-3',
        justify='center',
        align='center',
        class_name='h-100 w-100'
    ),
    while_examples,
    for_examples,
    activity_2
]


def serve_layout():
    return dbc.Container(
        [
            dcc.Location(id='location'),
            dbc.Row(
                [
                    intro,
                    html.Div(what_is_contents),
                    html.Div(tol_cards),
                    html.Div(example_contents),
                    outro
                ],
                class_name='flex-nowrap',
                style={'height': '95vh'}
            ),
            next,
            prev,
            table_of_contents
        ],
        fluid=True,
    )


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='change_pages'),
    Output('location', 'hash'),
    Input('prev', 'n_clicks'),
    Input('next', 'n_clicks'),
    Input('toc-home', 'n_clicks'),
    Input('toc-what-is', 'n_clicks'),
    Input('toc-types', 'n_clicks'),
    Input('toc-examples', 'n_clicks'),
    Input('toc-end', 'n_clicks'),
    State('location', 'hash')
)


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='update_icons'),
    Output('toc-home-icon', 'className'),
    Output('toc-what-is-icon', 'className'),
    Output('toc-types-icon', 'className'),
    Output('toc-examples-icon', 'className'),
    Output('toc-end-icon', 'className'),
    Input('location', 'hash')
)

app.layout = serve_layout
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
