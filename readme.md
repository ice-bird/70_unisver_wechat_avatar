# 祖国70周年头像制作
## 原理：
图片框透明度设置为为0，将头像与框叠加alpha_composite

## 使用方法
将头像放入image\，命名为test.jpg(或修改代码)
```python
img_head = Image.open('image/test.jpg') #用户头像
```
运行main.py:
```python
python -u main.py
```

## 结果
![new](res\new_head.png)
![new2](res\new_head2.png)


## 改进
1.命令行式运行，读取不同路径图片
2.不同风格框图
3.拖动图片