통화 예시는 이제 끝났다. 이제는 xUnit에 대한 예시를 위해 python에서의 TDD의 좀 더 교묘한 활용을 보게된다.

## chapter 18

크기를 넓혀서 테스트 뿐 아니라 테스트 프레임워크를 만들어 테스트를 해보도록 한다.  
테스트 프레임워크를 만드는데도, 가장 먼저 할 일은 테스트를 작성하는 것이다.  
파이썬을 사용한다고해도, 이전에 배웠던 TDD의 기본 로직은 변하지 않는다. 똑같이 테스트와 구현, 중복 제거를 진행한다.

### getattr
파이썬에선 메서드의 이름을 함수처럼 다룰 수 있는데, 이를 활용해 테스트 코드를 보다 간단히 할 수 있다.
```python
class wasRun:
    def __init(self, name):
        self.wasRun = None
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()
    def testMethod(self):
        self.wasRun = 1

test = wasRun("testMethod")
test.run()
```
위와 같은 코드에서, `testMethod`를 name으로 넣고, `run()`에서 `getattr()`를 통해 받아서 실행하게 할 수 있다.  
이 후 `run()` 코드를 상위 클래스에 두어 모든 테스트에서 `run()`을 통해 테스트를 진행할 수 있도록 구현할 수 있다.  

### TestCaseTest
```python
class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
        def __init__(self, name):
            self.wasRun = None
            TestCase.__init__(self, name)

class TestCaseTest(TestCase):
    def testRunning(self):
        test = wasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("testRunning").run()
```
처음 완성한 테스트는 위와 같다. test가 run했는지를 확인하기 위한 테스트인데, test F/W을 만드는데 test를 하고 있는 미묘한 상황이다.

## chapter 19

### 3A (pattern)
테스트를 작성하다보면 발견하게되는 공통된 패턴.
1. arrange(준비) - 객체를 생성한다.
2. act(행동) - 어떤 자극을 준다.
3. assert(확인) - 결과를 검사한다.

170p