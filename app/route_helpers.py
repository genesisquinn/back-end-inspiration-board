from flask import abort, make_response


def create_model(cls, request_body):
    try:
        model = cls.from_dict(request_body)
    except (KeyError, TypeError):
        abort(make_response({"details": "Invalid data"}, 400))
    return model


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    return model



