import flawunicode

success_examples = [
    'How we predict elections',
    '我不知道要做什麼',
    "本プログラムは、クリエイターの創作活動をさまざまな形で支援することで、クリエイターの可能性を広げることを目的としています。今回、約1,200件の応募のなかから、音楽、アート、映像、スポーツ、エネルギー、食などに関わる活動を行う多様なクリエイターへのサポートが決定しました。noteは「だれもが創作をはじめ、続けられるようにする」ための取り組みを今後も続けていきます。",
    '瑞薩：車用晶片荒將延續到下半年 不確定何時能達平衡  - 歐亞股',
    'דוויין ווייד הואשם על ידי אשתו',
    'टॉप न्यूज़ · राज्य-शहर|Local राज्य-शहर ·',
    'لرئيسية ... هيفاء وهبي نقاشات رواد مواقع التواصل الاجتماعي في دول عربية',
    'Major Democratic polling firm expands before midterm election',
]

failed_examples = [
    '�����4m�',
    '�� ��w��Qe�W����c��ᾎO�W7���di����9����-h�@F���oNwO���ͱ��3����{��ڙ~qc�G���Ϝ؀',
    """Fb�9��țD��ZԈ>P\'K�Y#�e4q��7~ >^�6���H��5""",
    'Á¶ÀÌ½ÃÆ¼, ¡®3on3 ÇÁ¸®½ºÅ¸ÀÏ¡¯ 2Á¾ÀÇ ¿¡µð¼Ç ¹øµé Ãâ½Ã',
    "�����4m�}ھR�N!V��s�9��l�}[��o��ڧ�] BygF��q��_�n���0��#]���.�y&��v�]<0��=j�&�)���^1ål����r�.9",
]

def test_examples():
    for example in success_examples:
        assert flawunicode.detect(example) > 0.5
    for example in failed_examples:
        assert flawunicode.detect(example) < 0.4
