# LEFT RIGHT 괄호를 다는 경우와 그 예시

"""
LEFT RIGHT 괄호를 쓰는 경우와 쓰지 않는 경우를 철저히 구분지어서 정리해야 한다.
둘 다 되는 경우는 없으며, 무조건 철저하게 괄호 안에 있는 문자열의 케이스를 구분지어야 한다.

1) 윗첨자, 아랫첨자
- 지수(^n)
- 아랫첨자(_n)
2) 분수식(frac{}{})
3) bar
4) vec
5) root

와 같은 경우가 괄호 안에 있는 경우, LEFT RIGHT가 필요하며, 이 이외의 경우에는 무조건! LEFT RIGHT를 제거해야 한다.

함수는 간단하게 

-LEFT RIGHT 존재 판별 함수
-LEFT RIGHT 가능/불가능 판별 함수
-LEFT RIGHT 추가 함수 
-LEFT RIGHT 제거 함수

이렇게 4가지로 나눌 것이다.

"""

def isLeftRightIn(string):
    """
    LEFT RIGHT가 안에 있는지 확인한다
    """


def isLeftRight(string):
    """
    LEFT RIGHT가 가능한지 불가능한지 판별한다.
    """


def delLeftRight(string):
    """
    LEFT RIGHT를 제거한다.
    """

def addLeftRight(string):
    """
    LEFT RIGHT를 추가한다.
    """
