from chat_completions import get_chat_response

if __name__ == '__main__':
    # 프로젝트 아이디어 브레인스토밍 요청 예시
    scenario_description = (
        "한 온라인 리테일 회사의 연간 데이터가 주어졌습니다. "
        "이 데이터에는 월별 총매출, 제품 카테고리별 판매량, "
        "고객 만족도 설문 점수가 포함되어 있습니다. "
        "이 데이터를 활용하여 어떤 데이터 분석 프로젝트를 진행할 수 있을까요? "
        "3가지 아이디어를 요약 설명과 함께 제안해주세요."
    )    

    role = "당신은 뛰어난 데이터 분석가입니다. 주어진 비즈니스 데이터로 가능한 분석 프로젝트를 브레인스토밍해보세요."


    print(get_chat_response(scenario_description, role))

