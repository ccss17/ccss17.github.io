
## **<div align="center"> ☀️ ️여기서부터 Day5   ☀️ </div>**

# Coding Convention

> 참고/출처 : https://en.wikipedia.org/wiki/Coding_conventions

코딩 컨벤션은 프로그래밍을 할 때 제시되는 가이드라인입니다. 코딩 컨벤션은 indentation, 주석처리, 선언문, 공백 문자, naming convention, 프로그래밍 원칙 등등 여러가지 가이드라인을 제시합니다. 

코딩 컨벤션은 여러가지가 있는데, 어떤 것을 따르던지 한 프로젝트에서는 통일된 컨벤션을 준수해야 합니다. 왜냐하면 코딩 컨벤션은 코드의 스타일을 통일하는 것으로써 마치 옷을 입는 스타일을 통일하는 것과 같기 때문입니다. 코딩 컨벤션이 뒤죽박죽이면 옷을 이상하게 껴입고 나가는 것과 같죠.

여기에서는 C/C++ 코딩 컨벤션과 Python 코딩 컨벤션을 간단하게 알아보겠습니다. 

## C/C++ Indentation Style

코딩 컨벤션은 여러가지 가이드라인을 제시하는데 그 중 하나가 Indentation Style 입니다.

- K&R, Allman

    ```c
    while (x == y)
    {
        something();
        somethingelse();
    }
    ```

- GNU

    ```c
    while (x == y)
      {
        something ();
        somethingelse ();
      }
    ```

- Whitesmiths 

    ```c
    while (x == y)
        {
        something();
        somethingelse();
        }
    ```

이렇게 각각의 Indentation Style 이 전혀 다름을 알 수 있습니다. 어떤 컨벤션을 따르든 상관없지만 한 프로젝트 내에서는 통일된 컨벤션을 유지해야 합니다.

## C++ Coding Convention

여러 커뮤니티와 회사들이 자신들의 코딩 컨벤션을 정립해두었습니다. 대표적으로 [Linux kernel](https://www.kernel.org/doc/html/v4.10/process/coding-style.html), [GNU C++ Style](https://gcc.gnu.org/wiki/CppConventions), [Microsoft C++ Style Conventions](https://docs.microsoft.com/en-us/windows/win32/stg/coding-style-conventions), [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html), [LLVM coding standards](http://llvm.org/docs/CodingStandards.html), [Chromium’s style guide](http://www.chromium.org/developers/coding-style), [Mozilla’s style guide](https://developer.mozilla.org/en-US/docs/Developer_Guide/Coding_Style), [WebKit’s style guide](http://www.webkit.org/coding/coding-style.html), [Qt Coding Style](http://wiki.qt.io/Qt_Coding_Style),   [Unreal Engine Coding Standard](https://docs.unrealengine.com/latest/INT/Programming/Development/CodingStandard/), [C++ Best Practices](http://codergears.com/QACenter/index.php?qa=questions), [Blender Coding Style](http://wiki.blender.org/index.php/Dev:Doc/Code_Style), [Blink Coding Style Guidelines](http://www.chromium.org/blink/coding-style), [Inkscape Coding Style](https://inkscape.org/en/develop/coding-style/), [CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md) 등등이 있습니다. 

이 중에서 [CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md) 이 가장 대표적인 C++ 코딩 컨벤션입니다. C++ 프로젝트를 진행한다면, 이러한 코딩 컨벤션 중 하나를 택하든가 아니면 프로젝트를 진행하는 사람들과 컨벤션에 합의를 보고 통일된 컨벤션으로 코딩을 하면 됩니다. 

한글번역도 있으니까 영어가 아직 어려우신 분들은 다음 링크를 참조해주세요. 하지만 원본을 영어로 읽으시는 것을 추천합니다. 

- https://www.cppkorea.org/CppCoreGuidelines/

## clang-format

하지만 매번 코딩 컨벤션을 신경쓰면서 코딩을 한다면 매우 피곤하겠죠. 이를 위하여 코딩 컨벤션을 자동으로 맞춰주는 툴이 있습니다. 그 툴 중 하나가 `clang-format` 입니다.

`clang-format` 은 `C`, `C++`, `Objective-C` 코드를 자동으로 포맷팅해주는 툴입니다. `clang-format` 은 **LLVM**, **Google**, **Chromium**, **Mozilla**, **WebKit** 의 `C++` 코딩 컨벤션에서 말하는 코드 포맷팅 기준을 자동으로 맞춰주기 때문에 일일히 코딩 컨벤션을 맞추느라 수고하지 않아도 되게 해줍니다. 

또한 코드 스타일을 `.clang-format` 파일에 명시하면 코드 스타일을 커스터마이징 할 수도 있습니다. 그래서 프로젝트 팀원들과 컨벤션 합의를 본 다음 `clang-format` 설정에 그 컨벤션 설정을 해준다면, 넋놓고 코딩을 해도 `clang-format` 이 그 컨벤션으로 자동으로 코드를 lint 해줍니다.

# Python Coding Convention

Python 코딩 컨벤션에는 대표적으로 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 이 있습니다. 일반적으로 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 을 많이 따라서 Python 코딩을 하니까 Python 에 더 관심있으신 분들은 꼭 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 를 공부해보세요.

또 Google 에서 제작한 [Google Python Coding Conventoin](https://google.github.io/styleguide/pyguide.html) 같은 것도 있으니까 여러가지 코딩 컨벤션을 비교해보고 가장 마음에 드는 컨벤션을 따르면 됩니다.

## pylint

Python 에도 자동으로 코딩 컨벤션을 맞춰주는 툴이 있습니다. 그것이 [`pylint`](https://www.pylint.org/) 인데 이 툴이 자동으로 [PEP 8](https://www.python.org/dev/peps/pep-0008/)을 맞춰주기도 하고, VSCode 에도 연동하여 사용할 수도 있으니까 정말 편하죠.

## **<div align="center"> 🌜 ️여기까지 Day5     🌜️ </div>**
