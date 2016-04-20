#coding=utf8
from engine import *

#objects (name, description, on touch, on use)  
rose = MudObject('玫瑰', '火红色的玫瑰花，散发出迷乱人心的香味，花瓣上血迹斑斑让人有种错觉：她是由鲜血染红的', '小心！不过好像已经晚了，你的手指被玫瑰刺伤，你开始感觉天昏地暗', '似乎吃掉她是一个好方法，你慢慢品味着这只带血玫瑰，然后缓缓倒下，死去')  
shit = MudObject('shit', 'a stinky one', 'ewww...', 'you are sick, you know that?')  
gaidys = MudObject('鸟', '哈，这是一只傻鸟', '它看起来很不爽，估计随时都会揍你', '你是不是考虑拔掉它的毛，烤来吃？')  
rebit = MudObject('机器人','这是一个非常厉害的机器人，它有五条腿，没有脑袋','他像你发射了无敌飞蛋，你满脸蛋黄。','它带你飞上了宇宙，你缺氧死了')
  
#areas  
woods = MudArea('这里是范驭航的领域，鱼都在天上游着，看起来非常无厘头。有一位老者站在你的身边，默默的看着你，眼神很鄙视。')  
river = MudArea('shallow river')  
hills = MudArea('orc hills')  
house = MudArea('house of all gay')  
meadow = MudArea('a green smelly meadow')  
  
#attaching interactive stuff to areas  
river.add_object('object', shit)  
woods.add_object('机器人', rebit)
woods.add_object('玫瑰', rose)  
woods.add_object('鸟', gaidys)  
meadow.add_object('animal', gaidys)  
  
#link all areas with bidirectional references  
river.add_area('south', hills)  
woods.add_area('north', river)  
woods.add_area('west', house)  
hills.add_area('east', meadow)  
meadow.add_area('north', woods)  
  
#create a player  
char = MudPlayer('大地呆瓜')  
  
#create a game with player and starting area  
game = MudGame(char, woods)  
  
#lets go!  
game.run()
