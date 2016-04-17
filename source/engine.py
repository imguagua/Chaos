#coding:utf8
class MudObject:
    def __init__(self, name, sight, collide = 'nothing happens',
                usability = 'unusable'):
        self.name = name
        self.sight = sight
        self.collide = collide
        self.usability = usability
    def view(self):
        return self.sight
    def touch(self):
        return self.collide
    def use(self):
        return self.usability


class MudPlayer:
    def __init__(self, name):
        self.inventory = {}
        self.name = name
        self.health = 100
    
    def move(self, area):
        return self.name + ' move to ' + area.sight

    def take(self, obj):
        self.inventory[obj.name] = obj
        return self.name + ' 拿起 ' + obj.name + ' 放入自己的背包'

    def drop(self, name):
        if self.inventory.has_key(name):
            return self.inventory.pop(name)

    def say(self, what):
        return self.name + ' says: ' + what

    def use(self, what):
        for i in self.inventory:
            print i
        if self.inventory.has_key(what):
            return self.inventory[what].use()
        else:
            return '你没有 ' + what


class MudArea:
    def __init__(self, sight):
        self.objects = {}
        self.panorama = {}
        self.sight = sight
        self.inverted_directions = {'north':'south', 'south':'north',
                                    'east':'west', 'west':'east'}

    def add_area(self, direction, area):
        area.panorama[self.inverted_directions[direction]] = self
        self.panorama[direction] = area

    def relocate(self, args):
        try:
            return self.panorama[args]
        except KeyError:
            return None

    def add_object(self, name, obj):
        if obj != None:
                self.objects[name] = obj
        return name + '被丢弃 ..'

    def get_object(self, name):
        if self.objects.has_key(name):
            return self.objects.pop(name)
        else:
            return 'there is no ' + name + ' arround!'

    def touch_object(self ,name):
        if self.objects.has_key(name):
            return self.objects[name].touch()
        else:
            return 'there is no ' + name + ' arround!'

    def view(self, args = 'arround'):
        if (args !='' and args !='arround'):
            try:
                return self.panorama[args].view()
            except KeyError:
                try:
                    return self.objects[args].view()
                except KeyError:
                    return 'nothing'
        else:
            objects = ', '.join([k for k,v in self.objects.items()])
            if (objects != ''):
                obsight = '. 这里有: ' + objects
            else:
                obsight = ''
            return self.sight + obsight


import sys

class MudCommand:
    """ 欢迎来到世界之初！你可以使用以下指令在这个世界探险：
    go, move, help, exit, look, touch, say, take, drop, inventory, use """
    def __init__(self, char, area):
        self.char = char
        self.area = area

    def go(self, args):
        """ 移动 """
        return self.move(args)

    def use(self, args):
        """ 使用背包中的物品 """
        return self.char.use(args)

    def inventory(self, args):
        """ 查看背包 """
        return '背包中的物品有: '  + ', '.join(self.char.inventory)

    def help(self, args):
        """ 获取系统提示 """
        if args == '':
            return self.__doc__
        else:
            try:
                return getattr(self, args).__doc__
            except AttributeError:
                return 'help topic not found'

    def exit(self, args):
        """ 退出游戏 """
        print 'bye bye!'
        sys.exit()

    def look(self, args):
        """ 查看周围 """
        return  self.area.view(args)

    def take(self, args):
        """ 捡起某物"""
        try:
            return self.char.take(self.area.get_object(args))
        except AttributeError:
            return '你不能捡起 ' + args

    def touch(self, args):
        """ 触碰某物 """
        return self.area.touch_object(args)

    def drop(self, args):
        """ 丢掉某物 """
        return self.area.add_object(args, self.char.drop(args))

    def move(self, args):
        """ 移动 """
        area = self.area.relocate(args)
        if area != None:
            self.area = area
            return self.char.move(self.area)
        else:
            return 'There seems to be nothing what way.'

    def say(self, args):
        """ 说话"""
        return self.char.say(args)

class MudGame:
    def __init__(self, char, area):
        self.cmd = MudCommand(char, area)

    def run(self):
        while True:
            command = raw_input('> ');
            self.parse(command)

    def parse(self, command):
        comm = command.lower().split(' ')
        try:
            cmd = comm[0]
        except IndexError:
            cmd = 'help'
        try:
            args = comm[1:]
        except IndexError:
            args = []
        try:
            result = getattr(self.cmd, cmd)(' '.join(args).strip())
        except AttributeError:
            result = 'Unknow Command'
        print result

            
        
