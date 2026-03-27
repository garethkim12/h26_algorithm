##### 스택 구조 실습_김근하 작성

# 연산 함수 정의
stack = []
capa = 5
def Push(data):
        if isFull():
            return print("> Stack이 차 있어서 더 이상 추가 할 수 없습니다.") 
        else:        
            return stack.append(data)
        

def Pop():
        if isEmpty():
            return print("> Stack 이 비어 있습니다.")
        else:
            return stack.pop()



def Peek():
    if isEmpty():
        return print("> Stack이 비어 있습니다.")
    else:
        return print(f'> 가져올 데이터[{stack[-1]}]')

## 논리 함수 정의

def isEmpty():
       return len(stack) == 0

def isFull():
       return len(stack) == capa


# 입력 인터페이스 구성
print('-'*5, '[ 정수형 스택 연산 실습 (용량 5)]', '-'*5)
while True:
    print('='*45)
    print('   ','1.Push    2.Pop    3.Peek    0.Exit')
    print('='*45)
    choice = input('> 매뉴 선택 :')

    if choice == '1':
        data = int(input('> 데이터 입력 :'))
        Push(data)
    elif choice == '2':
        data = int(input('> 데이터 입력 :'))
        Pop()
    elif choice == '3':
        Peek()
    elif choice == '0':
        print('-'*6, '[ 정수형 스택 연산 실습 종료]', '-'*6)
        break
    else:
        print("> 잘못된 선택입니다.")
        continue
    print(f'> 현재 스택 상태 : {stack}')