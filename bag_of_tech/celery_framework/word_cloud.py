from __future__ import absolute_import, unicode_literals
import logging
import numpy as np
from bag_of_tech.celery_framework.celery_app import app
from PIL import Image
from pymongo import MongoClient
from wordcloud import WordCloud

CLIENT = MongoClient()
MONGO_CONN = CLIENT.bot


@app.task
def tag_cloud():
    data = list()
    cursor = MONGO_CONN.question.find()
    for q in cursor:
        for tag in q["tags"]:
            data.append(tag)

    mask = np.array(Image.open("img/bot.png"))
    wc = WordCloud(background_color="white", max_words=2000, mask=mask)
    wc.generate("\n".join(data))
    wc.to_file("img/tag_cloud.png")
