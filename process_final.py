import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Carregar e filtrar dados (TERRA)
df_aod_terra = pd.read_csv('MOD043ktemporal_serie_manaus_aod2010_2020.csv').dropna()

# Carregar e filtrar dados (AQUA)
df_aod_aqua = pd.read_csv('MYD043ktemporal_serie_manaus_aod2010_2020.csv').dropna()

print("TERRA:", len(df_aod_terra))
print("AQUA:", len(df_aod_aqua))

# Remover outliers e converter datas (TERRA)
df_aod_terra = df_aod_terra[(df_aod_terra["AOD"] <= 5) & (df_aod_terra["AOD"] >= 0)]
df_aod_terra['date'] = pd.to_datetime(df_aod_terra['date'])

# Remover outliers e converter datas (AQUA)
df_aod_aqua = df_aod_aqua[(df_aod_aqua["AOD"] <= 5) & (df_aod_aqua["AOD"] >= 0)]
df_aod_aqua['date'] = pd.to_datetime(df_aod_aqua['date'])

# Mesclar dados TERRA e AQUA e calcular média
_df2010 = pd.merge(df_aod_aqua, df_aod_terra, on='date', how='outer').sort_values(by='date', ascending=True).fillna(0)
_df2010['mean'] = _df2010.apply(lambda row: row['AOD_x'] if row['AOD_y'] == 0 else
                                row['AOD_y'] if row['AOD_x'] == 0 else
                                (row['AOD_x'] + row['AOD_y']) / 2, axis=1)

# Remover colunas indesejadas
_df2010 = _df2010.drop(columns=["Unnamed: 0_x", "Unnamed: 0_y"], errors='ignore')

# Salvar resultado final
_df2010.to_csv('AOD_manaus_2010_2020_final.csv', index=False)

# Criar gráfico
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='date', y='mean', data=_df2010, color='steelblue')

# Definir rótulos do gráfico
ax.set(xlabel='Time', ylabel='AOD 3 km', title='Time Serie of AOD - Manaus')
plt.show()
