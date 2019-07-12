# -*- coding: utf-8 -*-
#

__author__ = 'Corey Lee'

'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    print('Get reponse...')
    return {
        '__template__': 'test.html',
        'users': users
    }