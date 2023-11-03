import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Teste')
    }
    import json
    from validate_docbr import CPF

    def lambda_handler(event, context):
        # Recebe o CPF do usuário
        cpf = event['cpf']

        # Verifica se o CPF é válido
        if CPF().validate(cpf):
            # CPF válido, retorna sucesso
            return {
                'statusCode': 200,
                'body': json.dumps('Usuário autenticado com sucesso!')
            }
        else:
            # CPF inválido, retorna erro
            return {
                'statusCode': 400,
                'body': json.dumps('CPF inválido!')
            }
