import matplotlib.pyplot as plt
import  matplotlib
import numpy as np
import matplotlib.ticker as ticker
plt.rcParams.update({'legend.fontsize': 25})
# 设置全局字体为serif风格，这通常接近于ACM推荐的Times New Roman
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman']  # 指定serif字体族的具体字体
matplotlib.rcParams['font.size'] = 20  # 可以根据需要调整全局字体大小
# 扩展示例数据以包括五个类别
categories = ['1M', '2M','3M' ,'5M','7M', '10M']
#categories = ['4', '8', '16', '32', '64']

group1 = [16,16,16,8,8,8 ] #不加内存约束预测的sa值  3m:3.65    7m3.04

group3= [16,16,16,8,4,4 ]#真实的sa


# group1 = [50.947,48.205,49.172,75.020,110.071 ] #1kw
# group3 = [31.933 ,30.004,31.888,40.729,57.222 ]#500w
#
# group2 = [21.077,19.319, 16.481, 19.414,25.929]#200w
#
# group4 = [18.870 ,15.648,12.610,13.244,15.897]#100w
# 将分类转换为x轴上的位置
x = np.arange(len(categories))

plt.figure(figsize=(10, 6))

# 绘制折线图，为每个组使用不同的颜色和标记
plt.plot(x, group1, marker='o', linestyle='-', color='#4472c4', label='Predicted SA_INTV')
plt.plot(x, group3, marker='^', linestyle='-', color='#70ad47', label='Real SA_INTV')
#plt.plot(x, group4, marker='d', linestyle='-', color='#ffc000', label='Running time of SRR10067255_1M')




# 添加标签和标题
plt.xticks(x, categories)
plt.xlabel('Reads Number', fontweight='bold', fontsize=25)
plt.ylabel('SA_INTV', fontweight='bold', fontsize=25)
#plt.title('Comparison Line Chart with Five Categories', fontsize=14)

# 显示网格线以提高可读性
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 创建图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.savefig('read_sa1.pdf', dpi=300) # 保存图表为图片，高分辨率
plt.show()
