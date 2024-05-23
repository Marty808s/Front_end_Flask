import plotly.graph_objects as go

def test():
    fig = go.Figure(data=[go.Bar(x=['Category 1', 'Category 2', 'Category 3'], y=[10, 20, 30])])
    fig.update_layout(title='Graf, který Vám ic neřekne ale funguje to')
    return fig

def scatter_plot():
    fig = go.Figure(data=[go.Scatter(x=['Category 1', 'Category 2', 'Category 3'], y=[10, 20, 30], mode='markers')])
    fig.update_layout(title='Bodový graf')
    return fig

def area_chart():
    fig = go.Figure(data=[go.Scatter(x=['Category 1', 'Category 2', 'Category 3'], y=[10, 20, 30], fill='tozeroy')])
    fig.update_layout(title='Plošný graf')
    return fig

def pie_chart():
    fig = go.Figure(data=[go.Pie(labels=['Category 1', 'Category 2', 'Category 3'], values=[10, 20, 30])])
    fig.update_layout(title='Koláčový graf')
    return fig