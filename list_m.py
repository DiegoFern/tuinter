
from flask import (
    Flask,
    jsonify,
    url_for,
    redirect,
    request,
    session)

from models import *

class list_messages:
    def get():
        mssg = [m.json()
                    for U in User.query.get(session['email']).following
                    for m in U.message
                ]+list(map(lambda x:x.json(),User.query.get(session['email']).message))
        return {
            'user' : 'user',
            'messages' : mssg
        }

    def post():
        import ast
        args = ast.literal_eval(request.data.decode())
        mssg = Message(text=args['message'],editor=(session['email']))
        db.session.add(mssg)
        db.session.commit()
        response = jsonify({})
        response.status_code = 201
        return {}

    def delete():
        object = Message.get(id=request.args['message_id'])
        if object:
            db.session(object.delete)



