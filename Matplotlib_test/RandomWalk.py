from random import choice

class RandomWalk1():
     def __init__(self,num_points=500):
         """初始化随机漫步属性"""
         self.num_points=num_points

         """起始坐标"""
         self.x_values=[0]
         self.y_values=[0]
     def fill_walk(self):
         """计算机漫步包含所有的点"""
         #不断漫步，直到列表达到指定的长度
         while len(self.x_values)<self.num_points:
             x_dir=choice([1,-1])
             x_dis=choice([0,1,2,3,4,5])
             x_step=x_dir*x_dis
             y_dir=choice([1,-1])
             y_dis=choice([0,1,2,3,4,5])
             y_step=y_dir*y_dis
             #拒绝原地踏步
             if x_step==0 and y_step==0:
                 continue
             #计算下一个点的x和y值,-1是倒数第一个元素
             next_x=self.x_values[-1]+x_step
             next_y=self.y_values[-1]+y_step

             self.y_values.append(next_y)
             self.x_values.append(next_x)





