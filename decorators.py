def decorator(func):
    def decorated(input_text):
        print('함수시작')
        func(input_text)
        print('함수 끝')

    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello_world')


# def decorator(func):
#     def decorated(x,y):
#         if x > 0 or y > 0 :
#             return func(x,y)
#         else:
#             print("error")
#
#     return decorated
#
# @decorator
# def rectangle(x,y):
#     return x * y
#
# def triangle(x,y):
#     return 1/2 * x * y
#





