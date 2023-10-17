import bottle as btl

app = application = btl.Bottle()

filepath = "/styles..css"
@app.route('/static/<filepath:path>')
def static_CSS(filepath):
    return static_file(filepath, root='/static')
    
btl.template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<form action = ""></form>
<button></button>

</body>
</html>



""")

btl.run(host='localhost', port=8080)