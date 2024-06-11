
import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([32, 64, 128, 256, 512])


import matplotlib.pyplot as plt
import  matplotlib
import numpy as np
plt.rcParams.update({'legend.fontsize': 25})

# 设置全局字体为serif风格，这通常接近于ACM推荐的Times New Roman
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman']  # 指定serif字体族的具体字体
matplotlib.rcParams['font.size'] = 20  # 可以根据需要调整全局字体大小
# 扩展示例数据以包括五个类别
categories = ['8', '16', '32', '64', '128']
group1 = [477.5288,
355.8288,
294.9788,
264.5538,
234.1318
]


group2 = [473.24,351.33, 292.39, 263.52 ,230.13]

group3 = [502.5288,
380.8288,
319.9788,
289.5538,
259.1318
]

group4 = [501.38,377.28,314.31, 282.27 ,267.31]

# 将分类转换为x轴上的位置
x = np.arange(len(categories))

plt.figure(figsize=(10, 6))

# 绘制折线图，为每个组使用不同的颜色和标记
plt.plot(x, group1, marker='o', linestyle='-', color='#4472c4', label='Predicted by Model for 50bp')
plt.plot(x, group2, marker='s', linestyle='-', color='#ed7d31', label='Measured for DRR331873')

plt.plot(x, group3, marker='d', linestyle='-', color='#ffc000', label='Predicted by Model for 75bp')
plt.plot(x, group4, marker='^', linestyle='-', color='#70ad47', label='Measured for SRR28738909')
# 添加标签和标题
plt.xticks(x, categories)
plt.xlabel('SA_INTV', fontweight='bold', fontsize=25)
plt.ylabel('SAMSE_Memory (MB)', fontweight='bold', fontsize=25)
#plt.title('Comparison Line Chart with Five Categories', fontsize=14)

# 显示网格线以提高可读性
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 创建图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.savefig('sa_samse.pdf', dpi=300) # 保存图表为图片，高分辨率
plt.show()

