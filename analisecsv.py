import pandas as pd
import matplotlib.pyplot as plt

def analisar_csv(arquivo_csv):
    # Ler o arquivo CSV
    df = pd.read_csv(arquivo_csv)
    
    print("ESTATÍSTICAS DO DATASET")
    print("=" * 50)
    print(f"Shape: {df.shape}")
    print(f"\nColunas: {list(df.columns)}")
    print(f"\nTipos de dados:\n{df.dtypes}")
    print(f"\nEstatísticas descritivas:\n{df.describe()}")
    print(f"\nValores nulos:\n{df.isnull().sum()}")
    
    # Gerar gráfico simples
    if len(df.columns) >= 2:
        plt.figure(figsize=(10, 6))
        df[df.columns[1]].hist(bins=20)
        plt.title(f'Distribuição de {df.columns[1]}')
        plt.savefig('analise.png')
        print("\n📈 Gráfico salvo como 'analise.png'")

# analisar_csv('dados.csv')
