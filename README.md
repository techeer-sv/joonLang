# joonLang
테커의 멘토 (-멘토?-), 김영준의 어록으로 만든 언어입니다. 

엄랭과 같은 brainf*ck언어들에서 영감을 얻었습니다.

![Untitled2](https://github.com/printSANO/joonLang/assets/83595905/6f6225c2-5ebb-4bec-84f2-b3587957bac7)

"하시면 어떻게든 됩니다." 를 언어 모토로 삼고 있습니다. 그것이 팀준이니까.

# 참고 어록
### 명대사

- 여러분 그럴 시간에 코드 한 줄 더 쓰세요.
- 잔다고요? 지금? 두신데?
- 벌써 가세요?
- 그래서 ㅇㅇ이는 왜 ㅁㅁ 안하니?
- 그래서 내가 쓴 글 읽었니?
- 기술블로그 쓰셨나요?
- 잠이 오세요?
- 이력서는 다 쓰셨어요?
- 그냥 여쭤보는 거예요 ^^
- 저 f 인데요? - 이러신 적이 있나요? 저보다 충격이네요
- @@님 벌써 주무시는 거 아니죠?
- 저는 강요 안 해요 ~
- 하기 싫으면 안해도 되요 ~
- 선택은 자유입니다 ~
- 아정님 맥 언제 사세요?
- 아정님 맥 사세요
- 유진님 잠깐 소회의실로 따라오세요
- 차고로 와
- 테커톡 하셔야죠
- 안보는게 좋을 거 같은데
- 안타깝네요
- (물 마시는 누군가를 보며) 워터밤 하려고?
- (물 마시는 누군가를 보며) 물 벌크업 벌크업 마시네
- @@님이 말씀해 보세요
- 왠지 나부터 시킬 것 같다 하시는 분! 자 정현님! (하린님!)
- 네? (에?)

# 초기 설정
1. joonLang 디렉토리에로 들어와 주시면 됩니다.
2. `bash add_joon`을 터미널에 실행 해주시면 됩니다.
- 위 스크립트는 수퍼유저 권환이 필요하기 때문에 비밀번호 입력이 필요합니다.
- "Symbolic link 'joon' created in /usr/local/bin." 라는 메시지가 뜨면 성공입니다.
3. 이제 이 디렉토리에서는 joon {filename}.joon 으로 실행이 가능합니다
- tests 디렉토리에 test.joon을 실행 하고싶으시면 `joon tests/test.joon`을 하시면 됩니다.
4. 새로운 파일을 만드실때 확장자를 .joon 으로 해주시면 됩니다.

# 준랭 삭제
- "Symbolic link 'joon' created in /usr/local/bin." 을 없에시고 싶으시면 `joon remove` 를 하시면 없어집니다.
- 수퍼유저 권환으로 비밀번호를 입력하시면 "joon removed" 가 뜹니다.
- 다시 joon 확장자 파일을 joon으로 실행하시고 싶으시면 위 초기 설정을 다시 따라하시면 됩니다.

# 문법

## 메인 함수 선언
- 모든 준랭 파일은 시작과 끝이 있습니다
- `하시면 어떻게든 됩니다.` 로 시작해서 `끝내는 것도 자유입니다.` 로 끝납니다.
- 만약에 위에 두 문장이 없을시 에러문이 나옵니다

## 변수 선언

- ㅇㅇ님이말씀해보세요
- 여기서 ㅇㅇ이 변수입니다
- 예시
```
익명님이말씀해보세요
```
## 변수 사용
- 변수를 사용하고싶을때는 뒤에 `님` 을 붙이면 됩니다

## 연산자

- 변수에 값을 추가하거나 그냥 콘솔에 리턴할수있습니다
- `네?` 는 +1 이고 `에?` 는 -1 입니다.
- 곱하기는 `워터밤` 을 사용하시면 됩니다
- 변수에 값을 바꿀때는 `님?` 을 뒤에 붙이고 사용하시면 됩니다.
- 예시
```
익명님이말씀해보세요

익명님? 네?네?

익명님? 에?

익명님? 네?네? 워터밤 네?네?
```
- 위 예시에는 변수를 선언하고
- 변수에 2를 더하고
- 변수에 1을 빼고
- 변수에 2*2 를 더해준겁니다

## 입출력
- 입력은 ㅇㅇ님맥언제사세요 로 합니다.
- ㅇㅇ 은 변수입니다
- 변수 선언을 한 이후에 입력을 할수있습니다.
- 입력은 `네?` 와 `에?` 만 받습니다
- 예시
```
익명님이말씀해보세요

익명님맥언제사세요
```
- 출력은 두가지 방식이 있습니다
- `ㅇㅇ님맥사세요` 는 int리턴값이 나오고
- `ㅇㅇ님맥사세요!` 는 ASCII 변환값이 나옵니다
- 예시
```
#대충 익명이라는 변수는 65라는 값이 있다고 합시다

익명님맥사세요
익명님맥사세요!

# 결과:
# 65
# A
```

## 반복문
- 반복문은 `언제까지 해보실래요?` 로 시작해서 `자러가시는거에요?` 로 끝납니다.
- `언제까지 해보실래요?` 뒤에 `네?` 아니면 변수를 넣어서 몇번 반복할지 설정할수있습니다.
- 예시
```
익명님이말씀해보세요

언제까지 해보실래요? 네?네?네?
    익명님? 네?네?
    자러가시는거에요?

익명님맥사세요
# 결과:
# 6
```
- 위 예시에서는 익명 변수에 2를 3번 더해서 6이 됩니다.

## 조건문
- 조건문은 `기술블로그 쓰셨나요?` 로 시작해서 `그냥여쭤^^보는거에요` 로 끝납니다.
- `기술블로그 쓰셨나요?` 뒤에 변수나 연산자를 2개를 넣어서 둘이 같으면 조건문이 발동됩니다.
- 예시
```
#익명1은 값이 1이 라고 하고
#익명2는 값이 2라고 합시다.

기술블로그 쓰셨나요? 익명1님 네?
    익명2님? 네?
    그냥여쭤^^보는거에요

익명2님맥사세요

# 결과:
# 3
기술블로그 쓰셨나요? 익명2님 네?
    익명1님? 네?
    그냥여쭤^^보는거에요

익명1님맥사세요

# 결과:
# 1
```
- 위 예시에서 익명1은 값이 1 이고 네? 는 값이 1 이니까 조건문이 발동되서 익명2는 3이 됩니다.
- 그 다음 조건문에서는 익명2는 3이고 네? 는 값이 1 이니 조건문이 발동 안되어서 익명1은 1에서 바뀌질 않습니다.

# 추가 doc
- tests 디렉토리에 있는 파일 2개를 보시면 이해가 좀 더 쉬울겁니다.
