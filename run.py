from operation.gh_testcase.gh_equipments import gh_001, gh_002, gh_003, gh_004
from operation.CNC_testcase.cnc_equipments import cnc_1, cnc_2, cnc_3, cnc_4
from operation.fj_testcase.fj_equipments import fj_001, fj_002, fj_003, fj_004
from operation.qs_testcase.qs_equipments import qs_001, qs_002
from operation.ay_testcase.aoya_equipments import app
import threading
from support.moc.equipment.equipment import Equipments

all_equipments = Equipments(gh_001, gh_002, gh_003, gh_004, cnc_1, cnc_2, cnc_3, cnc_4, fj_001, fj_002, fj_003,
                            fj_004, qs_001, qs_002)


def test():
    import time
    while True:
        time.sleep(10)
        print(1)


if __name__ == '__main__':
    print("start")
    aoya = threading.Thread(target=app.run, args=["0.0.0.0", 5000])
    others = threading.Thread(target=all_equipments.continue_publish)
    others.start()
    aoya.start()
    others.join()
    aoya.join()
