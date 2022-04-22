# SASS

CSS는 비교적 간단한 문법을 가지지만 작업이 커질수록 여러 불편함이 생긴다.  
SASS는 반복되어 사용되는 선택자 구문을 간략히 처리 및 연산 기능, 구문 등의 기능을 제공하여 CSS의 가독성, 재사용성, 유지보수를 쉽게 도와준다.

• CSS Preprocessor
• CSS에 variable, nesting, mixin, inheritance 등의 개념이 추가
• SASS는 Preprocessor 과정을 통해 CSS로 해석 및 컴파일된다.

```
/**CSS Syntax**/

.list {
    width: 100px;
    float: left;
}

.list li {
    color: red;
    background: url("./image.jpg");
}

.list li:last-child {
    margin-right: -10px
}


/**SCSS Syntax**/

.list {
  width: 100px;
  float: left;
  li {
    color: red;
    background: url("./image.jpg");
    &:last-child {
      margin-right: -10px;
    }
  }
}
```

🔥 SASS(SCSS)는 CSS를 편리하게 이용할 수 있도록 도와주며 추가 기능도 있는 확장판이다
