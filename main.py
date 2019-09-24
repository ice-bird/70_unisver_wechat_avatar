# -*- coding: utf8 -*-
#%%
from PIL import Image
import matplotlib.pyplot as plt

# 读取头像和国旗图案
img_head = Image.open('image/test.jpg')
img_flag = Image.open('source/source.png') #RGBA打开
#%%
# 获取头像和国旗图案宽度
w_head, h_head = img_head.size[:2]  #959
w_flag, h_flag = img_flag.size[:2]  #2194*2194

#抠图参数95/2098
# if w_flag!=w_head:
#     x
# # 计算图案缩放比例

# 缩放图案
final_size=min(w_head,w_flag)
img_flag=img_flag.resize((final_size,final_size),Image.ANTIALIAS)
img_head= img_head.convert('RGBA') #格式一致

final_img = Image.alpha_composite(img_head, img_flag) #按透明度重叠图像
# 保存最终结果
final_img.save('res/new_head.png')
plt.imshow(final_img)
plt.show()