"""
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 
맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 
제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고,
제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 
도시 이름은 최대 20자로 이루어져 있다.
"""

def solution(cacheSize, cities):
    answer = 0
    cache = []
    lower_cities = [x.lower() for x in cities] # 도시이름 모두 소문자로 바꾸기
    
    for city in lower_cities:
        if cacheSize == 0:
            answer += 5
        elif len(cache) < cacheSize:
            if city in cache: # LRU 알고리즘이므로 제거 후 가장 뒤에 다시 추가
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                answer += 5
        else:
            if city in cache: # LRU 알고리즘이므로 제거 후 가장 뒤에 다시 추가
                cache.remove(city)
                cache.append(city)
                answer += 1
            else: # LRU 알고리즘이므로 맨 앞의 도시 제거 후 뒤에 새로운 도시 추가
                cache.pop(0)
                cache.append(city)
                answer += 5
                
    return answer