# -*- coding: utf-8 -*-
'''    [화면번호]
        화면번호는 서버에 시세조회나 주문을 요청할때 이 요청을 구별하기 위한 키값으로 이해하시면 됩니다.
        0000(혹은 0)을 제외한 임의의 숫자를 사용하시면 되는데 갯수가 200개로 한정되어 있기 때문에 이 갯수를 넘지 않도록 관리하셔야 합니다.
        만약 사용하는 화면번호가 200개를 넘는 경우 조회결과나 주문결과에 다른 데이터가 섞이거나 원하지 않는 결과를 나타날 수 있습니다.
'''
selectConditionName = "단타 추세"
sendConditionScreenNo = "001"
sendRealRegScreenNo = "002"
dict_jusik = {
               "분봉TR":("종목코드", 
                            "종목명", 
                            "현재가",
                            "거래량", 
                            "체결시간", 
                            "시가",
                            "고가",
                            "저가", 
                            "수정주가비율", 
                            "수정비율", 
                            "대업종구분",
                            "소업종구분",
                            "종목정보",
                            "수주주가이벤트",
                            "전일종가"
                            ),
               "체결실시간":("종목코드", 
                            "종목명",
                            "체결시간", 
                            "현재가",
	                        "전일대비",
	                        "등락율",
	                        "(최우선)매도호가",
	                        "(최우선)매수호가",
                            "거래량",
	                        "누적거래량",
	                        "누적거래대금",
	                        "시가",
	                        "고가",
	                        "저가",
    	                    "전일대비기호",
	                        "전일거래량대비(계약,주)",
	                        "거래대금증감",
	                        "전일거래량대비(비율)",
	                        "거래회전율",
	                        "거래비용",
	                        "체결강도",
	                        "시가총액(억)",
	                        "장구분",
	                        "KO접근도",
	                        "상한가발생시간",
	                        "하한가발생시간")
}

dict_fid_set = {
                "주식체결": "20;10;11;12;27;28;15;13;14;16;17;18;25;26;29;30;31;32;311;290;691;567;568"
}
def fid(name):
    return dict_fid[name]

def parseErrorCode(code):
    """에러코드 메시지

        :param code: 에러 코드
        :type code: str
        :return: 에러코드 메시지를 반환

        ::

            parseErrorCode("00310") # 모의투자 조회가 완료되었습니다
    """
    code = str(code)
    ht = {
        "0" : "정상처리",
        "-100" : "사용자정보교환에 실패하였습니다. 잠시후 다시 시작하여 주십시오.",
        "-101" : "서버 접속 실패",
        "-102" : "버전처리가 실패하였습니다.",
        "-200" : "시세조회 과부하",
        "-201" : "REQUEST_INPUT_st Failed",
        "-202" : "요청 전문 작성 실패",
        "-300" : "주문 입력값 오류",
        "-301" : "계좌비밀번호를 입력하십시오.",
        "-302" : "타인계좌는 사용할 수 없습니다.",
        "-303" : "주문가격이 20억원을 초과합니다.",
        "-304" : "주문가격은 50억원을 초과할 수 없습니다.",
        "-305" : "주문수량이 총발행주수의 1%를 초과합니다.",
        "-306" : "주문수량은 총발행주수의 3%를 초과할 수 없습니다."
    }
    return ht[code] + " (%s)" % code if code in ht else code