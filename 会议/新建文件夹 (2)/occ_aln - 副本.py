import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family'] = 'Arial'
# 假设的数据
# data = np.array([
#     [100, 98.74, 96, 95.98],
#     [99.9, 99.43, 97.35, 97.34],
#     [100, 98.83,97.47, 97.44]
# ])
data = np.array([
    [100,99.9,100],[98.74,99.43,98.83],[96,97.35,97.47],[95.98,97.34,97.44]
])


x = np.arange(3)  # 柱状图的x轴位置
width = 0.15  # 柱状图的宽度

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, data[0], width,hatch='xx' ,color='0.8',edgecolor = 'k', label='BWA*1',align='center')
rects2 = ax.bar(x, data[1], width, hatch='+' ,color='0.8',edgecolor = 'k', label='BWA*2', align='center')
rects3 = ax.bar(x + width, data[2], width, hatch='o' ,color='0.8',edgecolor = 'k', label='BWA-MEM1', align='center')
rects4 = ax.bar(x + 2*width, data[3], width,hatch='*' ,color='0.8',edgecolor = 'k', label='BWA-MEM2', align='center')


# 设置y轴范围以放大差异
min_val = np.min(data)
max_val = np.max(data)
ax.set_ylim(min_val - 0.2, max_val + 0.2)  # 调整此处以改变显示的范围

# 添加一些标签，标题和自定义x轴标签
ax.set_xlabel('strategy')
ax.set_ylabel('precision(%)')
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
legend = ax.legend(fontsize='10')
# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
plt.savefig('precision11.png')
plt.show()
