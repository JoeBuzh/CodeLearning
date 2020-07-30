### Python面向对象

#### 1.OOP

+ class(object)

+ instance(class)


#### 2.类与实例的关系

+ __init__(self)方法为初始化方法，类似java里面的构造方法

+ self代表当前的实例, self.xxx 实例变量

+ def(self, \*params) 实例方法

+ 实例变量：**实例.变量**；类变量：**类.变量**
 1. 实例  内部self.xxx, 外部intense.xxx
 2. 类   内部class.xxx, 外部class.xxx
 3. 类变量一般在__init__之前声明, 每个实例均可共享


#### 3.类方法与静态方法

+ 类方法
 1. @classmethod 
    + def func(cls, \*params):
 2. cls作用与self一样，self代表实例本身，cls代表类本身 
 3. 实例可以继承类的方法和属性
 4. 类方法一般用于创建对象实例
 
+ 静态方法
 1. @staticmethod
 2. def func(\*params): 需要self 或者 cls，不依赖于任务类和实例


#### 4.继承

+ super() 继承父类

+ isinstance(), issubclass()


#### 5.特殊方法

+ __xxx__
 1. __repr__ 将实例内容输出字符串 -> 调试
 2. __str__  将对象实例内容输出   -> 应用开发 ，相当于Java的tostring
 3. __add__
 4. 可参考datetime模块的源代码


#### 6.属性装饰器 

+ 对于类种的属性，可用property装饰，在__init__后一部分属性改变后，此属性认可按照对应进行改变

+ 实现统一数据的同步

+ 对外暴露方法，所有属性隐藏，通过方法改变属性

+ property Decorators
 1. Getters
 2. Setters
 3. Deleters
 