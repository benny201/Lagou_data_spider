# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb
from django.http import HttpResponse, JsonResponse
import json
# connect mysql database

conn = MySQLdb.connect("127.0.0.1", "root", "12345", 'lagou', charset="utf8")
cursor = conn.cursor()


def get_company_population(request):

    popu_type = ['少于15人', '15-50人', '50-150人', '150-500人', '500-2000人', '2000人以上']
    # query_sql = " select count(*) from where population = {0}".format('1')

    result = []

    for type in popu_type:
        query_sql = """select count(*) from company_list where population=\'{0}\' """.format(type)
        cursor.execute(query_sql)
        # print(cursor.fetchone()[0])
        result.append({
            "range": type,
            "value": cursor.fetchone()[0]
        })

    # return result
    message = 'ok'
    if not result:
        message = 'Data Not Found'

    return JsonResponse({
        'message': message,
        'data': result
    })


# get_company_population()
# print(get_company_population())