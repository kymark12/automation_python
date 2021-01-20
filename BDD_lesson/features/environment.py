from BDD_lesson.features.steps.step_impl import *


def after_scenario(context, scenario):
    res_deletebook = requests.post(context.urls[1], json={"ID": context.bk_id},
                                   headers=context.headers)
    assert res_deletebook.status_code == 200
    res_message_delete = res_deletebook.json()
    res_message = res_message_delete["msg"]

    print(res_message)
    assert res_message == "book is successfully deleted"
