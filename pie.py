import plotly.plotly as py
import plotly.graph_objs as go

labels = ['CNC', 'SLM', 'SLA', 'SLS', 'FDM']
values = [2000, 1500, 678, 1789, 2555]

fig = {
    "data": [
        {
            "values": values,
            "labels": labels,
            "type": "pie"
        }
    ],
    "layout": {
        "title": "makerOS Types of Fabrication",
    }
}

py.iplot(fig, filename='makerOS_types_of_fabrication_pie')
