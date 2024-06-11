import numpy as np
import matplotlib.pyplot as plt
import  matplotlib


# 设置全局字体为serif风格，这通常接近于ACM推荐的Times New Roman
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman']  # 指定serif字体族的具体字体
matplotlib.rcParams['font.size'] = 10  # 可以根据需要调整全局字体大小
# 扩展示例数据以包括五个类别
categories = ['32', '64', '128', '256', '512']
group1 = [8.35,5.05,3.4,2.575,2.1625]


group2 = [8.41,5.02, 3.38, 2.7 ,2.21]
group3 = [8.34,5.04,3.37,2.61,2.18]
group4 = [8.36,5.12,3.41,2.55,2.16]

# 调整柱子宽度
barWidth = 0.15
space_width = 0.03
# 设置每个柱子的位置
r1 = np.arange(len(group1))
r2 = [x + barWidth + space_width for x in r1]
r3 = [x + barWidth * 2 + space_width*2 for x in r1]
r4 = [x + barWidth * 3 + + space_width*3 for x in r1]

# 创建图表，调整尺寸使图表更小
plt.figure(figsize=(5, 3))

# 绘制柱状图
plt.bar(r1, group1, color='#4472c4', width=barWidth, edgecolor='grey', label='Predict Data')
plt.bar(r2, group2, color='#ed7d31', width=barWidth, edgecolor='grey', label='Real Data1')
plt.bar(r3, group3, color='#a5a5a5', width=barWidth, edgecolor='grey', label='Real Data2')
plt.bar(r4, group4, color='#ffc000', width=barWidth, edgecolor='grey', label='Real Data3')

# 添加标签和标题
plt.xlabel('OCC_INTERVAL', fontweight='bold', fontsize=10)  # 稍微调整字体大小以适应更小的图表
plt.xticks([r + barWidth * 1.5 for r in range(len(group1))], categories, fontsize=10)  # 调整刻度标签的字体大小
plt.ylabel('ALN_MEM(GB)', fontweight='bold', fontsize=10)
#plt.title('Comparison Bar Chart with Five Categories', fontsize=12)

# 创建图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.savefig('comparison_bar_chart_five_categories_smaller.png', dpi=300) # 保存图表为图片，高分辨率
plt.show()
