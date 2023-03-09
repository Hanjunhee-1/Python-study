# 같은 경로에 있는 것들은 sys.path 에 추가하지 않아도 바로 import 가능
# as 로 별명을 지어줄 수도 있음
import package_test.module1.mod1 as mod1
import package_test.module2.mod2 as mod2

mod1.ModuleTest1()
mod1.ModuleTest2()
print()
mod2.ModuleTest1()
mod2.ModuleTest2()
print()
print()

# from 을 사용하여 import 해줄수도 있음
from package_test.module1 import mod1 as m1
from package_test.module2 import mod2 as m2
m1.ModuleTest1()
m1.ModuleTest2()
print()
m2.ModuleTest1()
m2.ModuleTest2()
print()
print()


# 만약에 모든걸 import 해야할 경우에는 아래와 같은 방법을 사용할 수 있음. 웬만하면 필요한 것만 사용하기 
from package_test.module1 import * 
from package_test.module2 import *


# __init__.py: 패키지로 인식할 수 있게 해주는 역할을 한다. Python 3.3 이상 버전부터는 없어도 상관없지만 하위호환을 위해 작성하는 것을 추천한다.
# module1 과 module2 의 __init__.py 를 보면 __all__ = [''] 이런 것이 있는데 list 안에 있는 것들에 대해 접근할 수 있도록 허락해준다는 것이다. 
# 만약 아무것도 없다면 해당 모듈이 갖는 소스에 접근할 수 없다. 이런거 생각하기 귀찮으면 그냥 __init__.py 를 다 없애도 상관은 없다. 
# 웬만하면 Python 3.3 이상 버전을 사용하기 때문에...