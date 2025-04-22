import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def carregar_dados(caminho_arquivo):
    """Carrega os dados de vendas a partir de um arquivo CSV"""
    df = pd.read_csv(caminho_arquivo)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Valor Total'] = df['Quantidade'] * df['Valor Unitário']
    return df

def analisar_vendas_por_vendedor(df):
    """Retorna um DataFrame com o total de vendas por vendedor"""
    return df.groupby('Vendedor').agg({
        'Quantidade': 'sum',
        'Valor Total': 'sum'
    }).sort_values('Valor Total', ascending=False)

def analisar_vendas_por_regiao(df):
    """Retorna um DataFrame com o total de vendas por região"""
    return df.groupby('Região').agg({
        'Quantidade': 'sum',
        'Valor Total': 'sum'
    }).sort_values('Valor Total', ascending=False)

def analisar_tendencia_mensal(df):
    """Retorna um DataFrame com o total de vendas por mês"""
    df['Mês'] = df['Data'].dt.to_period('M')
    return df.groupby('Mês').agg({
        'Quantidade': 'sum',
        'Valor Total': 'sum'
    })

def gerar_grafico_vendas_mensais(df):
    """Gera um gráfico de linha com as vendas mensais"""
    df_mensal = analisar_tendencia_mensal(df)
    df_mensal['Valor Total'].plot(
        kind='line',
        title='Vendas Mensais',
        xlabel='Mês',
        ylabel='Valor Total (R$)',
        figsize=(10, 6),
        marker='o'
    )
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('relatorios/vendas_mensais.png')
    plt.close()

if __name__ == "__main__":
    # Exemplo de uso
    df_vendas = carregar_dados('data/vendas.csv')
    print("\nVendas por Vendedor:")
    print(analisar_vendas_por_vendedor(df_vendas))
    
    print("\nVendas por Região:")
    print(analisar_vendas_por_regiao(df_vendas))
    
    print("\nTendência Mensal:")
    print(analisar_tendencia_mensal(df_vendas))
    
    gerar_grafico_vendas_mensais(df_vendas)
    print("\nGráfico de vendas mensais gerado em 'relatorios/vendas_mensais.png'")