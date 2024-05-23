from flask import Flask, render_template
from graf import scatter_plot, area_chart, pie_chart, test

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/graf')
def graf():
    fig = test().to_html(full_html=False)
    fig_scatter = scatter_plot().to_html(full_html=False)
    fig_area = area_chart().to_html(full_html=False)
    fig_pie = pie_chart().to_html(full_html=False)
    return render_template('grafy.html', plot=fig, plot_scatter=fig_scatter, plot_area=fig_area, plot_pie=fig_pie)

if __name__ == '__main__':
    app.run(debug=True)