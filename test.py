"""
 VPython教學: 4-1.自由落下
 日期: 2018/2/18
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
h = 15       # 小球離地高度
g = 9.8      # 重力加速度 9.8 m/s^2
t = 0        # 時間
dt = 0.01    # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title = "Free Fall", width = 600, height = 600, x = 0, y = 0, center = vector(0, h/2, 0), background = vector(0, 0.6, 0.6))
floor = box(pos = vector(0, 0, 0), length = 40, height = 0.01, width = 10, color = color.blue)
ball = sphere(pos = vector(0, h, 0), radius = size, color = color.red)
ball.v = vector(0, 0, 0)
ball.a = vector(0, -g, 0)

gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "blue: y(m), red: v(m/s)")
yt = gcurve(graph = gd, color = color.blue)
vt = gcurve(graph = gd, color = color.red)

"""
 3. 物體運動部分, 小球觸地時停止
"""
while(ball.pos.y > size):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    yt.plot(pos = (t, ball.pos.y))
    vt.plot(pos = (t, ball.v.y))
    t += dt

print("t = ", t)
