##пример pyplot построение простого графика
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.ylabel('some numbers')
# plt.show()
#

##применение RGB формата при работе с цветом
# import matplotlib.lines
# import matplotlib.patches
# import matplotlib.path
# import matplotlib.pyplot as plt

# def drawRect(color):
#     plt.xlim(-5, 2)
#     plt.ylim(-4, 2)
#     plt.grid()
#     axes = plt.gca()
#     axes.set_aspect("equal")
#     rect_back = matplotlib.patches.Rectangle((-1.0, -1.0), 2, 2, color='y')
#     rect_front = matplotlib.patches.Rectangle((-3.5, -3.7), 3, 3, color=color)
#     axes.add_patch(rect_back)
#     axes.add_patch(rect_front)
#     plt.title('color = {}'.format(color))
#     plt.show()
#
# if __name__ == "__main__":
#     color = '#AA00AA'
#     drawRect(color)

##демонстрация создания палитры SEABORN  распределением цвета
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# palette = sns.color_palette('Reds', 5)
# sns.palplot(palette)
#
# plt.show()

## демонстрация создания палитры со определенным набором цветов
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# color = ["Red", "Yellow", "Green", "Blue"]
# sns.set_palette(color)
# sns.palplot(sns.color_palette())
# plt.show()

##использование данных CVS файлов библиотеки. построение barplot
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# df = sns.load_dataset('penguins')
# color = ["Green"]
# sns.set_palette(color)
#
# sns.barplot(x='species',
# 			y='body_mass_g',
# 			data=df)
#
# plt.show()

##построение гистограммы с помощью histplot
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# data = sns.load_dataset("penguins")
# sns.histplot(x='species', y='island', data=data)
# plt.show()


##линейная прогрессия с помощью Rеgplot
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# data = sns.load_dataset("penguins")
# sns.regplot(x='bill_length_mm', y='body_mass_g', data=data)
# plt.show()

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import plotly.express as px


##столбчатая диаграмма с помощью plotly
# df = px.data.tips()
# fig = px.bar(df, x='day', y="total_bill")
#
# fig.show()
#
##построение круговой диграммы plotly
# df = px.data.tips()
# fig = px.pie(df, values="total_bill", names="day",
# 			color_discrete_sequence=px.colors.sequential.RdBu,
# 			opacity=0.7, hole=0.5)
# fig.show()


