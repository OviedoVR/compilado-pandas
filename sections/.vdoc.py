# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
#
#
#
#
#
#
#
preco_streamings = pd.read_excel('dados/preco_servicos_streaming/Streaming_prices.xlsx')
preco_streamings
#
#
#
#
#
vendas_europa = pd.read_csv('dados/vendas/EuropeSalesRecords.csv')
vendas_europa
#
#
#
#
enderecos_IP = pd.read_fwf('dados/enderecos_ip/ip_addresses.txt', delimiter='; ')
enderecos_IP
#
#
#
#
#
# OBS --- é preciso ter tabelas HTML para ler

URL = 'https://pt.wikipedia.org/wiki/Demografia_do_Brasil'

crescimento_populacional = pd.read_html(URL)[3]
crescimento_populacional
#
#
#
#
#
#
crescimento_populacional = pd.read_html(URL)
len(crescimento_populacional)
#
#
#
#
#
corridas_app = pd.read_json('dados/corridas/corridas.json')
corridas_app
#
#
#
#
#
#
