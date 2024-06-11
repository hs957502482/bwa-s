import matplotlib.pyplot as plt
import  matplotlib
import numpy as np
plt.rcParams.update({'legend.fontsize': 20})
# 设置全局字体为serif风格，这通常接近于ACM推荐的Times New Roman
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman']  # 指定serif字体族的具体字体
matplotlib.rcParams['font.size'] = 20  # 可以根据需要调整全局字体大小
# 扩展示例数据以包括五个类别
categories = ['0.5M', '0.6M', '0.7M', '0.8M', '0.9M']
group1 = [13.351,13.484,13.902,14.440,14.762 ] #srr20833263   samse2
group3 = [13.429 ,13.529,13.693,13.835,14.028 ]#srr20833263   samse3

group2 = [13.399,13.736, 14.445, 14.614,14.960]#srr20833262   samse2

group4 = [13.891,14.195,14.244,14.433,14.758]#srr20833262   samse3

# 将分类转换为x轴上的位置
x = np.arange(len(categories))

plt.figure(figsize=(10, 6))

# 绘制折线图，为每个组使用不同的颜色和标记
plt.plot(x, group2, marker='o', linestyle='-', color='#4472c4', label='Single thread running time of SRR20833262')
plt.plot(x, group4, marker='s', linestyle='-', color='#ed7d31', label='Four threads running time of SRR20833262')
#plt.plot(x, group3, marker='^', linestyle='-', color='#70ad47', label='Measured for SRR13371062')
#plt.plot(x, group4, marker='d', linestyle='-', color='#ffc000', label='Measured for SRR19540612')

# 添加标签和标题
plt.xticks(x, categories)
plt.xlabel('Reads Number', fontweight='bold', fontsize=25)
plt.ylabel('Time (s)', fontweight='bold', fontsize=25)
#plt.title('Comparison Line Chart with Five Categories', fontsize=14)

# 显示网格线以提高可读性
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 创建图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.savefig('srr20833262ps.pdf', dpi=300) # 保存图表为图片，高分辨率
plt.show()
