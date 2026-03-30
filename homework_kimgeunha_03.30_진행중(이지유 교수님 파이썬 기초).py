print('='*5, '로그 분석 프로그램', '='*5)
print('1. 로그 파일 불러오기')
print('2. 전채 로그 보기')
print('3. 로그 레벨별 개수 출력')
print('4. 날짜별 로그 개수 출력')
print('5. ERROR 로그만 보기')
print('6. 특정 레벨 로그 검색')
print('7. 특정 날짜 로그 검색')
print('8. 가장 많이 발생한 로그 레벨 출력')
print('9. ERROR가 가장 많이 발생한 날짜 출력')
print('10. 분석 결과 파일 저장')
print('11. 오전/오후 로그 개수 분석')
print('12. 연속 ERROR 발생 구간 찾기')
print('13. 로그 메시지 키워드 검색')
print('14. 로그 개수 총합 출력')
print('15. 종료')




while True:
    menu = input('매뉴를 입력 하세요:')
    #1. 로그 파일 불러오기
    if menu == '1':
     with open('log.txt', 'r', encoding='utf-8') as file:
       print(file)
    #2. 전체 로그 보기
    elif menu == '2':
     with open('log.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)
    #3. 로그 레벨별 개수 출력   
    elif menu == '3':
     with open('log.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f'ERROR의 갯수 : {content.count('ERROR')}')
        print(f'INFO의 갯수 : {content.count('INFO')}')
        print(f'WARNING의 갯수 : {content.count('WARNING')}')
    #4. 날짜별 로그 개수 출력 
    elif menu == '4':
        with open('log.txt', 'r', encoding='utf-8') as file:
            content = file.read() # 여기서도 한 번만 읽기
            
            days = ['01', '02', '03', '04', '05', '06', '07', '08']
            for day in days:
                date_str = f'2026-03-{day}'
                print(f"3/{day} 로그 갯수: {content.count(date_str)}")
    #5. ERROR 로그만 보기
    elif menu == '5':
        print("--- ERROR 로그만 보기 ---")
        with open('log.txt', 'r', encoding='utf-8') as file:
            # 한 줄씩 읽으면서 'ERROR'가 포함된 줄만 출력합니다.
            for line in file:
                if 'ERROR' in line: #ERROR 인 로그 내용만 보기
                    print(line.strip())
    #6. 특정 레벨 로그 검색
    elif menu == '6':
        with open('log.txt', 'r', encoding='utf-8') as file:
           Q = input('특정 레벨을 입력 하시오:(ERROR, INFO, WARNING)').upper()
           for line in file:
              if Q in line:
                 print(line.strip())
              
    #7. 특정 날짜 로그 검색
    elif menu == '7':
        with open('log.txt', 'r', encoding='utf-8') as file:
           D = input('특정 날짜를 입력하시오:(예시:01)')
           date_str = f'2026-03-{D}'
           if date_str in line:
              print(line.strip()) 
           else:
              print('다시 입력 하세요:')
              continue 
    #8. 가장 많이 발생한 로그 레벨 출력          
    elif menu == '8':
       # 8번 메뉴는 전체 개수를 비교해야 하므로 content를 먼저 만듭니다.
        with open('log.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            
            # 각 레벨의 개수를 변수에 담습니다.
            a_cnt = content.count("ERROR")
            b_cnt = content.count("WARNING")
            c_cnt = content.count("INFO")
            
            # 파이썬의 내장 함수 max()를 쓰면 훨씬 간단하게 비교 가능합니다!
            max_val = max(a_cnt, b_cnt, c_cnt)
            
            if max_val == a_cnt:
                print(f"가장 많이 발생한 레벨: ERROR ({a_cnt}회)")
            elif max_val == b_cnt:
                print(f"가장 많이 발생한 레벨: WARNING ({b_cnt}회)")
            else:
                print(f"가장 많이 발생한 레벨: INFO ({c_cnt}회)")


    # 9. ERROR가 가장 많이 발생한 날짜 출력
    elif menu == '9':
        with open('log.txt', 'r', encoding='utf-8') as file:
            # 1. 날짜별 ERROR 개수를 저장할 딕셔너리 만들기
            error_counts = {}
            days_array = ['2026-03-01', '2026-03-02', '2026-03-03', '2026-03-04', 
                          '2026-03-05', '2026-03-06', '2026-03-07', '2026-03-08']
            
            # 파일 내용을 한 번만 읽어옵니다.
            lines = file.readlines()
            
            for day in days_array:
                count = 0
                for line in lines:
                    # 해당 날짜이면서 동시에 ERROR가 포함된 줄인지 확인
                    if day in line and 'ERROR' in line:
                        count += 1
                error_counts[day] = count # { '2026-03-01': 5, ... } 형태로 저장됨
            
            # 2. 딕셔너리에서 값이 가장 큰 날짜 찾기
            # error_counts.get을 기준으로 가장 큰 키(날짜)를 가져옵니다.
            max_day = max(error_counts, key=error_counts.get)
            max_value = error_counts[max_day]
            
            print(f"🚩 ERROR가 가장 많이 발생한 날짜: {max_day} ({max_value}회)")

    elif menu == '15':
        print("프로그램을 종료합니다.")
        break