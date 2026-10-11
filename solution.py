import datetime
import requests


def cotar():
    hoje = datetime.date.today()
    url_base = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/"
        "versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)"
    )

    cotacoes = []

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)
        data = dia.strftime("%m-%d-%Y")

        parametros = {
            "@dataCotacao": f"'{data}'",
            "$format": "json"
        }

        resposta = requests.get(url_base, params=parametros)
        resposta.raise_for_status()

        dados = resposta.json()["value"]

        if dados:
            cotacoes.append({
                "data": dia.strftime("%Y-%m-%d"),
                "cotacao_compra": dados[-1]["cotacaoCompra"]
            })

    return cotacoes
