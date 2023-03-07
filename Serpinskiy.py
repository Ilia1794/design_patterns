import plotly.express as px
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
import time


def create_thriangle(coord_1: tuple, coord_2: tuple, coord_3: tuple, n: int):
    x = [np.random.randint(min(coord_3[0], coord_2[0], coord_1[0]), max(coord_3[0], coord_2[0], coord_1[0]))]
    y = [np.random.randint(min(coord_3[1], coord_2[1], coord_1[1]), max(coord_3[1], coord_2[1], coord_1[1]))]

    for i in range(n):
        create_step((coord_1,coord_2,coord_3), x, y)


    df = pd.DataFrame({
        "x":x,
        "y":y,
        "step":[_ for _ in range(len(x))]
        })

    return df

def create_step(coords: tuple, x: list, y: list):
    c = coords[np.random.randint(0,3)]
    new_coord(c, x, y)

def new_coord(coord: tuple, x: list, y: list):
    x.append((coord[0]+x[-1])/2)
    y.append((coord[1]+y[-1])/2)


# df = px.data.gapminder()
def plot(df):
    x = df["x"].values
    y = df["y"].values
    step = df["step"]
    fig = go.Figure(data=[
            go.Scatter(x=x, y=y, mode="markers",  marker=dict(size=1)) 
        ])#, 
        # frame=[
        #     go.Frame([go.Scatter(x=x[:_+1], y=y[:_+1], mode="markers")]) for _ in range(len(x)-1)
        # ])
    # fig = px.scatter(df, x="x", y="y", animation_frame="step") #,animation_group="country",
    # #size="pop", color="continent", hover_name="country",
    # # log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    fig.write_html("a.html")


if __name__ == "__main__":
    b = time.time()
    df = create_thriangle((0,0), np.random.randint(-10,10,2), np.random.randint(-7,18,2), 100000)
    print(f"time = {time.time()-b}")
    plot(df)