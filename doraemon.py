import turtle


def flyTo(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()


def drawEye():
	turtle.tracer(False)
	a = 2.5
	for i in range(120):
		if 0 <= i < 30 or 60 <= i < 90:
			a -= 0.05
		else:
			a += 0.05
		turtle.left(3)
		turtle.fd(a)
	turtle.tracer(True)


def beard():
	""" 画胡子， 一共六根
	"""
	# 左边第一根胡子
	flyTo(-37, 135)
	turtle.seth(165)
	turtle.fd(60)

	# 左边第二根胡子
	flyTo(-37, 125)
	turtle.seth(180)
	turtle.fd(60)

	# 左边第三根胡子
	flyTo(-37, 115)
	turtle.seth(193)
	turtle.fd(60)

	# 右边第一根胡子
	flyTo(37, 135)
	turtle.seth(15)
	turtle.fd(60)

	# 右边第二根胡子
	flyTo(37, 125)
	turtle.seth(0)
	turtle.fd(60)

	# 右边第三根胡子
	flyTo(37, 115)
	turtle.seth(-13)
	turtle.fd(60)


def drawRedScarf():
	""" 画围巾
	"""
	turtle.fillcolor("red")  # 填充颜色
	turtle.begin_fill()
	turtle.seth(0)  # 朝向右

	turtle.fd(200)  # 前进10个单位
	turtle.circle(-5, 90)

	turtle.fd(10)
	turtle.circle(-5, 90)

	turtle.fd(207)
	turtle.circle(-5, 90)

	turtle.fd(10)
	turtle.circle(-5, 90)

	turtle.end_fill()


def drawMouse():
	flyTo(5, 148)
	turtle.seth(270)
	turtle.fd(100)
	turtle.seth(0)
	turtle.circle(120, 50)
	turtle.seth(230)
	turtle.circle(-120, 100)


def drawRedNose():
	flyTo(-10, 158)
	turtle.fillcolor("red")  # 填充颜色
	turtle.begin_fill()
	turtle.circle(20)
	turtle.end_fill()


def drawBlackdrawEye():
	turtle.seth(0)
	flyTo(-20, 195)
	turtle.fillcolor("#000000")  # 填充颜色
	turtle.begin_fill()
	turtle.circle(13)
	turtle.end_fill()
	turtle.pensize(6)
	flyTo(20, 205)
	turtle.seth(75)
	turtle.circle(-10, 150)
	turtle.pensize(3)
	flyTo(-17, 200)
	turtle.seth(0)
	turtle.fillcolor("#ffffff")
	turtle.begin_fill()
	turtle.circle(5)
	turtle.end_fill()
	flyTo(0, 0)


def drawFace():
	"""
	"""
	turtle.forward(183)  # 前行183个单位
	turtle.fillcolor("white")  # 填充颜色为白色
	turtle.begin_fill()  # 开始填充
	turtle.left(45)  # 左转45度
	turtle.circle(120, 100)  # 右边那半边脸
	turtle.seth(90)  # 朝向向上
	drawEye()  # 画右眼睛
	turtle.seth(180)  # 朝向左
	turtle.penup()  # 抬笔
	turtle.fd(60)  # 前行60
	turtle.pendown()  # 落笔
	turtle.seth(90)  # 朝向上
	drawEye()  # 画左眼睛
	turtle.penup()  # 抬笔
	turtle.seth(180)  # 朝向左
	turtle.fd(64)  # 前进64
	turtle.pendown()  # 落笔
	turtle.seth(215)  # 修改朝向
	turtle.circle(120, 100)  # 左边那半边脸
	turtle.end_fill()  #


def drawHead():
	""" 画了一个被切掉下半部分的圆
	"""
	turtle.penup()  # 抬笔
	turtle.circle(150, 40)  # 画圆, 半径150，圆周角40
	turtle.pendown()  # 落笔
	turtle.fillcolor("#00a0de")  # 填充色
	turtle.begin_fill()  # 开始填充
	turtle.circle(150, 280)  # 画圆，半径150, 圆周角280
	turtle.end_fill()


def drawAll():
	drawHead()
	drawRedScarf()
	drawFace()
	drawRedNose()
	drawMouse()
	beard()
	flyTo(0, 0)
	turtle.seth(0)
	turtle.penup()
	turtle.circle(150, 50)
	turtle.pendown()
	turtle.seth(30)
	turtle.fd(40)
	turtle.seth(70)
	turtle.circle(-30, 270)
	turtle.fillcolor("#00a0de")
	turtle.begin_fill()
	turtle.seth(230)
	turtle.fd(80)
	turtle.seth(90)
	turtle.circle(1000, 1)
	turtle.seth(-89)
	turtle.circle(-1000, 10)
	turtle.seth(180)
	turtle.fd(70)
	turtle.seth(90)
	turtle.circle(30, 180)
	turtle.seth(180)
	turtle.fd(70)
	turtle.seth(100)
	turtle.circle(-1000, 9)
	turtle.seth(-86)
	turtle.circle(1000, 2)
	turtle.seth(230)
	turtle.fd(40)
	turtle.circle(-30, 230)
	turtle.seth(45)
	turtle.fd(81)
	turtle.seth(0)
	turtle.fd(203)
	turtle.circle(5, 90)
	turtle.fd(10)
	turtle.circle(5, 90)
	turtle.fd(7)
	turtle.seth(40)
	turtle.circle(150, 10)
	turtle.seth(30)
	turtle.fd(40)
	turtle.end_fill()

	# 左手
	turtle.seth(70)
	turtle.fillcolor("#FFFFFF")
	turtle.begin_fill()
	turtle.circle(-30)
	turtle.end_fill()

	# 脚
	flyTo(103.74, -182.59)
	turtle.seth(0)
	turtle.fillcolor("#FFFFFF")
	turtle.begin_fill()
	turtle.fd(15)
	turtle.circle(-15, 180)
	turtle.fd(90)
	turtle.circle(-15, 180)
	turtle.fd(10)
	turtle.end_fill()
	flyTo(-96.26, -182.59)
	turtle.seth(180)
	turtle.fillcolor("#FFFFFF")
	turtle.begin_fill()
	turtle.fd(15)
	turtle.circle(15, 180)
	turtle.fd(90)
	turtle.circle(15, 180)
	turtle.fd(10)
	turtle.end_fill()

	# 右手
	flyTo(-133.97, -91.81)
	turtle.seth(50)
	turtle.fillcolor("#FFFFFF")
	turtle.begin_fill()
	turtle.circle(30)
	turtle.end_fill()

	# 口袋
	flyTo(-103.42, 15.09)
	turtle.seth(0)
	turtle.fd(38)
	turtle.seth(230)
	turtle.begin_fill()
	turtle.circle(90, 260)
	turtle.end_fill()
	flyTo(5, -40)
	turtle.seth(0)
	turtle.fd(70)
	turtle.seth(-90)
	turtle.circle(-70, 180)
	turtle.seth(0)
	turtle.fd(70)

	# 铃铛
	flyTo(-103.42, 15.09)
	turtle.fd(90)
	turtle.seth(70)
	turtle.fillcolor("#ffd200")
	turtle.begin_fill()
	turtle.circle(-20)
	turtle.end_fill()
	turtle.seth(170)
	turtle.fillcolor("#ffd200")
	turtle.begin_fill()
	turtle.circle(-2, 180)
	turtle.seth(10)
	turtle.circle(-100, 22)
	turtle.circle(-2, 180)
	turtle.seth(180 - 10)
	turtle.circle(100, 22)
	turtle.end_fill()
	flyTo(-13.42, 15.09)
	turtle.seth(250)
	turtle.circle(20, 110)
	turtle.seth(90)
	turtle.fd(15)
	turtle.dot(10)
	flyTo(0, -150)
	drawBlackdrawEye()


def main():
	turtle.screensize(800, 6000, "#F0F0F0")
	turtle.pensize(3)
	turtle.speed(9)
	drawAll()


if __name__ == "__main__":
	main()
	turtle.mainloop()
