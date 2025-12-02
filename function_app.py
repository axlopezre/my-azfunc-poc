import azure.functions as func
from azure.functions import FunctionApp

app = FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="HttpExample", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def http_example(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hola {name}! Tu función de Azure está funcionando correctamente 🎉")
    else:
        return func.HttpResponse(
            "Por favor pasa un nombre en la query string o en el body (JSON) con 'name'",
            status_code=400
        )
