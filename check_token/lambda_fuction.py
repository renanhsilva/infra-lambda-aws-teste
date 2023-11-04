import json
import jwt

SECRET_NAME = "token-secret"  # Nome do segredo no AWS Secret Manager

def lambda_handler(event, context):
    # Recebe o token JWT da entrada do evento
    jwt_token = event.get("token")

    if not jwt_token:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Token JWT não fornecido"})
        }

    # Recupera o segredo do AWS Secret Manager
    secret_value = get_secret_value(SECRET_NAME)

    if not secret_value:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Falha ao recuperar o segredo"})
        }

    secret = secret_value["SecretString"]

    # Valida o token JWT
    valid, cpf = validate_jwt_token(jwt_token, secret)

    if valid:
        return {
            "statusCode": 200,
            "body": json.dumps({"cpf": cpf})
        }
    else:
        return {
            "statusCode": 401,
            "body": json.dumps({"error": "Token JWT inválido ou expirado"})
        }

def get_secret_value(secret_name):
    # Conecta-se ao AWS Secret Manager e recupera o valor do segredo
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)

    if "SecretString" in response:
        return json.loads(response["SecretString"])
    else:
        return None
