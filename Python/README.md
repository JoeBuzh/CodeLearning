### Python面向对象

#### 1.OOP



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
 3. 

#### 4.继承

+ super() 继承父类

+ isinstance(), issubclass()

+ 



#### 5.特殊方法



#### 6.属性装饰器


