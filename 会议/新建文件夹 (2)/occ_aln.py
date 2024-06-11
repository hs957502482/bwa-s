import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family'] = 'Arial'
# 假设的数据
# data = np.array([
#     [213.406, 95.826, 199.927, 180.361],
#     [576.396, 311.338, 441.77, 400.941],
#     [788.543, 307.894,471.529, 436.677]
# ])
data = np.array([
    [213.406,576.396,788.543],[ 95.826,311.338,307.894],[199.927,441.77,471.529],[180.361, 400.941,436.677]
])

x = np.arange(3)  # 柱状图的x轴位置
width = 0.15  # 柱状图的宽度


fig, ax = plt.subplots()
rects1 = ax.bar(x - width, data[0], width,hatch='xx' ,color='0.8',edgecolor = 'k', label='BWA*1',align='center')
rects2 = ax.bar(x, data[1], width, hatch='+' ,color='0.8',edgecolor = 'k', label='BWA*2', align='center')
rects3 = ax.bar(x + width, data[2], width, hatch='o' ,color='0.8',edgecolor = 'k', label='BWA-MEM1', align='center')
rects4 = ax.bar(x + 2*width, data[3], width,hatch='*' ,color='0.8',edgecolor = 'k', label='BWA-MEM2', align='center')

# 添加一些标签，标题和自定义x轴标签
ax.set_xlabel('strategy')
ax.set_ylabel('time(s)')
# ax.set_title()
ax.set_xticks(x)
ax.set_xticklabels(['ERR9616591', 'ERR5693770', 'ERR7720072'])
ax.legend()

# 添加文字标签
def autolabel(rects):
    """在每个柱上方附加一个文本标签显示高度."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3点垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
plt.savefig('TIME11.png')
plt.show()
