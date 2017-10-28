# -*- coding: utf-8 -*-
# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

movies_config = [
    ["黑客帝国", "未来世界尼奥等人抗争人工智能矩阵的故事", "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=261ec71cff03738dda4a0b20831ab073/279759ee3d6d55fb2de4ce9a64224f4a20a4dd68.jpg", "http://v.youku.com/v_show/id_XMjg5Njg3ODA4MA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2", 8.8],
    ["霸王别姬", "影片围绕两位京剧伶人半个世纪的悲欢离合，展现了对传统文化、人的生存状态及人性的思考与领悟。", "https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=fb3bf63cabec8a1300175fb2966afaea/b58f8c5494eef01f963eca16e2fe9925bc317d3f.jpg", "http://v.youku.com/v_show/id_XMjg5NTA5MDA5Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2", 9.5],
    ["大话西游", "周星驰的经典之作，影响了整整一代人。", "https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=fd6576f29d504fc2b652b85784b48c74/9358d109b3de9c82031303756a81800a18d843d2.jpg","http://v.youku.com/v_show/id_XMjk2ODc0OTE5Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2", 9.2]
]

movies_list = []

for movie_info in movies_config:
    movie = media.Movie(movie_info[0], movie_info[1], movie_info[2], movie_info[3], movie_info[4])
    movies_list.append(movie)

fresh_tomatoes.open_movies_page(movies_list)
