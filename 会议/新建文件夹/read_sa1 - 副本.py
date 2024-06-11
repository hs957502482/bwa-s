import matplotlib.pyplot as plt
import  matplotlib
import numpy as np
import matplotlib.ticker as ticker
plt.rcParams.update({'legend.fontsize': 19})
# 设置全局字体为serif风格，这通常接近于ACM推荐的Times New Roman
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman']  # 指定serif字体族的具体字体
matplotlib.rcParams['font.size'] = 20  # 可以根据需要调整全局字体大小
# 扩展示例数据以包括五个类别
categories = ['4', '8', '16', '32','64']
#categories = ['4', '8', '16', '32', '64']




group1 = [46.947,48.205,49.172,75.020,110.071 ] #1kw
group2 = [30.933 ,30.004,31.888,40.729,57.222 ]#500w

group3 = [21.077,19.319, 16.481, 19.414,25.929]#200w

group4 = [18.870 ,15.648,12.610,13.244,15.897]#100w

group5= [23.162,22.945,20.270,27.860,40.475 ] #300w
group6=[31.648 ,32.839 ,36.432,57.273,84.438] #700w
# 将分类转换为x轴上的位置
x = np.arange(len(categories))

plt.figure(figsize=(10, 6))

# 绘制折线图，为每个组使用不同的颜色和标记
plt.plot(x, group1, marker='o', linestyle='-', color='#4472c4', label='Running time of SRR10067255_10M')
plt.plot(x, group6, marker='v', linestyle='-', color='#9467bd', label='Running time of SRR10067255_7M')
plt.plot(x, group2, marker='s', linestyle='-', color='#ed7d31', label='Running time of SRR10067255_5M')
plt.plot(x, group5, marker='p', linestyle='-', color='#d62728', label='Running time of SRR10067255_3M')
plt.plot(x, group3, marker='^', linestyle='-', color='#70ad47', label='Running time of SRR10067255_2M')
plt.plot(x, group4, marker='d', linestyle='-', color='#ffc000', label='Running time of SRR10067255_1M')





# 添加标签和标题
plt.xticks(x, categories)
plt.xlabel('SA_INTV', fontweight='bold', fontsize=25)
plt.ylabel('Time (s)', fontweight='bold', fontsize=25)
#plt.title('Comparison Line Chart with Five Categories', fontsize=14)

# 显示网格线以提高可读性
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 创建图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.savefig('GUAIDIAN.pdf', dpi=300) # 保存图表为图片，高分辨率
plt.show()
