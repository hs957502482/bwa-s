
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
group1 = [9.07,7.42,5.77,4.945,4.5325]


group2 = [9.03,7.45, 5.79, 4.93 ,4.61]
group3 = [9.11,7.34,5.88,4.88,4.56]
group4 = [9.10,7.38,5.73,4.94,4.49]



# 将分类转换为x轴上的位置
x = np.arange(len(categories))

plt.figure(figsize=(10, 6))

# 绘制折线图，为每个组使用不同的颜色和标记
plt.plot(x, group1, marker='o', linestyle='-', color='#4472c4', label='Predicted by Model')
plt.plot(x, group2, marker='s', linestyle='-', color='#ed7d31', label='Measured for SRR13313285')
plt.plot(x, group3, marker='^', linestyle='-', color='#70ad47', label='Measured for SRR13371062')
plt.plot(x, group4, marker='d', linestyle='-', color='#ffc000', label='Measured for SRR19540612')

# 添加标签和标题
plt.xticks(x, categories)
plt.xlabel('SA_INTV', fontweight='bold', fontsize=25)
plt.ylabel('BWA-MEM_Memory (GB)', fontweight='bold', fontsize=25)
#plt.title('Comparison Line Chart with Five Categories', fontsize=14)

# 显示网格线以提高可读性
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 创建图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.savefig('sa_mem.pdf', dpi=300) # 保存图表为图片，高分辨率
plt.show()
