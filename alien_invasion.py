import sys
import pygame

'''
首先， 我们导入了模块sys 和pygame 。 模块pygame 包含开发游戏所需的功能。 玩家退出时， 我们将使用模块sys 来退出游戏。
游戏《外星人入侵》 的开头是函数run_game() 。 ❶处的代码行pygame.init() 初始化背景设置， 让Pygame能够正确地工作。 在❷处， 我们调
用pygame.display.set_mode() 来创建一个名为screen 的显示窗口， 这个游戏的所有图形元素都将在其中绘制。 实参(1200, 800) 是一个元组， 指定了游戏窗口的尺
寸。 通过将这些尺寸值传递给pygame.display.set_mode() ， 我们创建了一个宽1200像素、 高800像素的游戏窗口（你可以根据自己的显示器尺寸调整这些值） 。
对象screen 是一个surface。 在Pygame中， surface是屏幕的一部分， 用于显示游戏元素。 在这个游戏中， 每个元素（如外星人或飞船） 都是一个surface。 display.set_mode()
返回的surface表示整个游戏窗口。 我们激活游戏的动画循环后， 每经过一次循环都将自动重绘这个surface。
这个游戏由一个while 循环（见❸） 控制， 其中包含一个事件循环以及管理屏幕更新的代码。 事件是用户玩游戏时执行的操作， 如按键或移动鼠标。 为让程序响应事件， 我们编
写一个事件循环， 以侦听事件， 并根据发生的事件执行相应的任务。 ❹处的for 循环就是一个事件循环。
为访问Pygame检测到的事件， 我们使用方法pygame.event.get() 。 所有键盘和鼠标事件都将促使for 循环运行。 在这个循环中， 我们将编写一系列的if 语句来检测并响应
特定的事件。 例如， 玩家单击游戏窗口的关闭按钮时， 将检测到pygame.QUIT 事件， 而我们调用sys.exit() 来退出游戏（见❺） 。
❻处调用了pygame.display.flip() ， 命令Pygame让最近绘制的屏幕可见。 在这里， 它在每次执行while 循环时都绘制一个空屏幕， 并擦去旧屏幕， 使得只有新屏幕可
见。 在我们移动游戏元素时， pygame.display.flip() 将不断更新屏幕， 以显示元素的新位置， 并在原来的位置隐藏元素， 从而营造平滑移动的效果。
在这个基本的游戏结构中， 最后一行调用run_game() ， 这将初始化游戏并开始主循环。
如果此时运行这些代码， 你将看到一个空的Pygame窗口。
'''
def  run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()