


# header route
@app.route("/")
def get_api_response_header():
    return dict(api_response.headers)


# payload route
@app.route("/data")
def get_api_response():
    data = api_response.text
    decoded_data = json.loads(data)
    return decoded_data

