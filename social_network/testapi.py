# import requests

# email = 'TestUser3@gmail.com'
# password = 'TestUser5678'

"""  1) 'Create User' Feature  """

# r = requests.post('http://127.0.0.1:8000/api/register/', json={
#     'email': 'TestUser3@gmail.com',
#     'first_name': 'TestUSer3',
#     'last_name': 'TestUser3Last',
#     'password1': 'TestUser5678',
#     'password2': 'TestUser5678'
# })

"""  2) 'Login User' + 'Token Access' Feature  """

# r1 = requests.post('http://127.0.0.1:8000/api/token/',
#                    json={'email': email, 'password': password})
# token = 'Bearer {}'.format(r1.json()['access'])
#
# """  3) 'Create Post by User only' Feature  """
#
# post = {
#     'content': 'Post3'
# }

# r2 = requests.post('http://127.0.0.1:8000/api/posts/', headers={'Authorization': token},
#                   json=post)

"""  4) 'Post Like' Feature  """

# r3 = requests.post('http://127.0.0.1:8000/api/posts/1/likes/', headers={'Authorization': token},)

"""  5) 'Post Unlike' Feature  """

# r4 = requests.delete('http://127.0.0.1:8000/api/posts/2/likes/', headers={'Authorization': token},)

"""  6) 'Like Analytics' Feature  """

# r5 = requests.get('http://127.0.0.1:8000/api/posts/analytics/', headers={'Authorization': token},)
# like_count = '{}'.format(r5.json())
# print(like_count)

"""  7) 'User Activity' Feature  """

# r6 = requests.get('http://127.0.0.1:8000/api/users/2/activity/', headers={'Authorization': token},)
# user_activity = '{}'.format(r6.json())
# print(user_activity)
