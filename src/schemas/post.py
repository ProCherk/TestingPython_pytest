POST_SCHEMA = {
    "meta": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "gender": {"type": "string"},
        "status": {"type": "string"},
    },
    "required": ["id", "name", "email"]
}

'''
{
    'meta': {
        'pagination': {
            'total': 1993,
            'pages': 200,
            'page': 1,
            'limit': 10,
            'links': {
                'previous': None,
                'current': 'https://gorest.co.in/public/v1/users?page=1',
                'next': 'https://gorest.co.in/public/v1/users?page=2'
            }
        }
    },
 'data': [
     {'id': 3279, 'name': 'Lila Bhat', 'email': 'lila_bhat@hahn.info', 'gender': 'male', 'status': 'active'},
          {'id': 3278, 'name': 'Tanirika Gupta', 'email': 'gupta_tanirika@cummings.net', 'gender': 'female',
           'status': 'inactive'},
          {'id': 3277, 'name': 'Bharadwaj Kakkar', 'email': 'bharadwaj_kakkar@swaniawski.info', 'gender': 'male',
           'status': 'inactive'},
          {'id': 3275, 'name': 'Mangala Devar', 'email': 'mangala_devar@rempel-fay.com', 'gender': 'male',
           'status': 'inactive'},
          {'id': 3136, 'name': 'Harinakshi Ahluwalia', 'email': 'harinakshi_ahluwalia@hayes.com', 'gender': 'male',
           'status': 'active'},
          {'id': 3134, 'name': 'Suresh Pothuvaal', 'email': 'pothuvaal_suresh@mohr.io', 'gender': 'male',
           'status': 'inactive'},
          {'id': 3133, 'name': 'Abhirath Chopra', 'email': 'abhirath_chopra@schmeler-kautzer.org', 'gender': 'male',
           'status': 'active'},
          {'id': 3132, 'name': 'Niro Nambeesan', 'email': 'nambeesan_niro@lindgren.io', 'gender': 'female',
           'status': 'active'},
          {'id': 3129, 'name': 'Mayoor Tagore', 'email': 'mayoor_tagore@zboncak.org', 'gender': 'female',
           'status': 'active'},
          {'id': 3127, 'name': 'Geetanjali Chaturvedi LLD', 'email': 'lld_chaturvedi_geetanjali@davis.name',
           'gender': 'female', 'status': 'inactive'}]}

'''
