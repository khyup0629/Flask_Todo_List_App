# Flask Todo List App Project
+ 개요
+ [프로젝트 기획 의도](#프로젝트-기획-의도)
+ [앱 화면 구성](#앱-화면-구성)
+ [앱 기능 설명](#앱-기능-설명)
+ [추가하고 싶은 기능](#추가하고-싶은-기능)
---
## 개요
> 파이썬 플라스크와 MongoDB를 이용한 To-do note
  + Frontend : Bootstrap
  + Backend : Flask
  + DB : MongoDB
---
## 프로젝트 기획 의도
> 첫 번째 개인 토이 프로젝트로 적당한 난이도라 판단했다. 난이도가 높지 않은 웹 어플리케이션을 스스로 개발해봄으로써 프론트엔드와 백엔드 사이의 상호 작용에 관하여 공부해보고 싶었고, DB를 활용해보면서 어떤 메커니즘으로 작용하는지 알고 싶었다. 또한 Todo List는 앞으로 나의 개발 공부에 자기개발 도구로서 활용해볼 수 있을 것 같다는 점에서 매력적으로 다가왔다.
---
## 앱 화면 구성
![image](https://user-images.githubusercontent.com/43658658/119603193-ad929980-be27-11eb-8ed6-5e0e3b9a8259.png)
![image](https://user-images.githubusercontent.com/43658658/119603314-e763a000-be27-11eb-9968-85df197ae224.png)
![image](https://user-images.githubusercontent.com/43658658/119603362-fe09f700-be27-11eb-8187-f630812309d6.png)
![image](https://user-images.githubusercontent.com/43658658/119603400-10843080-be28-11eb-82b9-4d9c9a0821d7.png)
![image](https://user-images.githubusercontent.com/43658658/119603443-298ce180-be28-11eb-8cfa-5c3843793343.png)
---
## 앱 기능 설명
+ 웹 페이지의 크기에 맞춰서 **view 또한 유동적으로 변화**하게 했다.
+ 본문의 내용이 한 눈에 들어오도록 하기 위해 **상단의 접이식 메뉴**를 통해 필요시에만 펼쳐서 메뉴를 확인하게 했다.
+ **모든 항목, 해야할 항목, 완료된 항목**으로 할 일을 분류하여 사용자가 자신이 완료한 일, 해야할 일에 대해 쉽고 편리하게 구분짓도록 했고, 필요에 따라 모든 항목을 표시하여 모든 일에 대해 전체적으로 볼 수 있도록 했다.
+ **Input memo**를 통해 **자신이 할 일을 입력**하고 **중요도를 선택**해 추가할 수 있도록 했다.
+ **각 항목에 대한 미완료 또는 완료 상태를 변경**할 수 있도록 했다. List의 상태의 동그라미 아이콘이 비어있는 상태(미완료)에서 클릭하면 체크표시 상태(완료)로 바뀐다. 동시에 해당 항목은 '해야할 항목'에서 '완료된 항목'으로 분류된다. 반대로 완료 상태에서 클릭 시 미완료 상태로 되며 해당 항목은 '완료된 항목'에서 '해야할 항목'으로 재분류된다.
+ 필요 없는 항목에 대한 **삭제가 가능**하다. 항목의 삭제 탭에서 휴지통 버튼을 클릭하면 '정말로 삭제하시겠습니까?'라는 **대화상자로 주의**를 준다. '삭제'버튼을 누르면 해당 항목은 삭제된다.
+ 항목에 대한 **내용과 중요도의 변경이 가능**하다. 항목의 변경 탭에서 아이콘을 클릭하면 update memo 페이지로 이동한다. 변경할 내용을 입력하고 중요도를 재선택한 후 변경을 클릭하면 해당 항목의 내용과 중요도가 변경된다.
---
## 추가하고 싶은 기능
+ 날짜별 해야 할 일 보기
+ 중요도 순 정렬
+ 페이지 나누기

[위로](#Flask-Todo-List-App-Project)
---
