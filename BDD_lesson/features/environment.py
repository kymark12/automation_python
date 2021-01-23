import requests


def after_scenario(context, scenario):
    if 'library' in scenario.tags:
        res_deletebook = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={'ID': context.bk_id},
                                       headers={"Content-Type": "application/json"})
        assert res_deletebook.status_code == 200
        res_message_delete = res_deletebook.json()
        res_message = res_message_delete['msg']
        print(res_message)
        assert res_message == "book is successfully deleted"
