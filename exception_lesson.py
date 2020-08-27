ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:  # raise Exception("Products Cart count not matching")
    pass
assert (ItemsInCart == 0)

# try , catch
# try:
#     with open('readwritetest.txt', 'r') as reader:
#         reader.read()
# except:
#     print("Somehow I reached this block because there is a failure in my try block")

try:
    with open('est.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    """
    This is important in test automation, because of its capability to clean resources after a test fails, you can set
    clear cache, cookies, or use an API to take of test data breadcrumbs
    """
    print("cleaning up resources")
