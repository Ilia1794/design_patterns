from time import time
import plotly.graph_objects as go 
# TODO: Прикрутить ползунки для варьирования r, x_0, n в func_2

def func(x_0):
	x=x_0
	i=0
	while x != 1:
		print(f"{i}) {x=}")
		if x%2==0:
			x//=2
		else:
			x=3*x+1
		i+=1


def func_2(r, x_0, n):
	ret = []
	for i in range(n):
		ret.append(x_0)
		x_0 = r*x_0*(1-x_0)
	return ret


def plot(x, n):
	fig = go.Figure(data=go.Scatter(x=n, y=x, mode="markers"))#+lines
	return fig


if __name__ == "__main__":

	# func(int(time()*1000000))
	# print(f"{int(time())=}")
	n = 10000
	x = func_2(r=3.82, x_0=0.5, n=n)
	plot(x[1000:], list(range(n))[1000:]).show()#to_html("test.html")
