
Rust 는 [Official Documentation](https://doc.rust-lang.org/book/) 이 매우 잘 정립되어 있어서 이것을 기반으로 쉽게 배울 수 있는데 이 문서의 특징은 기존의 C++ 언어 같은 memory-unsafe 언어와는 달리 어떻게 Rust 가 memory-safe 언어를 이룰 수 있었는지에 대한 철학과 규칙을 설명한다는 것이다. 

다음 리스트는 기존의 C/C++ 같은 memory-unsafe 언어가 근본적으로 우리를 해킹취약점으로부터 구원할 수 없기 때문에 애초에 Rust 나 Swift 같은 memory-safe 언어를 사용해야 한다는 주장의 논거가 되는 글들이다.

- [Modern C++ Won't Save Us](https://alexgaynor.net/2019/apr/21/modern-c++-wont-save-us/)

- [Undefined behavior in C is a reading error.](https://www.yodaiken.com/2021/05/19/undefined-behavior-in-c-is-a-reading-error/)

- [C++ Software Security Sins](https://www.cppstories.com/2021/security-sins/)

- [Speed of Rust vs. C](https://kornel.ski/rust-c-speed)

- [Google is now writing low-level Android code in Rust](https://arstechnica.com/gadgets/2021/04/google-is-now-writing-low-level-android-code-in-rust/)

- [Google Wants Rust In Kernel](https://www.phoronix.com/scan.php?page=news_item&px=Google-Wants-Rust-In-Kernel)

- [Microsoft: 70 percent of all security bugs are memory safety issues](https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/)

- [Chromium project finds that 70% of security defects are memory safety problems](https://www.chromium.org/Home/chromium-security/memory-safety)

- [Memory safe ‘curl’ for a more secure internet](https://daniel.haxx.se/blog/2020/10/09/rust-in-curl-with-hyper/)

특히 이 문서가 memory-safe 언어를 사용해야 하는 중요한 근거가 될 수 있을듯.

- [Mitigating Memory Safety Issues in Open Source Software](https://security.googleblog.com/2021/02/mitigating-memory-safety-issues-in-open.html)

C/C++ 시대는 가고 memory-safe 언어(Rust, Go, Swift 등)의 시대가 오지 싶네.

그래서 Rust 를 익혀보자 이거지요. 그러니까 위 공식 문서에서 설명되는 Rust 만의 독특한 철학과 규칙들을 좀 정리해두어야 할 필요가 있다. Rust 의 문법은 정리할 필요가 없지만, 다른 언어에서 찾아볼 수 없는 Rust 만의 독특한 문법같은 경우는 예외적으로 정리해둘 필요가 있다. 

다음 메일기록은 Linux community 가 Rust 를 Linux kernel 이 지원하는 공식적인 두번째 언어로 채택했다는 것을 알려준다.

- https://lore.kernel.org/lkml/20210704202756.29107-1-ojeda@kernel.org/

# Ownership Rules

- Each value in Rust has a variable that’s called its owner.

- There can only be one owner at a time.

- When the owner goes out of scope, the value will be dropped.

    - 메모리를 사용하면 지금까지 그것을 해제하는 두 가지 방법이 있었다. 첫째는 GC 를 사용하는 것이다. GC 는 더 이상 참조될 수 없는 포인터가 발견되면 자동으로 메모리를 해제해준다. 둘째는 직접 메모리를 해제해주는 것이다. 하지만 직접 해제를 너무 빨리하면 부적절한 포인터가 발생하고 너무 늦게하면 메모리가 낭비되며 두번 해제하면 double free 버그가 발생한다. 

        Rust 는 이와 달리 scope 를 넘어서면 drop 함수를 호출하여 자동으로 메모리를 해제해주는 방식을 택했다. 

# Move

String 은 스택에 ptr, len, capacity 를 저장하는데 String 변수를 다른 변수에 저장하면 ptr, len, capacity 가 스택에 저장되고, 힙에 있는 데이터 자체가 복사되지는 않는다. 하지만 Rust 가 scope 를 넘어서면 메모리를 해제해주기 때문에 두 String 변수가 살아있으면 double free 버그가 발생한다. 따라서 String 변수를 다른 변수에 저장하면 Rust 는 이전 변수를 더 이상 사용할 수 없고 해제할 필요도 없는 죽은 변수로 취급한다.

그러므로 Rust 가 동적 메모리 포인터를 복사하는 방식은 shallow copy 와 비슷하다. shallow copy 는 힙에 있는 실제 데이터를 복사하지 않고 포인터ptr, 길이len, 용량capacity만 복사하는 것이기 때문이다. 하지만 Rust 는 shallow copy 를 하는 것이 아닌데, 왜냐하면 이전의 변수를 죽이기 때문이다. 그러므로 Rust 는 Move 를 한다고 말하는 게 맞다.

# Copy 

단 integer 같이 완전히 stack 에 저장되고 데이터 사이즈를 파악할 수 있는 것들은 다른 변수에 저장할 때 실제 데이터까지 잘 복사가 된다.

만약 어떤 타입에 Copy trait 가 선언되면 integer 를 복사하는 것처럼 저장될 때 복사된다. 이 trait 는 Drop trait 와 함께 선언될 수 없다. integer, bool, float, character, tuple 같은 것들에 Copy trait 가 선언되어있다.

# 함수 인자 전달

함수 인자 전달은 Move 이거나 Copy 이다. Move 로 파라미터를 전달하면 그 변수의 Ownership 이 넘어간 것이므로 더 이상 사용할 수 없다. Copy 로 파라미터를 전달하면 계속 변수를 사용할 수 있다.

# 함수 반환값 전달

함수 반환값 전달도 Move 이거나 Copy 이다. 함수가 return 하는게 Move 이면 Ownership 이 상위 함수로 이동한다.

# Reference

하지만 함수가 Ownership 을 가져가지 않고 값만 사용하게 하고 싶다면 Reference 를 사용한다. Reference 를 만들면 Ownership 은 갖고 있지 않게 된다.

만약 `let s1: String` 의 Ownership 을 넘겨주지 않고 값만 넘겨주고 싶다면 `let s :&String = &s1` 처럼 한다. String 이 ptr, len, capacity 를 갖고 있다면 &String 은 ptr 만 갖고 있다. 

Reference 를 함수 파라미터로 넘겨주는 것을 borrowing 이라 한다. borrowing 해온 변수는 수정할 수 없다.

# Mutable Reference

그런데 예외적으로 Reference 를 사용할 때에도 값을 변경해야 하는 경우가 있다. 이 경우 `let mut s1: String` 에 대하여 `let s: &mut String = &mut s1` 와 같이 하면 된다. 이렇게 Mutable Reference 를 만들 수 있다. 그리고 dereferencing 을 사용하여 `*s = (VALUE)` 로 변경할 수 있다.

하지만 Mutable Reference 는 위험하기 때문에 다음과 같은 제약사항이 있다. 

- 특정 데이터에 대한 스코프 내에서 Mutable Reference 는 유일하다.

    다른 언어들은 이런 제약이 없지만 이 제약으로 인하여 Rust 는 컴파일할 때 data race 를 예방한다. 이로써 두개 이상의 포인터가 같은 데이터에 같이 접근하는 data race 를 예방한다.

- Reference 가 있다면 Mutable Reference 는 없다.

    이 제약이 존재하는 이유는 Reference 를 가져간 공간에서는 해당 데이터가 불변할 거라고 기대하기 때문이다. (그러면 owner 가 데이터를 바꾸는 경우에도 컴파일 에러가 발생하나? cannot assign to `s` because it is borrowed 라고 에러가 발생하네.)

    이때 Reference 의 스코프는 Reference 가 마지막으로 사용된 때까지 이므로 Reference 가 선언되어도 마지막으로 사용된 이후에 Mutable Reference 가 선언되고 사용되면 아무런 문제가 발생하지 않는다.

# Slice

Slice 도 Reference 와 같이 데이터에 대한 Ownership 을 갖지 않는 데이터 타입이다. 하지만 Reference 와 다르게 Slice 는 연속적인 데이터의 부분 데이터를 참조한다.

`let s: String = String::from("hello word")` 의 Slice 를 만드려면 `let world: &str = s[6..11]` 와 같이 만들 수 있다. 이것은 s 의 7번째 바이트부터 5바이트만큼의 slice 를 만든다는 것이다. 

기존의 String 이 ptr, len, capacity 로 구성되었다면 slice 는 ptr, len 으로 구성된다.

String 의 Slice 를 생성할 수 있지만, Slice 의 Slice 도 생성할 수 있다.

String literal 은 String Slice 이다. 즉, `let s: &str = "abc";` 이다.

지금까지 String 의 Slice 만 살펴보았지만 Slice 는 일반적인 타입이다. integer 배열의 Slice 를 만들 수도 있다. `let a: [i32; 5] = [1,2,3,4,5]` 의 slice 를 `let slice: &[i32] = &a[1..];` 와 같이 만들 수 있다.

---

# Struct

Struct 는 관련된 데이터를 모아주는 데이터타입이다. OOP 에서 Data 와 기능이 있다면 Struct 가 Data 를 담당한다. 

기본 Struct 외에도 tuple Struct 와 Unit-Like Struct 를 선언할 수도 있다. Unit-Like Struct 는 아무 필드가 없지만, 아무 데이터가 없는 타입에 대한 trait 를 구현할 때 사용된다.

Struct 를 사용하는 연습을 할 때 `&str` 이 아니라 String 타입으로 문자열을 멤버로 선언했다. 그 이유는 Struct 의 멤버 전체가 Struct 가 살아있을 때까지 살아있는다는 보장이 필요하기 때문이다. 그러나 물론 Struct 에서 Reference 를 멤버로 가질 수 있는 장치인 lifetime 이 있다. lifetime 은 Reference 인 Struct 멤버가 Struct 의 수명보다 같거나 길다는 것을 보장해준다. 만약 lifetime 없이 Struct 에 Reference 를 멤버로 정하면 에러가 발생한다.

# Method

Method 는 Function 과 거의 비슷한 문법을 가지지만, Function 과 달리 Struct 과 관련되어 `impl` 블록 안에 정의된다. Method 의 첫번째 파라미터에는 `self` 키워드가 있어야 한다. `self` 는 Struct 의 인스턴스를 뜻한다. 

많은 경우 Method 의 첫번째 파라미터를 `&self` 로 정하여 인스턴스의 Ownership 을 가져오지 않는다. 만약 `self` 로 한다면 Ownership 이 가져와져서 Method 의 스코프가 끝날 때 인스턴스의 메모리가 해제되기 때문에 예외적인 상황에서만 사용된다. `self` 를 사용하는 경우는 인스턴스 자체를 바꾸고 caller 가 원래의 인스턴스를 사용하지 못하게 하는 경우를 들 수 있다.

`&mut self` 로 Method 에서 인스턴스의 데이터를 변경할 수 있다. 인스턴스를 수정해야 할 때 왠만하면 `self` 보다 `&mut self` 를 사용하겠지만, `&mut self` 는 인스턴스 자체가 Mutable 로 선언되어야 한다는 단점이 있다. immutable 인스턴스를 기반으로 새로운 인스턴스를 만들어서 반환해야 할 때 `self` 를 쓰면 되겠지.

# Automatic referencing and dereferencing

C/C++ 에서는 인스턴스의 멤버를 참조할 때 `.` 을 사용하고 포인터의 멤버를 참조할 때 `->` 를 사용한다. 하지만 Rust 는 Automatic referencing and dereferencing 기능이 있어서 Reference 의 멤버를 참조할 때 원래 인스턴스에서 멤버를 참조하는 것처럼 `.` 을 사용한다.

# Associated Functions

`impl` 블록 안에는 `self` 파라미터가 없는 Associated Function 을 정의할 수 있다. 이는 Struct 의 인스턴스를 받지 않으므로 Method 가 아니지만, Struct 와 밀접한 관련이 있는 함수이다. 가령 `String::from` 이 Associated Function 이다. 이처럼 Associated Function 은 대표적으로 Struct 의 Constructor 로 사용된다.

---

# Enum

커스텀 타입을 만드는 방법은 Struct 외에도 Enum 이 있다. Enum 은 특정 타입의 데이터가 여러 변형을 가지는 것을 표현하기 위하여 사용된다. 가령 IP 의 버전에는 v4, v6 이 있는데 이 변형을 표현하기 위하여 enum 을 사용할 수 있다.

Enum 은 여러 변형에 대한 추상 데이터가 되어 모든 변형들을 한꺼번에 다룰 수 있다. 가령 함수 선언에서 enum 을 쓰면 모든 변형을 파라미터로 받을 수 있다.

Enum 의 변형에 데이터 타입을 연관시킬 수 있는데, 이렇게 하면 Enum 변형이 가지는 데이터를 표현할 추가적인 Struct 를 선언하지 않아도 된다.

# Enum Method

Enum 도 Struct 와 같이 `impl` 블록 안에 Method 를 구현할 수 있다.

# Important Enum: Option<T>

`Option<T>` 는 Rust 에서 null 로 인하여 발생하는 수많은 버그를 해결하기 위하여 만든 Enum 이다. 이 `Option<T>` 는 `Some<T>` 과 `None` 이라는 변형을 가지는데, 이것 외에 null 을 표현할 수 있는 변수는 존재하지 않는다. 이 설계 덕분에 `Option<T>` 가 아닌 모든 변수는 null 이 아니라는 보장을 얻을 수 있다. 

# Match

Match 는 Enum 의 모든 변형들의 경우에 대한 처리를 할 때 사용된다. 그래서 어떤 변형이라도 `match` 에서 제외되면 에러가 발생한다. `match` 가 `if-else` 와 다른 점은 `if-else` 는 `bool` 타입을 넣을 수 있는데 `match` 에는 어떤 타입이라도 넣을 수 있다는 것이다.

기본적으로 `match` 의 case 에 대상 데이터와 다른 자료형을 넣을 수 없고, 자유변수가 들어간다면 임의의 대상 데이터가 매칭된다. case 에는 자료형 자체가 아니라 literal 이 들어가야 하는데, 나는 처음에 자료형 자체를 넣어야 하는 줄 알고 `u32` 같은 자료형을 넣어봤는데 대상 데이터가 String 인데도 매칭이 되는거야. 그래서 조사해보니까 `u32` 가 자유변수로 인식되어서 `u32` 라는 변수에 String 타입 대상 데이터가 전달되었던 거였지.

# if let

`match` 는 데이터의 모든 경우에 대한 행동을 정의하지 않으면 사용할 수 없다. 하지만 우리는 하나의 경우에 대해서만 다루고 싶을 때도 있다. 하나의 경우만 다루더라도 `_ => ()` 을 써야하듯이 `match` 는 너무 장황해진다.

그러므로 이렇게 하나의 경우만 다룰 경우 `match` 대신 `if let` 문법을 쓰면 된다. `if let` 은 `=` 으로 매칭 패턴과 대상 데이터를 구분하는데, 이는 `match` 의 매칭 패턴, 대상 데이터와 완전히 동일하다.

---

# Package 와 Crate

crate 는 바이너리 혹은 라이브러리이다. crate root 는 Rust 가 컴파일을 시작할 소스 파일이다. 

package 란 특정한 기능을 제공하는 하나 이상의 crate 들이다. package 는 반드시 하나 이상의 바이너리 crate 를 가져야 하고, 반드시 0개나 1개의 라이브러리 crate 를 가져야 한다. 

package 는 Cargo.toml 파일을 갖고 crate 들을 어떻게 빌드할지 정의한다.  Cargo.toml 이 crate 를 어떻게 빌드할지 정한다고 했지만, 우리가 `cargo new` 를 통해 생성한 package 가 갖고 있는 엔트리 포인트인 `src/main.rs` 가 Cargo.toml 에는 없다. 이는 `src/main.rs` 가 바이너리 crate 의 디폴트 엔트리 포인트이기 때문이다.

Cargo 는 `src/main.rs` 가 있으면 이를 package 의 이름과 같은 바이너리 crate 로 인식한다. 또한 `src/lib.rs` 가 있으면 이를 package 의 이름과 같은 라이브러리 crate 로 인식한다.

package 는 바이너리 crate 소스를 src/bin/ 에 위치시킴으로써 여러 바이너리 crate 를 가질 수 있다.

# Module

`pub` 키워드는 아이템을 public 으로 만든다.

`mod` 키워드는 Module 을 만든다. Module 은 crate 의 코드를 가독성과 재사용성을 위해 여러 그룹들로 모을 수 있게 해준다. Module 은 또한 아이템을 public 으로 만들거나 private 으로 만든다.

src/main.rs 와 src/lib.rs 가 crate root 라고 했는데 그 이유가 이 파일의 내용이 "crate" 라는 Module 을 이루고 이 Module 이 crate 의 모듈 구조(module tree)의 root 가 되기 때문이다.

Module 내부의 아이템을 사용하기 위하여 path 를 사용한다. path 는 절대 경로와 상대 경로가 있다. 절대 경로는 crate root 인 `crate` 부터 해당 아이템까지의 모든 경로를 다 사용하여 아이템을 참조하는 것이다. 상대경로는 현재 Module 로부터 경로를 시작하여 아이템을 참조하는 것이다. `super` 키워드로 상대경로를 한 단계 상위의 Module 에서부터 시작할 수도 있다.

하위 Module 은 상위 Module 의 아이템을 사용할 수 있지만, 상위 Module 은 하위 Module 이 public 이 아닌 이상 하위 Module 의 아이템을 사용할 수 없다. 만약 서로 같은 레벨의 아이템들이라면 다른 아이템이 public 이 아니어도 참조할 수 있다.

Struct 도 Module 안에 정의할 수 있다. Struct 를 public 으로 만든 것으로 필드값들이 public 이 되는 것은 아니다. Struct 의 필드값 각각에 `pub` 키워드를 사용해야 각 필드에 접근 할 수 있다.

Struct 를 public 으로 지정한 이후에 필드도 public 으로 지정해야만 Struct 의 필드에 접근할 수 있는 것과 달리, Enum 은 public 으로 지정되면 모든 변형이 public 이 된다. 

## Module 위계 

같은 레벨이면 namespace 로 참조하지 않아도 item 을 참조할 수 있다. 가령 `main` 함수 바로 위에 선언된 `test` 라는 함수를 `main` 함수에서 바로 호출할 수 있다.

하지만 Module 로 분리되면 다른 레벨이 된다. 이 경우 같은 Module 인데 상하 관계가 분리되었는지, 아예 다른 Module 로 분리되었는지 나뉜다.

같은 Module 인데 상하 관계가 분리되었다면 하위 레벨에서 상위 레벨의 item 을 그냥 참조할 수 있다. 하지만 상위 레벨에서 하위 레벨의 public 이 아니면 참조할 수 없다.

아예 다른 Module 로 분리되었다면 상대 경로나 절대 경로로 Module Path 를 지정해주어야 item 을 참조할 수 있다.

# use

`use` 키워드는 아이템에 대한 경로를 가져온다. Module 의 경로를 매번 반복하기가 너무 힘들 때 `use` 를 쓴다. `use` 에 절대경로를 입력할 수도 있고 상대경로를 입력할 수도 있다.

`as` 키워드로 `use` 키워드로 가져온 아이템에 다른 이름을 부여할 수 있다.

`pub use` 키워드로 `use` 키워드가 편리하게 만든 경로 단축을 외부에서도 사용하게 할 수 있다.

# Separating Modules into Different Files

`mod` 키워드로 Module 을 선언 후 바디를 정의하지 않고 세미콜론 `;` 으로 Module 선언을 끝내버리면, Rust 는 Module 이름과 같은 다른 파일(src/[Module Name].rs)에서 Module 바디의 정의를 찾는다. 

분리된 Module 내에서도 Module 을 분리시켜 선언한다면 (src/[Module Name]/[Sub Module Name].rs) 에서 Module 바디를 찾는다.

---

# Collections

built-in array 나 tuple 외에 데이터가 힙 메모리에 저장되는 데이터 타입을 Collections 이라 한다. 

## Vector 

Vector 도 Mutable Reference 와 immutable Reference 를 함께 가질 수 없다는 규칙을 따라야 한다. 그러므로 `let mut v = vec![1]; let n = &v[0]; v.push(1);` 이라는 코드는 에러이다. `&v[0]` 으로 immutable Reference 를 가져온 후 `v.push(1)` 로 Mutable Reference 가 생성되기 때문이다.

Vector 는 같은 타입의 데이터만 저장되도록 하기 때문에 어떤 상황에서 불편할 수 있다. 이럴 때는 필요한 데이터 타입을 Enum 으로 정의해서 Enum 데이터를 Vector 에 저장하면 된다.

## String

`String::push_str(s)` 함수는 s 의 Ownership 을 가져가지 않는다.

String 을 서로 붙일 때 `let a="a".to_string();let b="b".to_string();let c=a+&b;` 와 같이 하면 a 는 c 로 Move 되어서 더 이상 사용될 수 없다.

String 은 indexing 을 지원하지 않는다. String 은 `Vec<u8>` 의 wrapper 이다. 따라서 `let s = String::from("Hola");` 와 같은 영어를 저장할 때 4byte 로 잘 저장된다. 하지만 `let hello = String::from("Здравствуйте");` 와 같은 UTF-8 언어를 저장할 때는 문자 당 2byte 가 필요해진다. `let s = &hello[0];` 으로 인덱싱을 하면 "З" 이라는 문자가 UTF-8 로 인코딩 되어 2byte 를 사용하면서 208, 151 로 저장되기 때문에 208 이 반환되어야 한다. 하지만 208 은 올바른 문자가 아니다. 우리가 원하는 것은 "З" 인데 이것을 UTF-8 2byte 로 표현하려면 208, 151 이 필요하다. 따라서 개발자가 기대한 값이 반환되지 않는 상황과 그 상황으로 인한 버그를 차단하기 위하여 Rust 는 아예 String 에 대한 indexing 을 지원하지 않기로 결정했다. 

하나의 숫자로 String 을 [] 로 indexing 은 차단하는 대신 정말로 굳이 String slice 가 필요한 경우를 위하여 숫자 범위로 String 을 [] 로 indexing 하는 것은 허용한다. 그래서 `let s = &hello[0..4];` 와 같은 첫 4byte 를 가져오겠다는 코드는 허용된다. 하지만 0..1 이나 0..3 같이 slice 를 만들면 invalid chracter boundary 를 참조했다면서 panic 에 빠진다. 그래서 범위를 참조할 때 엄청 조심해야 한다.

## HashMap

이 Collections 은 Key, Value 구조를 갖는 데이터 구조이다. Ownership 을 갖는 데이터만 Key:Value 로 등록해야 한다. Reference 를 HashMap 에 등록하려면 Reference 가 HashMap 이 살아있는 동안 반드시 살아있어야 한다는 보장(lifetime)이 필요하다. lifetime 없이는 Reference 를 HashMap 에 등록할 수 없다.

---

# Error

Rust 는 error 를 recoverable 과 unrecoverable 로 구분한다. 다른 언어는 이 구분을 하지 않고 모든 error 를 같은 방식으로 처리하지만, Rust 는 recoverable 을 위하여 `Result<T, E>` 타입을 만들었고 unrecoverable 을 위하여 panic! 을 만들었다. 

## unrecoverable error

panic 이 일어났을 때 stack 을 역추적하면서 clean up 을 하는 unwinding 을 한다. 하지만 unwinding 은 상당히 많은 작업을 필요로 하므로 panic 의 행동을 unwinding 에서 abort 로 바꿀 수 있다. abort 는 메모리 정리를 하지 않고 바로 종료시킨 후 메모리 정리를 OS 에 맡긴다. 만약 최종 컴파일된 실행파일의 크기를 최대한 줄이고 싶다면 Cargo.toml 에 

```toml
[profile.release] 
panic = 'abort' 
```

라고 설정하면 된다.

## recoverable error

recoverable 에러는 

```rust
enum Result<T, E> { 
    Ok(T), 
    Err(E), 
} 
```

로 다뤄진다. 가령 `let f = File::open("test.txt");` 은 `Result<File, Error>` 를 반환하므로 

```rust
let f = match f {
    Ok(file) => file,
    Err(error) => 에러처리,
}
```

와 같이 사용하면 된다. Err 일 경우 panic 을 하든지, 다른 파일 이름을 입력하게 하든지 에러 처리를 하면 된다. Option Enum 처럼 Result Enum 도 prelude 에 있으므로 `Result::Ok` 가 아니라 그냥 `Ok` 로 해도 된다.

error 를 caller 함수에서 처리하도록 propagating 하는 방법도 있다. 이는 callee 함수에서 `Result<T, E>` 자체를 반환하는 것이다. 하지만 `Result<T, E>` 를 반환하기 위하여 `match` 를 사용해야 하는데, 이 propagating 패턴이 자주 사용되어서 `?` 로도 propagating 할 수 있게 되었다.

`?` 는 Result 바로 뒤에 위치하여 `Result<T, E>` 를 propagating 하기 위한 `match` 문과 거의 비슷하게 작동한다. `Result` 가 Ok 라면 Ok 의 값이 반환되고 `Err` 라면 `Err` 가 return 된다. 따라서 `?` 로 propagating 을 했을 경우 `?` 는 `Err` 만 return 해주기 때문에, 마지막에 `Ok` 값을 return 해주어야 한다.

propagating 에서 `?` 가 `match` 와 다른점은 `?` 에서의 에러는 에러 타입을 변환하는데 사용되는 `From` trait 가 정의된 `from` 함수를 거쳐간다는 것이다. `?` 가 `from` 함수를 호출하면 발생한 에러 타입이 함수의 반환에서의 에러 타입으로 변환된다. 이는 함수 내에서 발생하는 모든 에러를 함수의 반환 에러 타입이 대표할 수 있을 때 유용하다.

일반적으로 `?` 는 propagating 뿐만 아니라 `Result` 타입, `Option` 타입 등 `std::ops::Try` 를 구현한 타입을 반환하는 모든 곳에서 사용될 수 있다.

## Choice to recoverable or unrecoverable

`panic!` 은 unrecoverable 인 상황에서만 사용한다. 하지만 다른 많은 경우 `Result` 를 반환해라. 그러면 caller 에서 `Result` 의 `Err` 를 보고 또 다시 recoverable 인지 unrecoverable 인지 판단할 수 있다.

예측 가능한 에러라면 recoverable 이고, 예측 불가능한 에러라면 unrecoverable 이다. 에러를 fix 할 방법이 있으면 recoverable 이고 방법이 없으면 unrecoverable 이다. 

## Advice to error handling 

Rust 튜토리얼에서는 랜덤값 맞추기 예제가 나오는데 유저는 1~100 까지의 숫자를 입력해야 한다. 이것의 에러를 매번 검사하는 것이 아니라 새로운 타입을 만들고 그것에 적용되는 메소드를 만들면 값이 생성될 때 에러처리가 자동으로 된다. 이렇게 하면 모든 곳에서 매번 에러 처리를 할 필요가 없는 거지.

---

# dereferencing coercion

```rust
let a="a".to_string();
let b="b".to_string();
let c=a+&b; 
```

와 같은 코드가 가능한 이유는 `+` 가 `fn add(self, s: &str) -> String` 이라는 함수로 변환되기 때문이다. 첫번째 파라미터가 `self` 이므로 Reference 기호 `&` 를 `a` 에는 안붙혀도 되고, `a` 의 Ownership 이 이동하는 것이다.

이때 `&b` 는 `&String` 이고 `&str` 이 아닌데 어떻게 두번째 파라미터로 전달될 수 있었을까? 이는 Rust 가 `&b` 를 `&b[..]` 으로 변환시켜서 `&String` 을 `&str` 로 변환시키기 때문이다. 이것이 deref coercion 이다.

# main function return type

`main` 함수의 반환값은 `()` 와 `Result<T, E>` 이 가능하다.

# for 

```rust
let mut max: i32 = 0;
for &n in &l {
    if n > max {
        max = n;
    }
}
```

`&l` 이라고 안하면 `l` 의 Ownership 이 for-loop 안으로 이동되고 for-loop 의 스코프가 끝날 때 해제되버린다. `&n` 이라고 안하고 `n` 이라고 하면 `n` 은 `&i32` 이기 때문에 `*n` 으로 해야 max 와 연산할 수 있다. 

---

# Generic 

여러 데이터 타입에 적용되는 반복되는 코드를 Generic 으로 통합시킬 수 있다. Method 와 Struct 와 enum 에 Generic 을 사용할 수 있다. `impl` 블록도 Generic 으로 구현할 수 있고, 특정 데이터 타입에만 구현할 Method 를 선언하는 `impl` 블록을 선언할 수도 있다. 

```rust
impl<T> Point<T> {
    fn method(self) {
        ...
    }
}

impl Point<f32> {
    fn method2(&self) {
        ...
    }
}
```

Generic 으로 구현된 `impl` 블록 안에서도 Generic 메소드를 선언할 수 있다. 

```rust
impl<T> Point<T> {
    fn method<U>(self, other: Point<U>) -> Point<U> {
        ...
    }
}
```

## Monomorphization 

C++ 같은 경우 Template 을 많이 사용하면 v-table 인가 그런것 때문에 성능이 떨어진다고 들었었는데, Rust 는 Monomorphization 이라는 Generic 을 컴파일 상에서 특정 데이터 타입으로 바꿔주는 기법 때문에 성능이 안떨어진다.

---

# Trait

trait 는 특정 데이터 타입들이 공유하는 공통된 기능이다. Java 에서 interface 와 살짝 비슷한 개념이다. trait 에 선언된 함수가 trait 를 구현한 struct 에 똑같은 함수 선언으로 구현되어야 한다.

다른 라이브러리에 있는 trait 를 가져와서 자신이 정의한 struct 에 구현할 수도 있다. 이 경우 `use <PACKAGE>::<PATH_TO_TRAIT>::<TRAIT>;` 를 사용한 다음 struct 에 trait 를 구현하면 된다. 

## orphan rule (coherence)

이때 중요한 것은 trait 를 struct 에 구현할 때 trait 나 struct 중 하나는 반드시 local 패키지에 선언되어있어야 한다. 즉, 외부 패키지의 trait 를 외부 패키지의 struct 에 구현할 수 없다.

이 규칙이 없다면 Rust 는 같은 데이터 타입에 대한 같은 trait 를 구현한 두개 이상의 crate 를 허용하게 된다.

## Default Implementation

trait 에 method 선언만 하는 것이 아니라 method 본체를 구현해 놓으면 trait 를 구현할 struct 의 Default Implementation 이 된다. Default Implementation 을 사용하고 싶다면 `impl <TRAIT> for <STRUCT> { }` 와 같이 `impl` 블록을 비어있는채로 냅두면 된다. 

## Trait as Parameter

trait 를 함수의 파라미터로 전달할 수도 있다. 이 경우 trait 를 구현한 struct 들을 대표할 수 있게 된다. `fn f(p: &impl Trait)` 와 같이 사용된다. 

## Trait Bound

`impl Trait` 는 Trait bound 의 syntax sugar 이다. trait bound 는 

```rust
fn f<T: Trait>(p: &T)
``` 

와 같이 사용한다. Generic 과 비슷한데 콜론을 쓰고 Trait 를 명시하면 된다.

하지만 차이점이 있는데, 

```rust
fn f(p: &impl Trait, q: &impl Trait)
``` 

라고 하면 p 와 q 가 다른 타입이어도 되지만 

```rust
fn f<T: Trait>(p: &T, q: &T)
``` 

라고 하면 p 와 q 가 같은 타입이어야 한다.

## Multiple Trait Bound 

여러 Trait 를 구현한 struct 를 파라미터로 전달하기 위해서 

```rust
fn f(p: &(impl Trait1 + Trait2))
```

이나 

```rust
fn f<T: Trait1 + Trait2>(p: &T)
```

와 같이 하면 된다.

## where

trait bound 가 많을 경우 함수 선언을 읽기가 힘들어진다. 이를 위하여 trait bound 를 함수 선언 다음에 정의할 수 있도록 `where` 문을 쓰면 된다. 

```rust
fn f<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 
```

위 코드가 다음 코드와 동일하다.

```rust
fn f<T, U>(t: &T, u: &U) -> i32
    where T: Display + Clone,
          U: Clone + Debug
```

## return Trait

Trait 를 반환하기 위해서 `fn f() -> impl Trait` 와 같이 `impl Trait` 를 반환형으로 삼으면 된다. 하지만 함수가 반드시 하나의 타입을 반환해야 한다. 가령 `fn f() -> impl Summary` 로 선언된 함수에서 조건에 따라 NewsArticle 이나 Tweet 타입이 반환되면 컴파일이 되지 않는다.

## conditionally implement method

```rust
impl<T: Display> ToString for T
``` 

라고 하면 `ToString` Trait 를 `struct T` 위에 구현하는데 `T` 는 `Display` Trait 가 정의된 것이라고 해석한다. 이 선언이 `std` 에 정의되어 있으므로 `Display` Trait 가 정의된 모든 데이터 타입에 대하여 `to_string` 함수를 사용할 수 있는 것이다. 

`impl` 블록 안에서 `Self` 라고 하면 해당 타입을 지칭하게 된다. 

---

# Lifetime

Lifetime 은 Reference 가 적절한 시간동안 살아있다는 것을 보장해주는 Generic 이다. 모든 Reference 는 스코프 내에서 유효하다는 lifetime 을 갖는다. Lifetime 의 목적은 Dangling Reference 가 발생하는 것을 차단하는 것이다.

## borrow checker

Rust 는 컴파일 시 Reference 와 대상 데이터의 lifetime 을 계산한다. 그리고 다음 조건이 충족되지 않으면 에러를 발생시킨다.

- Reference 의 lifetime 이 대상 데이터의 lifetime 에 포함된다.

## Generic Lifetime

다음과 같이 함수를 짜면 Lifetime 이 필요하다는 에러가 발생한다. 

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

이 함수에서 `x` 와 `y` 의 값을 정확히 모르기 때문에 `if` 문이 실행될지 `else` 문이 실행될지 알 수 없다. 또한 Reference 들의 lifetime 도 알 수 없다. borrow checker 도 이 Reference 들이 항상 유효한지 알 수 없다. 왜냐하면 `x`, `y` 의 lifetime 이 반환 Reference 의 lifetime 과 어떤 관계를 갖는지 알 수 없기 때문이다. 이 에러를 해결하기 위하여 Reference 간의 관계를 정의하는 Generic Lifetime 을 추가하면 borrow checker 가 lifetime 분석을 해낼 수 있다.

Rust 가 이 함수에게 원하는 것은 `x,y` 와 반환 Reference 가 최소한 함수가 끝날 때 까지 살아있다는 보장이다. 

## Lifetime Annotation in Function

Lifetime annotation 은 Reference 의 수명에 영향을 끼치지 않는다. Lifetime annotation 은 단지 여러 Reference 의 lifetime 간의 관계를 설명해준다. 

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

기존의 `longest` 함수에 위와 같이 lifetime `'a` 를 추가함으로써 `x,y` 그리고 반환값이 최소한 lifetime `'a` 만큼 살아있음을 보장해준다. 이러면 `x,y` 와 반환 Reference 가 최소한 함수가 끝날 때 다 함께 살아있다는 보장이 되므로 드디어 컴파일이 된다.

이것은 실제상황에서 함수가 반환하는 Reference 의 lifetime 이 파라미터로 전달되는 Reference 의 lifetime 보다 같거나 작다는 것을 의미한다.

이처럼 함수에 Lifetime annotation 을 정의하는 것은 Reference 의 lifetime 에 실질적인 영향을 주지 못하지만, borrow checker 가 이 lifetime 관계를 따르지 않는 Reference 가 전달되는 것을 제한할 수 있도록 하는 역할을 한다.

즉, `x, y` 와 반환 Reference 가 최소한 `'a` 만큼 살아있다는 것이 보장되므로 `longest` 가 컴파일된다는 말인데, 그러면 `'a` 는 어떻게 결정되는가? 먼저 `x` 의 수명이 `'a` 로 정의되었으므로 `'a` 의 수명은 `x` 가 되는데, `y` 도 `'a` 로 정의되었으므로 `x` 와 `y` 의 겹치는 수명이 `'a` 의 값이 된다. `'a` 의 수명은 이렇게 파라미터의 Reference 의 교집합으로 결정된다. 이때 반환 Reference 도 `'a` 로 정의되었으므로 반환 Referencer 가 최소한 `'a` 만큼은 살아있다는 제한이 생긴다. 이렇게 파라미터에 의해 결정된 Lifetime annotation 을 기반으로 반환 Reference 의 수명을 보장해준다.

```rust
let str1 = String::from("aaaaaaaaaaaaaaaaaaaa");
let mut rst;
{
    let str2 = String::from("aaaaaaa");
    rst = longest(str1.as_str(), str2.as_str());
}
println!("{}", rst);
```

그러므로 위와 같은 코드는 컴파일 되지 않는다. `str1, str2` 의 수명의 교집합으로 반환 Reference 의 수명이 결정되었기 때문에 반환 Reference 는 최소한 inner scope 에서 수명이 끝난다. 그런데도 `rst` 를 inner scope 바깥에서 사용하고 있기 때문에 컴파일이 되지 않는다.

항상 모든 파라미터에 lifetime 을 정의해야 하는 것은 아니다. 

```rust
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

위 함수는 무조건 첫번째 파라미터를 반환한다. 그래서 lifetime `'a` 를 `x` 와 반환 Reference 에만 정의해주었다. 이로써 반환 Reference 가 `x` 와 같거나 작은 수명을 갖는다는 제한이 생긴다. 이 함수에서 `y` 는 `x` 와 반환 Reference 와 아무런 관계가 없으므로 `'a` 를 정의할 필요가 없다.

반환 Reference 에 정의된 lifetime 은 파라미터 중 하나와 연관되어야 한다. 그렇지 않으면 반환 Reference 가 함수 내부의 데이터에 대한 Reference 가 되므로 Dangling Reference 가 된다. 

결과적으로 lifetime 이란 파라미터의 lifetime 과 반환 Reference 의 lifetime 을 연결시키는 것이다. 파라미터와 반환 Reference 가 연결되면 Rust 는 memory-safe 연산을 이룰 수 있고 Dangling pointer 를 차단할 수 있는 충분한 정보를 얻을 수 있는 것이다. 

## Lifetime Annotation in Struct

Struct 는 멤버로 Reference 를 가질 수 있는데 이 경우 Reference 가 Struct 보다 일찍 죽지 않는다는 것을 보장하는 lifetime 이 정의되어야 한다. Reference 멤버가 Struct 보다 먼저 죽으면 Dangling 이 되기 때문이지.

## Lifetime Elision

이제 우리는 Reference 를 사용하는 모든 Function 과 Struct 가 Reference 의 lifetime 을 정의해야 한다는 것을 알았다. 하지만 우리는 이미 다음과 같이 lifetime 이 없는데도 Reference 를 잘 사용하는 함수를 정의했었다. 

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

사실 이 코드는 Rust 초기 버전(pre-1.0) 에서 컴파일 되지 않으며, 이때 당시 lifetime 이 명시되지 않은 모든 Reference 가 컴파일 되지 않았다. 이때 당시였다면 위 함수를 

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

와 같이 정의해야만 했다. 하지만 Rust 개발진은 똑같은 패턴의 상황에서 lifetime annotation 을 똑같이 매번 써야 한다는 것을 깨달았다. 이 상황은 예측가능 하며 결정론적 패턴이 존재했다. 그래서 이 패턴을 컴파일러에 주입시켰고 borrow checker 가 이 패턴을 맞닦드리면 lifetime annotation 이 없어도 lifetime 을 추론할 수 있도록 만들었던 것이다. 이 패턴을 lifetime elision rules 이라 한다. 만약 당신의 코드가 이 패턴에 부합하면 lifetime 을 명시하지 않아도 된다.

파라미터 Reference 의 lifetime 을 input lifetime 이라 하고 반환 Reference 의 lifetime 을 output lifetime 이라 한다.

컴파일러는 3가지 규칙으로 lifetime elision rules 을 판단한다. 이 규칙은 `fn` 블록(함수 정의) 뿐 아니라 `impl` 블록에도 적용된다.

1. (input lifetime 에 적용되는 규칙) 각각의 파라미터는 각각의 lifetime 을 갖는다. 

    가령 파라미터가 하나이면 `fn foo<'a>(x: &'a i32)` 와 같이 하나의 lifetime 을 갖고, 파라미터가 두 개 이면 `fn foo<'a, 'b>(x: &'a i32, y: &'b i32)` 와 같이 두 개의 lifetime 을 갖는다.

2. (output lifetime 에 적용되는 규칙) input lifetime 이 하나이면 그 lifetime 이 모든 output lifetime 에 할당된다.

    가령 `fn foo<'a>(x: &'a i32) -> &'a i32` 와 같다.

3. (output lifetime 에 적용되는 규칙) input lifetime 이 여러개 있고 그 중 하나가 `&self` 나 `&mut self` 라면 이것은 Method 이기 때문에 `self` 의 lifetime 이 모든 output lifetime 에 할당된다.

## Lifetime Elision Example 1

`first_word` 함수에 이 세 가지 규칙을 적용해보자. 먼저 함수가

```rust
fn first_word(s: &str) -> &str 
```

와 같이 Reference 를 입력으로 받는데도 lifetime 이 명시되어 있지 않으므로 규칙 1) 을 적용하여 

```rust
fn first_word<'a>(s: &'a str) -> &str 
```

로 만든다. input lifetime 이 하나이므로 규칙 2) 가 적용되어

```rust
fn first_word<'a>(s: &'a str) -> &'a str 
```

가 된다. 이로써 모든 Reference 가 lifetime 을 갖게 되어 프로그래머가 lifetime 을 명시하지 않아도 된다.

## Lifetime Elision Example 2

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

위 함수를 컴파일 했을 때 실패했었고,

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
```

와 같이 lifetime 을 명시했을 때 컴파일이 성공했다. 왜 실패했는지 따져보자. 먼저 규칙 1) 을 적용하면

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str {
```

가 된다. 규칙 2) 와 규칙 3) 의 조건에 부합하지 않으므로 적용되지 않는다. 규칙 1), 2), 3) 을 모두 적용했음에도 불구하고 추론되지 않은 lifetime 이 있다. 반환 Reference 의 lifetime 이 밝혀지지 않았기 때문이다. 그러므로 컴파일에 실패한 것이다.

## Lifetime Annotation in Method

lifetime 이 정의된 Struct 에 Method 를 구현하기 위해 먼저 `impl` 키워드 바로 다음에 lifetime 을 선언해주어야 한다. Method 의 Reference 는 Struct 의 필드로 정의된 Reference 이거나 독립적인 Reference 이다. 

```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}

impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }

    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {}", announcement);
        self.part
    }
}
```

함수 이름 다음에 나타나는 lifetime annotation 은 `impl` 블록 다음에 나오는 lifetime annotation 으로 대체된다.

`level` 에는 규칙 1) 이 적용되어 모든 Reference 의 lifetime 을 결정할 수 있다. `announce_and_return_part` 에는 규칙 1) 과 3) 이 적용되어 모든 lifetime 을 결정할 수 있다.

## Static Lifetime

Static Lifetime 인 `'static` 가 있는 Reference 는 프로그램이 실행되는 전체 시간동안 살아있다는 것을 뜻하는 Reference 이다.

모든 string literal 은 `'static` 을 가진다. 따라서 

```rust
let s: &'static str = "I have a static lifetime.";
```

와 같이 정의할 수 있다.

> 근데 `'static` 에 대해서 잘 이해가 안된다. 그리고 string literal 이 `'static` 이라는 것도 이해가 잘 안되고. 

에러 메시지 같은 것들에 `'static` 을 사용하고 싶을 수도 있지만, `'static` 을 사용하기 전에 Reference 가 실제로 프로그램 전체 수명 동안 살아있는지 확인해야 하고, 그것이 가능하다고 해도 당신이 Reference 가 그렇게 길게 살아있길 원하는지 고려해봐라.

## Example (Generic+Trait+Lifetime)

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

위 함수는 Generic, Trait, Lifetime 이 모두 포함된 올인원 함수이다. 

---

# Automated Tests

Test 는 버그가 존재한다는 것을 효과적으로 밝힐 수 있지만, 버그가 존재하지 않는다는 것을 보이는데에는 힘을 발휘하지 못한다. 하지만 이것은 우리가 Test 를 하지 않아도 된다는 것을 의미하지 않는다.

프로그램의 **Correctness** 란 코드가 **우리의 의도대로 행동한다** 는 것이다. Rust 는 Correctness 를 고려하며 설계했지만 이것은 복잡한 개념이었고 증명하기가 쉽지 않았다. Rust 의 타입 시스템이 Correctness 의 짐을 많이 지고 있지만 이것이 Incorrectness 를 모두 밝힐 수는 없었다. 따라서 Rust 는 Automated test 를 제공하기로 했다. 

가령 두 숫자를 더하여 반환하는 `add_two` 함수를 만들었다고 하자. 이 함수는 Rust 의 타입 시스템과 borrow checker 로 올바른 자료형과 올바른 Reference 만을 받아들일 것이다. 하지만 Rust 는 **이 함수가 정말로 우리의 의도대로 행동한다** 는 것은 보장해주지 않는다. 그러므로 이 시점에서 Test 가 필요하다. 

## Test 코드 작성

Test 코드란 non-test 코드가 **우리가 의도한 대로 행동한다** 는 것을 검증하는 코드이다. Test 코드는 보통 다음 3단계로 행동한다.

1. 필요한 데이터와 상태를 준비한다. 

2. non-test 코드에 대한 test 를 진행한다. 

3. 결과를 assert 한다. 

## Test Function

Test 함수란 `test` Attribute 가 붙혀진 함수이다. Attribute 란 Rust 코드에 대한 metadata 이다. 가령 우리는 이미 

```rust
#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
}
```

와 같은 Attribute 를 사용했었다. 이와 같이 함수를 Test 함수로 만들기 위하여 `#[test]` Attribute 를 붙이면 된다. 그리고 `test` Attribute 가 붙은 함수를 실행하고 검증하기 위하여 `cargo test` 명령어를 실행하면 된다. 

`#[test]` 함수들을 모듈로 묶기 위해서는 `[cfg(test)]` Attribute 가 붙은 `mod` 에 Test 함수를 정의하면 된다. 

## Testing 방법

Test 함수에 `assert!`, `assert_eq!`, `assert_ne!` 로 non-test 코드가 의도한대로 행동하는지 확인한다. 정상적인 값이 반환되면 아무일 없이 넘어가고 비정상적인 값이 반환되면 `panic!` 을 호출하게 되는데 Test 함수는 이 `panic!` 을 catch 해서 Test 결과로 보고하는 것이다.

`assert_ne!` 는 보통 함수의 반환값이 명확하지는 않지만 이것만큼은 분명히 아니라고 확신할 때 사용된다. 

`assert_eq!` 로 기댓값을 비교하기 위해서는 `PartialEq` Trait 가 정의되어 있어야 한다. 모든 primitive type 과 대부분의 std 가 제공하는 타입은 `PartialEq` 를 정의했지만, 당신이 만든 Struct 나 Enum 을 특정 기댓값과 assert 하고 싶다면 `PartialEq` 을 정의해야 할 것이다. 또한 assertion 이 실패했을 때 `Debug` Trait 가 정의되어 있어야지 에러 메시지를 출력할 수 있기 때문에 `Debug` Trait 도 정의해야 할 것이다.

그런데 `PartialEq` 와 `Debug` Trait 는 derivable traite 이기 때문에 당신이 만든 Struct 와 Enum 정의 위에 단지

```rust
#[derive(PartialEq, Debug)]
```

를 추가하면 된다. 

## Custom Failure Message

assertion 진행 중 Test 가 실패하면 단지 "assertion 에 실패했다" 라는 식의 메시지밖에 볼 수 없다. 만약 Test 개수가 수백개가 넘어가면 각각의 Test 의 의미가 잘 생각나지 않을 때도 있다. 그렇기에 Test 를 만드는 시점에서 Test 가 실패했을 때 단순히 "assertion 에 실패했다" 는 메시지가 아니라 왜 Test 가 실패했고 실패한 중요한 원인이 되는 데이터를 출력해주는 것이 중요하다. 

`assert!` 두번째 파라미터에 format string 을 넣고 세번째 파라미터부터 `{}` 에 들어갈 데이터를 넣을 수 있다. 이런 식으로 Custom Failure Message 를 제작해둘 수 있다.

## panic test

코드가 의도한대로 행동한다는 것을 Test 하는 것도 중요하지만, 비정상적인 입력을 받았을 때 `panic` 을 일으키는 것을 확인하는 것도 중요하다. 이를 위해 `should_panic` attribute 를 Test 함수에 붙이면 된다. 

```rust
#[test]
#[should_panic]
fn test_function(){
    // panicable code
}
```

근데 non-test 코드 중에서 여러가지의 `panic` 이 있을 수 있다.  `should_panic` test 가 정확하게 우리가 원하는 `panic` 이 일어났다는 보장을 얻기 위하여 `should_panic` 의 `expected` 파라미터에 `panic` 메시지가 반드시 포함해야 할 failure message 명시할 수 있다. 

## Result<T, E> Test

Test 함수에서 Test 에 성공했다 실패했다를 `panic` 이 일어났냐 안일어났냐로 판단한다고 했다. 하지만 이 기준을 `Result<T, E>` 로 바꿀 수도 있다. 다음과 같이 Test 에 성공하면 `Ok` 를 반환하고 실패하면 `Err` 를 반환하면 된다. 

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```

# Controlling Test 

## thread-safe test

Test 가 여러개면 Rust 는 default 로 멀티 스레드로 Test 함수를 검증한다. 따라서 당신은 Test 들이 서로 의존적이지 않고 공유되는 상태나 환경이 없도록 thread-safe 하게 만들어야 한다. 

가령 파일을 만들고 내용을 작성하는 Test 들이 여러개일 경우 내용이 엉키겠지. 만약 Test 들을 thread-safe 하게 만들기가 불가능하다면 `cargo test -- --test=threads=1` 이라고 실행하면 된다.

## show output of test

Rust 는 default 로 실패한 Test 의 stdout 을 보여준다. 하지만 성공한 Test 의 출력도 보고 싶다면 `cargo test -- --show-output` 이라고 하면 된다. 

## Running subset of Test

Test 가 엄청 많아지면 그것들을 매번 다 Test 하는 것이 비효율적일 때도 있다. `cargo test <TEST FUNCTION>` 이라고 하면 원하는 Test 함수만 test 할 수 있어.

하지만 여러 함수 이름을 전달할 수는 없지. 그 대신 패턴을 전달할 수 있어. 가령 `cargo test add` 라고 하면 `add` 가 포함된 Test 함수가 test 되는거야.

## Ignore some Tests

몇몇 Test 들은 시간 소모가 매우 심하다. 이런 Tests 들을 `cargo test` 를 실행했을 때 무시하기 위하여 `#[ignore]` attribute 를 붙힐 수 있다.

```rust
#[test]
#[ignore]
fn expensive_test() {
    // code that takes an hour to run
}
```

`ignore` attribute 가 붙은 Test 까지 다 테스트하기 위해서는 `cargo test -- --ignored` 를 실행하면 된다. 

# Test Organization

Test 라는 개념은 커뮤니티마다 다양하게 정의된다. Rust 커뮤니티는 Test 를 크게 unit test 와 integration test 로 분류한다.

Unit test 란 특정 코드를 부분적으로, 독립적으로, 소규모로, private 인터페이스도 테스트하는 것이다. Integration test 란 전체 코드를, 종속적으로, 대규모로, public 인터페이스만을 사용하여 다 테스트 하는 것이다. Rust 커뮤니티는 이 두 Test 를 다 시행하는 것을 중요하게 생각한다.

## Unit test

unit test 의 convention 은 unit test 를 `src` 디렉토리의 각각의 파일안에 정의하고, `tests` 라는 Module 에 Test 함수를 정의하는 것이다. 이 `tests` Module 에는 `#[cfg(test)]` 라는 attribute 가 정의되어야 한다. 

## Test Module and #[cfg(test)]

`#[cfg(test)]` 는 Rust 에게 이 코드는 `cargo test` 를 실행했을 때만 컴파일하고 실행하라고 말해주는 attribute 이다. 그래서 이 attribute 는 컴파일 시간을 절약해주고 릴리즈 버전의 바이너리에 테스트 코드가 포함되지 않게 해준다. 

Integration test 에 대해서도 살펴볼텐데 이 테스트는 non-test 코드와 같은 디렉토리에 저장되지 않기 때문에 `#[cfg(test)]` 를 쓰지 않아도 되고, Unit test 는 non-test 코드와 같은 파일에 저장되므로 `#[cfg(test)]` 가 필요하다. 

`#[cfg(test)]` 의 `cfg` 는 configuration 을 뜻하고 Rust 가 괄호 안에 있는 item 이 configuration 에 설정되도록 만든다. 이 경우 configuration 옵션에 `test` 가 추가되는 것이다. 

## Integration test

Integration test 는 당신의 라이브러리에서 완전히 외부에 선언되고, 그러므로 public API 만 사용하여 테스트를 한다. 이 Test 의 목적은 라이브러리가 잘 작동하는지 전체적으로 확인하는 것이다. 이렇게 전체 코드가 서로 잘 작동하는지 확인하는 이유는 Unit test 로 개인적으로 잘 작동하는 것이 확인된 코드들이 integrated 되었을 때 오작동을 하는 경우도 있기 때문이다.

Integration test 를 위하여 먼저 패키지 root 에 `tests` 라는 디렉토리를 만들어라.

## tests Directory

Cargo 는 `tests` 디렉토리에 Integration test 가 존재한다는 것을 안다. Cargo 는 각각의 파일들을 독립적인 crate 로 컴파일한다. 따라서 Integration test 에 `#[cfg(test)]` 가 필요 없고 `use <PACKAGE>;` 선언이 필요하다.

## Submodules in Integration test

`tests` 디렉토리의 파일들이 각각 독립적인 crate 로 컴파일 되므로 대부분의 test 함수에서 공통적으로 필요한 파일들을 가령 `tests/common.rs` 에 모아둘 수 있다. 이 파일에 아래와 같이 대부분의 test 함수가 호출해야 하는 함수를 정의 했다고 하자. 

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

이 함수는 test 함수가 아니고 `tests/common.rs` 자체에 test 코드가 없는데도 `cargo test` 를 실행하면 `tests/common.rs` 의 test 항목이 발생한다. 이것을 피하기 위하여 `tests/common.rs` 대신 `tests/common/mod.rs` 를 만들 수 있다. 이렇게 하면 Rust 가 `common` 모듈을 Integration test 로 여기지 않게 된다. 

일반적으로 `tests` 에서 디렉토리를 또 생성하고 그 디렉토리 밑에 파일이 생성되면 Cargo 가 그것을 non-test 코드로 여긴다. 

이제 아래와 같이 다른 test 코드에서 `tests/common/mod.rs` 의 코드를 가져다가 쓸 수 있다.

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

## Integration test for Binary Crate

패키지에 `src/lib.rs` 가 없고 `src/main.rs` 만 있다면 `tests` 디렉토리에 Integration test 를 정의할 수 없다. 라이브러리 crate 만 Integration test 로 테스트할 수 있다. 이는 바이너리 crate 는 unit test 만 할 수 있다는 것이다.

Rust 가 `src/main.rs` 의 integration test 를 제한하는 이유는 `src/main.rs` 가 `src/lib.rs` 에 있는 코드를 호출하는 적은 양의 코드만을 지니고 있다고 가정하기 때문이다. 중요한 코드와 로직은 모두 라이브러리 crate 에 정의되어 있으므로 라이브러리 crate 의 Integration test 가 된다면 `src/main.rs` 의 Integration test 는 불필요하다는 것이다. 

> 근데 그래도 굳이 제한을 했어야 했을까? 그럴 필요까지는 없었는데 Rust 커뮤니티가 원한 것은 Rust 개발자가 `src/main.rs` 에는 오로지 Drive 코드만 넣고 중요한 로직과 기능은 `src/lib.rs` 에 넣는 것이라고 생각된다. 그래서 그것을 강제한 것이지.

---

# derive attribute

어떤 Struct 나 Enum 에 `derive` attribute 가 추가되면 trait 의 default implementation 이 해당 데이터 타입에 추가된다. 

---

# I/O Project

`grep` 프로그램을 만들어보자.  

## First Try

초안은 다음과 같다.

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let filename = &args[2];

    println!("Search: {}", query);
    println!("In file: {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went worng reading the file");

    println!("With text:\n{}", contents);
}
```

이 초안에는 다음과 같은 문제가 있다. 

1. 한 함수가 parse 를 하고 read 를 하는 등 2가지 기능을 한다. 이렇게 다양한 기능을 한 함수에 넣으면 테스트와 수정이 점점 더 힘들어진다.

2. `query` 와 `filename` 이 configuration variable 로 저장되었다. 변수가 많아질수록 각각의 변수들의 목적이 기억나지 않을 것이다. 이를 위해 configuration variable 을 하나의 Struct 로 묶자. 일반적으로 함께 쓰이는 변수들은 다 Struct 로 묶어야 한다.

3. 파일을 읽을 때 `expect` 로 하나의 에러 메시지를 출력해주지만, 파일 읽기에서 발생할 수 있는 에러는 매우 다양하다. 그래서 사용자에게 충분한 정보를 줄 수 없다.

4. `expect` 로 에러를 처리하지만 모든 에러 핸들링 코드가 한 장소에 정의되었다면 관리하기가 훨씬 편하다.

## Separation of Concerns

`main` 함수에 여러 기능을 집어넣는 일이 흔해지자 Rust 커뮤니티는 `main` 함수의 모듈성을 위하여 다음과 같은 가이드라인을 만들었다. 

- 프로그램을 `main.rs` 와 `lib.rs` 로 분리하되 프로그램의 로직은 모두 `lib.rs` 에 넣어라. 

- CLI 파싱 로직이 간단하다면 `main.rs` 에 있어도 된다. 

- CLI 파싱 로직이 복잡해지면 `main.rs` 에서 분리하여 `lib.rs` 에 넣어라.

이 과정이 끝나면 `main` 함수가 할 일은 다음과 같이 축약된다. 

- CLI 파싱 로직을 호출한다. 

- configuration 을 setup 한다.

- `lib.rs` 의 `run` 함수를 호출한다. 

- `run` 이 에러를 반환하면 에러를 처리한다. 

이 패턴은 `main.rs` 가 프로그램의 실행을 관리하고, `lib.rs` 가 프로그램의 로직을 관리한다는 철학을 기반으로 만들어졌다. 

## Extracting the Argument Parser

그러면 먼저 CLI 파싱 로직을 다음과 같이 분리하자.

```rust
fn main() {
    let args: Vec<String> = env::args().collect();
    let (query, filename) = parse_config(&args);
    // --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let filename = &args[2];

    (query, filename)
}
```

## Grouping Values

이제 configuration value 를 다음과 같이 그룹핑해보자. 

```rust
fn main() {
    let args: Vec<String> = env::args().collect();
    let config = parse_config(&args);

    println!("Searching for {}", config.query);
    println!("In file {}", config.filename);
    // --snip--
}

struct Config {
    query: String,
    filename: String,
}

fn parse_config(args: &[String]) -> Config {
    let query = args[1].clone();
    let filename = args[2].clone();

    Config { query, filename }
}
```

`Config` 에 String 을 Clone 하여 Ownership 을 부여하고 있는데 다른 다양한 방법으로 더 효율적으로 String 을 다룰 수 있다. Clone 은 런타임 비용이 많이 들어가기 때문에 최적화가 필요한 프로그램에서 사용되지 않는다. 지금은 아주 작은 프로그램이므로 Clone 을 사용해도 상관없다.

효율적이 방법에 대해서는 챕터 13 의 "함수형 언어: Iterator 와 Closure" 에서 더 다뤄본다. 

## Creating constructor for Config

`parse_config` 함수의 목적은 `Config` 인스턴스를 생성하는 것이었다. 이 함수를 좀 더 Rustacean 하게 만들기 위하여, 그리고 다른 곳에서 매번 인스턴스를 생성하는 함수를 만들어야 하는 것을 방지하기 위하여, `Config::new` 라는 Method 를 다음과 같이 만들자. 

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args);
    // --snip--
}

// --snip--

impl Config {
    fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let filename = args[2].clone();

        Config { query, filename }
    }
}
```

## Improving Error Handling

`new` 함수에서 에러가 발생하면 단지 `index out of bounds: the len is 1 but the index is 1` 라는 메시지만 나오는데 이는 별 도움이 안된다. 그러니까 다음과 같이 에러 메시지를 상황에 따라 구체화시켜주자.

```rust
    // --snip--
    fn new(args: &[String]) -> Config {
        if args.len() < 3 {
            panic!("not enough arguments");
        }
        // --snip--
```

## Returning a Result from new Instead of Calling panic!

하지만 위와 같이 `panic` 시켜버리는 것은 caller 에게 에러를 처리할 기회 주지 않는 것이다. 그러니까 다음과 같이 `Result<T, E>` 를 반환하여 Error propagating 을 해주자. 

```rust
impl Config {
    fn new(args: &[String]) -> Result<Config, &str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let filename = args[2].clone();

        Ok(Config { query, filename })
    }
}
```

## Calling Config::new and Handling Errors

그러면 `main` 에서 에러를 처리할 기회를 얻고, 에러 코드로 프로세스를 종료시켜주는 등 사용자에게 더 많은 정보를 제공해줄 수 있다.

```rust
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    // --snip--
```

## Extracting Logic from main 

이제 CLI 파싱 로직을 고쳐보았으니 configuration 세팅과 error 핸들링을 제외한 `main` 함수의 로직을 `run` 함수로 옮기자. 

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.filename)
        .expect("Something went wrong reading the file");

    println!("With text:\n{}", contents);
}
```

## Returning Errors from the run Function

이제 `run` 또한 error propagating 을 하게 만들어서 `main` 이 `run` 의 에러를 처리할 수 있도록 하자.

```rust
use std::error::Error;

// --snip--

fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;

    println!("With text:\n{}", contents);

    Ok(())
}
```

Error 타입으로 `Box<dyn Error>` 라는 trait object 를 반환하고 있는데 이는 챕터 17 의 OOP 에서 배우게 될 것이다. 지금은 이것이 단지 `Error` trait 를 구현한 타입이라고 이해하면 된다. 

즉 특정 데이터 타입을 명시해주지 않겠다는 것인데 이로써 여러 에러 타입을 일반적으로 다룰 수 있게 된다. `dyn` 키워드는 dynamic 의 줄임말이다.

그리고 `expect` 를 `?` 로 바꿔주었다. 성공시에는 그냥 `Ok(())` 를 반환하는데 이는 unit type `()` 를 `Ok` 타입으로 wrap 한 것이다. 이는 `run` 함수를 side effect 를 위하여 호출하는 것이고, 반환값이 필요하지 않는다는 것을 뜻한다.  

## Handling Errors Returned from run in main

이제 다음과 같이 `run` 이 반환하는 `Result<T, E>` 를 `main` 에서 처리해줄 차례이다. 

```rust
fn main() {
    // --snip--
    if let Err(e) = run(config) {
        println!("Application error: {}", e);

        process::exit(1);
    }
}
```

`unwrap_or_else` 가 아닌 `if let` 을 사용하는 것은 반환값이 없으니까 `match` 의 경우 중 `Err` 의 경우만 처리해주겠다는 것이다. 

## Splitting Code into a Library Crate

이제 다음과 같은 로직을 다루는 코드를 `src/lib.rs` 로 옮길 차례이다.

- `run` 함수

- 관련 `use` 선언

- `Config` Struct

- `Config` Struct 의 Method(`Config::new`)

다음과 같이 `src/lib.rs` 로 로직 코드를 옮겼고 외부에서 사용할 수 있도록 `pub` 키워드도 추가해준다.

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub filename: String,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &str> {
        // --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    // --snip--
}
```

이제 이 코드를 `src/main.rs` 에 가져와서 사용하자. 

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    // --snip--
    if let Err(e) = minigrep::run(config) {
        // --snip--
    }
}
```

# Developing the Library’s Functionality with Test-Driven Development

전체적인 코드 작성은 끝났다. 이제 할 일은 TDD 를 통해 라이브러리를 테스트하며 확장하는 것이다. TDD 는 다음과 같이 이루어진다. 

1. 실패하는 Test 를 작성하여 당신의 의도대로 프로그램이 실패하는지 확인하라.

2. Test 를 패스하는 코드를 작성하라.

3. 그 Test 가 통과하는지 확인하라. 

4. 1단계부터 다시 반복하라.

이 과정은 소프트웨어를 만드는 방법론 중 하나이지만, TDD 는 안정성있는 코드를 만들 수 있도록 도와준다. 우리는 이 TDD 를 통해 최종적으로 `search` 함수를 만들 것이다.

## 1) Failing Test

`tests` Module 안에 Test 함수를 먼저 짜고 우리가 원하는 `search` 함수의 행동의 예시를 명시한다. 

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(vec!["safe, fast, productive."], search(query, contents));
    }
}
```

이 Test 함수는 `search` 함수가 `"duct"` 을 찾고 이것을 포함하는 라인들을 반환하는 것을 명시한다. 하지만 아직 `search` 함수의 정의조차 없기에 컴파일도 할 수 없다.

그러니 일단 컴파일이 되도록 `search` 함수를 정의해준다.

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    vec![]
}
```

여기서 Lifetime `'a` 를 사용했는데 Lifetime 은 파라미터의 lifetimei 과 반환 lifetime 을 연결해준다고 했었다. 이 경우 반환되는 벡터가 포함하는 String slice 가 `contents` 파라미터의 referencing slice 이므로 같은 Lifetime 으로 연결해줬다. 

이는 Rust 에게 `search` 함수가 반환하는 데이터가 `search` 함수로 들어오는 `contents` 라는 데이터만큼 살아 있음을 보장해준다. Lifetime 을 뺀다면 Rust 가 lifetime elision 을 해도 Lifetime 을 유추할 수 없어서 컴파일 에러가 발생한다. 

## 2) Writing Code to Pass the Test

1) 단계의 Test 함수는 실패한다. 이제 `search` 함수를 고쳐서 Test 에 통과하도록 만들자.

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

`lines` 함수를 사용하여 라인을 반환해주는 Iterator 를 생성하고 `query` 가 있는지 확인하여 있으면 리스트에 추가해주면 끝난다. Iterator 에 대해서 챕터 13 함수형 언어에서 다룬다. 

이렇게 짜면 테스트에 통과한다. 

## Using the search Function in the run Function

이렇게 TDD 로 `search` 함수를 만들어보았다. 그러면 `search` 를 `run` 에 포함시키자. 

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;

    for line in search(&config.query, &contents) {
        println!("{}", line);
    }

    Ok(())
}
```


이로써 grep 프로그램을 minimal 하게 만들어보았다. 이렇게 minigrep 프로젝트는 완성을 했지만 환경변수 사용과 에러 스트림 출력 기능이 추가되면 더 개선시킬 수 있다.

# Working with Environment Variables

minigrep 프로그램을 사용할 때 옵션을 유저가 지정하게 할 수도 있지만 환경변수로 저장하게 하면 더 편하게 사용할 수 있다. 

여기에서는 간단하게 case-insensitive 옵션을 환경변수로 지정하는 방법을 살펴보자. 

이를 위하여 먼저 TDD 로 `search_case_insensitive` 함수를 만들자.

## 1) 테스트 함수 작성

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        // --snip--
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

## 2) 테스트에 통과하도록 코드 구현

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.to_lowercase().contains(&query) {
            results.push(line);
        }
    }

    results
}
```

일단 `to_lowercase` 함수로 `query` 를 소문자로 만든다. 이때 `query` 는 `&str` 에서 `String` 이 된다. `to_lowercase` 함수는 Reference 가 아닌 아예 새로운 데이터를 만들기 때문이다. 

그리고 `line` 에 `query` 가 있는지 체크하기 전에 `to_lowercase` 로 소문자로 만든 후 체크한다.

## 3) 구현 코드를 `run` 에 추가

```rust
pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

// --snip--

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;

    let results = if config.case_sensitive {
        search(&config.query, &contents)
    } else {
        search_case_insensitive(&config.query, &contents)
    };

    for line in results {
        println!("{}", line);
    }

    Ok(())
}
```

`Config` Struct 에 `case_sensitive` 변수를 추가하여 구분하도록 한다. 

## 환경변수 

이렇게 TDD 로 `search_case_insensitive` 를 만들어 보았다. 

이제 환경변수로써 `case_sensitive` 를 설정할 수 있도록 만들자. 

```rust
use std::env;
// --snip--

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let filename = args[2].clone();

        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

        Ok(Config {
            query,
            filename,
            case_sensitive,
        })
    }
}
```

`env::var` 로 환경변수의 값을 가져올 수 있다. 환경변수가 세팅되어 있으면 `env::var` 함수는 `Ok` 를 반환하고 아니면 `Err` 를 반환한다. `is_err` 함수는 `Ok` 라면 `true` 를, `Err` 라면 `false` 를 반환한다.

PowerShell 에서는 

```powershell
PS> $Env:CASE_INSENSITIVE=1; cargo run to poem.txt
```

로 실행할 수 있고 bash-like 에서는 

```shell
$ CASE_INSENSITIVE=1 cargo run to poem.txt
```

로 실행할 수 있다. 

# 표준 에러 스트림 

stdout 과 stderr 를 구분하여 에러들은 stderr 로 출력하는 것은 사용자가 에러 메시지를 구분하기 쉽게 해준다. 

minigrep 에서 에러 메시지들은 모두 stderr 로 출력해주자. Rust 표준 라이브러리는 `eprintln!` 매크로를 제공하여 에러 스트림으로 출력할 수 있게 해준다. 

```rust
fn main() {
    // --snip--
    let config = Config::new(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {}", e);
    // --snip--
```

---

# Functional Language Features: Iterators and Closures

이 장에서 다음과 같은 Rust 의 함수형 언어 특징을 살펴본다.

- Closures

- Iterators

이 두 특징으로 minigrep 을 개선시켜볼 것이다. 마지막으로 이 두 특징의 성능을 벤치마킹해볼 거야.

# Closures

Rust 의 Closure 는 변수나 파라미터로 다른 함수에 전달 할 수 있는 anonymous function 이다. Closure 는 Function 과 달리 그것이 정의된 scope 의 변수를 사용할 수 있다. 

```rust
fn simulated_expensive_calculation(intensity: u32) -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    intensity
}

fn generate_workout(intensity: u32, random_number: u32) {
    if intensity < 25 {
        println!(
            "Today, do {} pushups!",
            simulated_expensive_calculation(intensity)
        );
        println!(
            "Next, do {} situps!",
            simulated_expensive_calculation(intensity)
        );
    } else {
        if random_number == 3 {
            println!("Take a break today! Remember to stay hydrated!");
        } else {
            println!(
                "Today, run for {} minutes!",
                simulated_expensive_calculation(intensity)
            );
        }
    }
}
```

`generate_workout` 함수는 `simulated_expensive_calculation` 함수를 여러번 호출하고 있다. 이 코드를 추상화시켜보자. 

```rust
fn generate_workout(intensity: u32, random_number: u32) {
    let expensive_result = simulated_expensive_calculation(intensity);

    if intensity < 25 {
        println!("Today, do {} pushups!", expensive_result);
        println!("Next, do {} situps!", expensive_result);
    } else {
        if random_number == 3 {
            println!("Take a break today! Remember to stay hydrated!");
        } else {
            println!("Today, run for {} minutes!", expensive_result);
        }
    }
}
```

먼저 위와 같이 `simulated_expensive_calculation` 함수가 여러번 호출되는 것을 추출하여 하나의 변수에 저장해두는 방법이 있다. 하지만 세 번째 `if` 문에서는 이 결과값이 필요 없다. 

`simulated_expensive_calculation` 의 결과값을 변수에 저장해두는 대신 Closure 에 `simulated_expensive_calculation` 함수 전체를 저장해줄 수 있다. 

```rust
let expensive_closure = |num| {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

Closure 는 위와 같이 `=` 다음부터 정의되어 파이프 `|` 의 쌍으로 시작한다. 이 안에 파라미터를 정의하게 되는데, 위의 경우 `num` 이라는 파라미터가 있다. 

만약 Closure 의 로직이 단일 expression 이라면 중괄호 `{ }` 가 필요없지만 여러 statement 들이 필요하면 `{ }` 로 묶어 줄 수 있다. 이를 기반으로 다음과 같이 코드를 고쳐보자.

```rust
fn generate_workout(intensity: u32, random_number: u32) {
    let expensive_closure = |num| {
        println!("calculating slowly...");
        thread::sleep(Duration::from_secs(2));
        num
    };

    if intensity < 25 {
        println!("Today, do {} pushups!", expensive_closure(intensity));
        println!("Next, do {} situps!", expensive_closure(intensity));
    } else {
        if random_number == 3 {
            println!("Take a break today! Remember to stay hydrated!");
        } else {
            println!(
                "Today, run for {} minutes!",
                expensive_closure(intensity)
            );
        }
    }
}
```

하지만 이렇게 하면 여전히 첫번째 `if` 문에서 Closure 를 여러번 호출하게 된다. 우리는 이 문제를 그냥 `if` 블록에서 변수를 하나 선언하여 Closure 의 결과값을 저장하는 것으로 해결하자. 

## Closure Type Inference and Annotation

Closure 는 Function 과 달리 명시적인 파라미터 데이터 타입 선언이 없다. 이는 Function 이 외부 인터페이스를 가지므로 모든 사용자가 파라미터 데이터 타입에 대한 합의를 해야 하는 것과 달리 Closure 는 외부 인터페이스를 제공하지 않기 때문이다. 

즉, Closure 는 Function 과 달리 내부 인터페이스에서 사용되고 Function 이 일반적인 맥락에서 사용되는 것과 달리 Closure 는 국소적인 맥락에서 사용된다. 

따라서 rustc 가 Closure 의 파라미터 데이터 타입을 쉽게 유추할 수 있으므로 Rust 는 개발자에게 Closure 의 파라미터 데이터 타입을 항상 명시하도록 하는 것은 비효율적이라고 결론을 내렸다. 

그러나 물론 Closure 의 파라미터와 반환형에 데이터 타입을 선언하는 것이 금지되는 것은 아니다. 다음과 같이 할 수 있다. 

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

다음 네 가지 코드는 모두 같은 기능을 한다.

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

하지만 rustc 는 Closure 의 파라미터와 반환 타입을 반드시 한 데이터 타입으로 유추한다. 가령 다음의 코드는 에러가 발생하는데 Closure 의 `x` 의 타입이 `String` 으로 유추되었는데 `5` 가 전달되었기 때문이다. 

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

## Storing Closures Using Generic Parameters and the Fn Traits

이제 처음의 예시로 다시 되돌아가보면, 시간이 많이 필요한 연산 결과를 `if` 블록 앞에 저장해두는 방법도 있었고, 꼭 필요할 때만 연산하는 방법도 있었다. 하지만 다른 곳에서 해당 연산이 또 필요하다면 Closure 를 다시 호출해야 한다. 

이 문제를 해결하기 위해 Closure 를 멤버로 갖는 Struct 를 만들고 이 Struct 가 Closure 의 결과값도 저장하게 할 수 있다. 즉, 이 Struct 는 Closure 가 필요할 때만 호출하고 이미 호출되었다면 Caching 된 결과값을 반환만 해준다는 것이다.(memoization or lazy evaluation)

Struct 에 Closure 를 만들기 위해서는 Closure 의 데이터 타입이 명시되어야 한다. 이때 각각의 Struct 인스턴스의 Closure 인스턴스는 설령 같은 signature 를 갖고 있더라도 서로 구별되는 유일한 타입이 된다. 

모든 Closure 는 `Fn`, `FnMut`, `FnOnce` Trait 중 최소한 하나를 구현한다. `Fn` Trait 를 사용하는 Closure 를 갖는 Struct 예시를 들어보자. 

```rust
struct Cacher<T>
where
    T: Fn(u32) -> u32,
{
    calculation: T,
    value: Option<u32>,
}
```

Trait bound `T` 는 파라미터로 `u32` 를 받고 `u32` 를 반환하는, `Fn` trait 를 사용하는 Closure 이다. 

> 근데 Closure 를 Struct 멤버로 갖는 거랑 Trait 를 Method 로 구현한 Struct 랑 무슨 차이지.

```rust
impl<T> Cacher<T>
where
    T: Fn(u32) -> u32,
{
    fn new(calculation: T) -> Cacher<T> {
        Cacher {
            calculation,
            value: None,
        }
    }

    fn value(&mut self, arg: u32) -> u32 {
        match self.value {
            Some(v) => v,
            None => {
                let v = (self.calculation)(arg);
                self.value = Some(v);
                v
            }
        }
    }
}
```

이 Struct 를 바탕으로 위와 같이 `new` Method 와 `value` Method 를 정의하여 Closure 가 한번만 실행되게끔 만든다. 

```rust
fn generate_workout(intensity: u32, random_number: u32) {
    let mut expensive_result = Cacher::new(|num| {
        println!("calculating slowly...");
        thread::sleep(Duration::from_secs(2));
        num
    });

    if intensity < 25 {
        println!("Today, do {} pushups!", expensive_result.value(intensity));
        println!("Next, do {} situps!", expensive_result.value(intensity));
    } else {
        if random_number == 3 {
            println!("Take a break today! Remember to stay hydrated!");
        } else {
            println!(
                "Today, run for {} minutes!",
                expensive_result.value(intensity)
            );
        }
    }
}
```

이를 기반으로 위와 같이 Closure 를 변수에 저장하는 것이 아니라 Struct 를 변수에 저장하여 Caching 기법으로 Closure 가 여러번 실행되는 것을 방지할 수 있다. 

## Limitations of the Cacher Implementation

하지만 위와 같이 Cacher 를 구현하면 한번 저장된 데이터가 절대로 바뀌지 않는다는 단점이 있다. 그러므로 `value` 필드를 단일 값이 아니라 arg 를 키로 갖는 hash map 으로 정의할 수도 있다. 

또 다른 문제는 위의 Cacher 는 오직 `u32` 타입만 받고 반환한다는 것이다. 이를 해결하기 위해서는 Cacher 에 Generic 을 적용해야 한다. 

hash map 과 Generic 를 적용한 코드는 Official Documentation 에 없어서 다음과 같이 만들어보았다. 

```rust
use std::collections::HashMap;
use std::hash::Hash;

struct Cacher<T, U>
where
    T: Fn(U) -> U,
    U: Copy + Hash + Eq
{
    calculation: T,
    value: HashMap<U, U>,
}

impl<T, U> Cacher<T, U>
where
    T: Fn(U) -> U,
    U: Copy + Hash + Eq
{
    fn new(calculation: T) -> Cacher<T, U> {
        Cacher {
            calculation,
            value: HashMap::new(),
        }
    }

    fn value(&mut self, arg: U) -> U {
        match self.value.get(&arg) {
            Some(&v) => v,
            None => {
                let v = (self.calculation)(arg);
                self.value.insert(arg, v);
                v
            }
        }
    }
}

#[test]
fn generate_workout() {
    let mut expensive_result = Cacher::new(|num| {
        println!("Executing Closure");
        num
    });

    println!("{} => {}", 1, expensive_result.value(1));
    println!("{} => {}", 1, expensive_result.value(1));
    println!("{} => {}", 2, expensive_result.value(2));
    println!("{} => {}", 3, expensive_result.value(3));
    println!("{} => {}", 3, expensive_result.value(3));
    println!("{} => {}", 4, expensive_result.value(4));
}
```

## Capturing the Environment with Closures

지금까지 Closure 를 inline anonymous 함수처럼 사용해왔지만 Closure 는 함수에는 없는 기능을 갖고 있다. Closure 는 자신이 정의된 scope 에 있는 변수를 Capture 하여 접근할 수 있다. 

Closure 는 scope 의 변수들을 Capture 할 때 그것들을 저장하기 위하여 메모리를 사용한다. 하지만 이 메모리 사용은 우리가 scope 에 있는 변수들을 사용하지 않을 때 오버헤드가 된다. 그에비해 Inner Function 은 scope 의 변수들을 Capture 하지 않기 때문에 이런 오버헤드가 발생하지 않는다. 

Closure 는 세 가지 방식으로 Capture 를 한다. 1) taking ownership, 2) borrowing mutably, 3) borrowing immutably 이 세 가지 방식은 다음과 같은 trait 로 인코딩 되었다. 

1. `FnOnce` Trait : scope 의 변수들의 Ownership 을 가져와서 Closure 로 Move 한다. Once 라는 말은 같은 변수의 Ownership 을 두 번이상 가져올 수 없기 때문이다. 

2. `FnMut` Trait : scope 의 변수들의 Reference 를 mutably 하게 가져온다.

3. `Fn` Trait : scope 의 변수들의 Reference 를 immutably 하게 가져온다.

당신이 Closure 를 사용하면 Rust 가 어떤 Trait 가 사용되어야 한지 infer 해준다.

만약 Closure 가 변수의 Ownership 을 강제로 가져오게 하고 싶다면 Closure 정의 앞에 `move` 키워드를 넣으면 된다. 이 기법은 thread 에서 많이 사용되는데, Closure 를 새로운 thread 에 보낼 때 데이터를 Move 시킴으로써 새로운 thread 가 owner 가 되게 할 수 있기 때문이다. 

`move` Closure 도 `Fn`, `FnMut` 를 구현한다. 왜냐하면 세가지 Fn Trait 들은 Closure 가 무엇을 Capture 할지 정하는 것이고, 어떻게 Capture 할지 정하는 것은 아니기 때문이다. `move` 키워드란 어떻게 Capture 할지 정하는 것이다. 

# Iterator

Iterator 는 sequence 데이터에 차례로 어떤 작업을 할 수 있도록 해준다. 

Rust 의 Iterator 는 lazy 하다. 이는 Iterator 를 사용하는 Method 를 호출하기 전까지 sequence 데이터에 아무런 영향이 없다는 것이다. 가령 다음과 같이 `Vec::iter` 로 Iterator 를 만드는 것 자체는 아무런 일도 하지 않는다. 

```rust
let v1 = vec![1, 2, 3];
let v1_iter = v1.iter();
```

Iterator 를 만들면 다양하게 사용할 수 있다. 대표적으로 `for` 루프에서 사용하지.

## Iterator Trait 

모든 Iterator 는 `Iterator` Trait 를 구현한다. 이 Trait 는 다음과 같이 정의되어 있다. 

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

`type Item` 과 `Self::Item` 문법에 대해서는 챕터 19 에서 다룬다. 어쨌든 Iterator 는 오직 `next` Method 만 구현하면 된다는 것이다. 이 `next` 는 호출될때마다 Iterator 의 아이템 중 하나를 `Some` 으로 wrap 해서 반환하고 iteration 이 끝나면 `None` 을 반환한다. 

```rust
let v1 = vec![1, 2, 3];

let mut v1_iter = v1.iter();

assert_eq!(v1_iter.next(), Some(&1));
assert_eq!(v1_iter.next(), Some(&2));
assert_eq!(v1_iter.next(), Some(&3));
assert_eq!(v1_iter.next(), None);
```

위 코드에서 `next` 가 반환하는 것은 vector 의 immutable reference 이다. `iter` 가 immutable reference 로 구성된 Iterator 를 생성하기 때문이다. 만약 데이터의 Ownership 을 갖는 Iterator 를 만들고 싶다면 `into_iter` 를 호출하면 된다. 만약 mutable reference 로 구성된 Iterator 를 생성하고 싶다면 `iter_mut` 를 호출하면 된다.

## Methods that Consume the Iterator

Iterator 자체를 소모하는 Method 들을 consuming adaptor 라고 한다.

```rust
fn iterator_sum() {
        let v1 = vec![1, 2, 3];
        let v1_iter = v1.iter();
        let total: i32 = v1_iter.sum();

        assert_eq!(total, 6);
}
```

가령 위에서 `sum` 은 Iterator 의 Ownership 을 받아서 Sum 연산을 수행한다. 그래서 `sum` 호출 이후에 `v1_iter` 를 사용할 수 없다. 

## Methods that Produce Other Iterators

consuming adaptor 가 아닌 iterator adaptor 라는 것도 있는데, 얘는 `Iterator` trait 에 정의된 한 Iterator 를 다른 Iterator 로 변환한다.

```rust
let v1: Vec<i32> = vec![1, 2, 3];
v1.iter().map(|x| x + 1);
```

위 코드는 `map` 에 Closure 를 전달하여 새로운 Iterator 를 만드는 것이다. 즉 `map` 은 iterator adaptor 인 것이다. 하지만 `map` 이 반환하는 것은 Iterator 이므로 lazy 하다. 그래서 Iterator 를 consume 해주는 `collect` Method 를 사용해야 벡터로 저장할 수 있다.

```rust
let v1: Vec<i32> = vec![1, 2, 3];
let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();
assert_eq!(v2, vec![2, 3, 4]);
```

> <_> 라고 한 것은 어떤 문법?

`filter` iterator adaptor 는 Closure 가 `true` 를 반환할 때에만 새로운 Iterator 에 포함시킨다. 

## Creating Our Own Iterators with the Iterator Trait

지금까지 `Vec` 에 `iter`, `into_iter`, `iter_mut` 을 호출하여 Iterator 를 만들어 봤는데, `HashMap` 같은 다른 collections 에서부터도 Iterator 를 만들 수 있다. 일반적으로 `Iterator` Trait 를 구현한 모든 데이터타입으로부터 Iterator 를 만들 수 있다. 

가령 1 부터 5 까지 카운팅하는 Iterator 를 만들어보자. 먼저 `Counter` 라는 Struct 를 만든다. 

```rust
struct Counter {
    count: u32,
}

impl Counter {
    fn new() -> Counter {
        Counter { count: 0 }
    }
}
```

관례적으로 `new` Function (생성자) 을 만들어준다. 이제 `Iterator` Trait 를 구현해보자. 그러려면 `next` Method 를 구현하면 되지.

```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.count < 5 {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}
```

associated `Item` type 을 `u32` 로 지정했는데 이로써 `next` 의 반환 타입은 `u32` 가 된다. 

이렇게 만들어본 우리의 Iterator 를 `next` Method 를 직접 호출해봄으로써 테스트해보자. 

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn calling_next_directly() {
        let mut counter = Counter::new();

        assert_eq!(counter.next(), Some(1));
        assert_eq!(counter.next(), Some(2));
        assert_eq!(counter.next(), Some(3));
        assert_eq!(counter.next(), Some(4));
        assert_eq!(counter.next(), Some(5));
        assert_eq!(counter.next(), None);
    }
}
```

즉, `Counter::new()` 를 `vec![1,2,3,4,5].into_iter()` 와 거의 동일하다고 보면 된다. 

이렇게 구현된 Iterator 는 엄연히 Iterator 이므로 다음과 같이 Standard Library 에 있는 Iterator Method 들을 모두 사용할 수 있다. 

```rust
let sum: u32 = Counter::new()
    .zip(Counter::new().skip(1))
    .map(|(a, b)| a * b)
    .filter(|x| x % 3 == 0)
    .sum();
assert_eq!(18, sum);
```

# Improving Our I/O Project

iterator 로 minigrep 을 개선해보자. 

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

위와 같은 코드를 iterator 로 개선할 수 있다. 

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}
```

이렇게 함수형 언어 특징으로 mutable state 를 최대한 줄이는 것이 좋다. 왜냐면 나중에 병렬 처리를 할 때 접근 관리를 해주어야 하는 영역을 최소화할 수 있기 때문이다. 

심지어 for-loop 같은 것들 보다 iterator 를 사용하는게 성능이 좀 더 빠르다. 

---

# More About Cargo and Crates.io

## Customizing Builds with Release Profiles

Cargo 는 디폴트로 dev 레벨로 컴파일을 하는데 이는 최적화 레벨이 낮은 대신 컴파일 속도가 빨라서 디버깅을 빨리 할 수 있다. release 를 할때가 되었으면 release 레벨로 컴파일을 해라. 그러면 최적화를 빡세게 해서 프로그램의 성능을 높일 수 있다. dev 레벨과 release 레벨의 디폴트 최적화 단계는 각각 0, 3 단계이다. 그러나 이 최적화 단계 또한 커스터마이징 가능하다. 

[Cargo 의 모든 빌드 옵션](https://doc.rust-lang.org/cargo/reference/profiles.html) 을 살펴보라.

## Making Useful Documentation Comments

```rust
/// Adds one to the number given.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

위와 같이 `///` 으로 주석을 달면 Markdown 형식으로 HTML 변환이 되어 문서로 만들어진다. `cargo doc --open` 으로 확인하라. 

`//!` 는 아이템을 만드는 주석이고 `pub use` 로 선언된 Module 들도 자동으로 문서화가 된다. 

re-export 를 하면 실제 Module 경로가 매우 복잡해도 `use crate::path` 할 때 경로를 짧게 만들 수 있다. 

`cargo publish` 로 crate 를 publish 하라.

`cargo yank` 로 미래의 프로젝트들이 이전 버전의 crate 를 의존성으로 두는 것을 방지할 수 있다. 

# Cargo Workspaces

library crate 가 점점 더 커지면 이것을 다른 package 로 분리하고 싶어질 때가 온다. 이를 위해 Cargo 는 여러 package 를 관리하게 해주는 Workspaces 를 제공한다. 

Workspaces 는 같은 `Cargo.lock` 과 같은 output 디렉토리를 공유하는 package 집합이다.

이제 실행기능을 제공하는 Binary crate 와 1 을 더하는 기능을 제공하는 library crate, 2 를 더하는 기능을 제공하는 library crate, 이 세 가지 crate 를 같은 Workspaces 로 관리해보자. 

```shell
$ mkdir add
$ cd add
$ cat > Cargo.toml
[workspace]

members = [
    "adder",
]
$ cargo new adder
```

이제 `cargo build` 로 빌드 할 수 있다. 이제 library crate 를 추가해보자. `Cargo.toml` 을 다음과 같이 고치고, 

```toml
[workspace]

members = [
    "adder",
    "add-one",
]
```

다음 명령어로 library crate 를 만든다. 

```shell
$ cargo new add-one --lib
     Created library `add-one` package
```

`add-one/src/lib.rs` 는 다음과 같이 채우자.

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

이제 이 library crate 를 Binary crate 에서 사용하기 위하여 `adder/Cargo.toml` 에 다음을 추가하자. 

```toml
[dependencies]

add-one = { path = "../add-one" }
```

workspace 는 하나의 `Cargo.lock` 을 공유하기 때문에 한 crate 에서 어떤 package 의존성을 선언하면 다른 crate 에서도 해당 버전의 package 를 사용하게 된다. 만약 `add-one` 에서 다음과 같은 

```toml
[dependencies]
rand = "0.8.3"
```

package 를 사용하면 다른 crate 에서도 동일한 버전을 사용해야 한다. 하지만 이 dependencies 를 해당 crate 의 `Cargo.toml` 에 추가해주어야 사용할 수 있다. 

---

# Smart Pointers

> https://doc.rust-lang.org/book/ch15-00-smart-pointers.html

pointer 는 주소값을 저장하는 변수에 대한 개념이다. Rust 에서 pointer 에 해당하는 개념은 reference 이다. reference 는 데이터를 borrow 해올 뿐이라서 데이터를 지칭하는 것 외에 아무런 기능을 하지 않는다. 

반면 Smart pointer 는 reference 보다 더 다양한 기능을 제공한다. 가령 어떤 종류의 Smart pointer 는 reference counting 기능을 제공한다. 

또한 reference 가 단순히 데이터를 borrow 해오는데 비해 smart pointer 는 많은 경우 데이터의 owner 가 된다. 

사실 우리는 이미 smart pointer 를 다뤘었다. 그것은 `String` 과 `Vec<T>` 이다. 

Smart pointer 는 struct 를 통하여 구현되는데, 일반적인 struct 들과 다른 점은 smart pointer 가 `Deref` 와 `Drop` Trait 를 구현한다는 것이다. 

`Deref` trait 는 smart pointer 가 reference 처럼 행동하게 해준다. `Drop` trait 는 smart pointer 가 scope 를 벗어났을 때 drop 되는 시점을 커스터마이징 하게 해준다.

smart pointer 는 Rust 에서 자주 발견되는 디자인 패턴이고 많은 라이브러리에 독자적으로 구현되어 있으며 당신도 구현할 수 있다. 지금은 표준 라이브러리에 구현된 smart pointer 인 `Box<T>`, `Rc<T>`, `Ref<T>` 를 알아본다. 

이후에 interior mutablility 패턴과 reference cycles 개념을 알아보자.

# Box

`Box<T>` 는 데이터를 stack 이 아닌 heap 에 저장하게 해준다. stack 에 남는 것은 heap 에 있는 데이터를 가르킬 pointer 이다. Box smart pointer 는 다음과 같은 상황에 유용하다.

- 컴파일 시 사이즈를 알 수 없는 데이터 타입을 사용할 때 

- 매우 큰 데이터를 사용하면서 ownership 을 옮겨야 하는데 Copy 되지 않아야 할 때 

- When you want to own a value and you care only that it’s a type that implements a particular trait rather than being of a specific type (-> trait object ch17)

`Box` 의 기본적인 사용법은 다음과 같다. scope 를 벗어나면 stack 에 있는 pointer 와 heap 에 있는 data 모두 할당해제가 된다.

```rust
let b = Box::new(5);
println!("b = {}", b);
```

하지만 많은 상황에서 `i32` 변수 하나 정도는 `Box` 에 저장하는 것보다 그냥 stack 에 저장하는 것이 더 낫다. 

## Enabling Recursive Types with Boxes

재귀 타입 데이터는 데이터 구조 내부에 자기 자신의 타입을 갖는다. 이러한 타입은 이론적으로 무한히 끝나지 않기에 Rust 가 데이터 크기를 가늠할 수 없다. 그래서 재귀 타입에 대하여 Rust 는 에러를 발생시킨다. 그러나 Box 를 사용하면 정확한 크기를 알 수 있기 때문에 재귀 타입 데이터를 사용할 수 있다. 정확한 크기를 알 수 있기 때문에 재귀 타입 데이터를 사용할 수 있다. 

함수형 프로그래밍에서 자주 사용되는 cons 리스트를 예시로 들어보자. 다음과 같이 cons 리스트를 표현할 enum 을 정의하면 Rust 가 컴파일 시 사이즈를 가늠할 수 없기에 에러가 발생한다. 

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

하지만 일단 이 enum 을 기반으로 cons 리스트를 형식적으로라도 만들어보자. 

```rust
use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

물론 에러가 발생한다. 에러 타입은 "데이터 타입이 무한한 크기를 지닌다" 는 것이다. 

이것을 해결하는 방법은 `List` 를 재귀적으로 `List` 에 포함시키는 것이 아니라 `Box<List>` 를 포함시키는 것이다. Box smart pointer 는 pointer 이기 때문에 데이터의 크기과 관계 없이 항상 동일한 사이즈를 갖는다. 

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
}
```

이렇게 하면 Rust 는 `List` 의 사이즈가 `i32` 와 pointer 크기 만큼이라는 것을 알 수 있고 정상적으로 컴파일을 할 수 있게 된다. 

# Treating Smart Pointers Like Regular References with the Deref Trait