다시 공부를 시작하면서 적어보는 자료구조 공부

해당 자료구조의 특징이나, 비슷한 역할의 자료구조와 차이점 장단점 위주로 우선 정리

** Python / Java 


Array, ArrayList, LinkedList

Python 에서는 list타입으로 해당 자료구조 구현 


Array - 초기화시 사이즈를 미리 지정, 데이터 추가삭제 어렵
ArrayList - 크기가 동적 (가용량 이상 저장시, 더 큰 메모리 새로 할당) 데이터 추가삭제 용이 검색이 많을때 사용
LinkedList - 항상 일정한 속도, 노드 뒤에 다음 데이터의 주소값이 있고 이를 통해 다음 데이터를 찾아감 그래서 (linkedList) 삽입/삭제 잦을때 사용



Stack, Queue

Stack - FILO or LIFO, 내부 프로세스 구조의 함수 동작 방식
Queue - FIFO, 프로세스 스케줄링 방식을 구현하기 위에 많이 사용

Hash, Hash Map, Hash Table

Python Dicionary 타입이 Hash Table


K-V 형식 속도가 빠르다, Key는 중복될수 없고 Value는 중복 가능

Hash 충돌 현상

*Java Hash Map 과 Hash Table 차이점
-Thread-safe 여부
-null 허용 여부
-enumeration 여부


Tree

Node, Branch로 사이클을 이루지 않도록 구성한 데이터 구조
이진트리 형태 구조로 탐색 알고리즘 구현 



Heap

데이터 최소값과 최대값을 바르게 찾기 위한 완전 이진트리

최대값을 구하기 위한 구조, 최소값을 구하기 위한 구조

Heap과 이진탐색트리의 공통점 차이점

공 - 이진트리
차이점 - Heap은 각 노드의 값이 자식 노드보다 크거가 같음 (최대힙)
        이진탐색트리는 왼쪽 자식노드값이 가장 작고 그다음 부모노드, 그다음 오른쪽 자식노드값이 가장 큼
        힙은 자식 노드의 가장작은 값이 왼쪽, 큰건 오른쪽이어야 한다는 조건이 없음
