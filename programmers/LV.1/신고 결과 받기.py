"""
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 
무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

유저 ID	유저가 신고한 ID	설명
"muzi"	"frodo"	"muzi"가 "frodo"를 신고했습니다.
"apeach"	"frodo"	"apeach"가 "frodo"를 신고했습니다.
"frodo"	"neo"	"frodo"가 "neo"를 신고했습니다.
"muzi"	"neo"	"muzi"가 "neo"를 신고했습니다.
"apeach"	"muzi"	"apeach"가 "muzi"를 신고했습니다.
각 유저별로 신고당한 횟수는 다음과 같습니다.

유저 ID	신고당한 횟수
"muzi"	1
"frodo"	2
"apeach"	0
"neo"	2
위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 
이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

유저 ID	유저가 신고한 ID	정지된 ID
"muzi"	["frodo", "neo"]	["frodo", "neo"]
"frodo"	["neo"]	["neo"]
"apeach"	["muzi", "frodo"]	["frodo"]
"neo"	없음	없음
따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""

# 내가 푼 것
def solution(id_list, report, k):
    stop_cnt = {name: 0 for name in id_list} # 신고 당한 카운트 딕셔너리
    info_cnt = {name: 0 for name in id_list} # 신고 해서 정보 받는 수 저장 딕셔너리
    organize_report = list(set(report)) # 똑같은 신고 중복 제거
    
    # 신고 당한 횟수만큼 카운트
    for i in organize_report:
        name_report = i.split()
        stop_cnt[name_report[1]] += 1
    
    # 신고 당한 횟수가 k 이상인 경우만 저장
    stop_list = [name for name, cnt in stop_cnt.items() if cnt >= k]
    
    # 자신이 신고한 사람이 정지 당한 경우 카운트
    for i in organize_report:
        stop_report = i.split()
        if stop_report[1] in stop_list:
            info_cnt[stop_report[0]] += 1
    
    # 결과 리스트
    info_list = [cnt for name, cnt in info_cnt.items()]
    
    return info_list

# 내가 푼 것보다 훨씬 가독성 좋은 모범 코드
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer