import requests
from plotly.graph_objs import Bar
from plotly import offline

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
submission_ids = r.json()

links, comments = [], []

for submission_id in submission_ids:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        response_dict = r.json()
        title = response_dict["title"]
        url = f"http://news.ycombinator.com/item?id={submission_id}"
        link = f"<a href='{url}'>{title}</a>"
        links.append(link)
        comment = response_dict["descendants"]
        comments.append(comment)
    except KeyError:
        continue

data = [{
    "type": "bar",
    "x": links,
    "y": comments,
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {
            "width": 1.5,
            "color": "rgb(25,25,25)"
        }
    },
    "opacity": 0.6
}]

my_layout = {
    "title": "Most Active Hacker News Discussions",
    "titlefont": {
        "size": 28
    },
    "xaxis": {
        "title": "Article",
        "titlefont": {
            "size": 28
        },
        "tickfont": {
            "size": 14
        }
    },
    "yaxis": {
        "title": "Comments",
        "titlefont": {
            "size": 28
        },
        "tickfont": {
            "size": 14
        }
    }
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="active_discussions.html")