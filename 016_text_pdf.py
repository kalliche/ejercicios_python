'''La biblioteca para extraer texto de python pypdf2 '''

import tabula
import pandas as pd

# Ruta del PDF con las tablas o formularios
pdf_path = "./1006946511.pdf"  # Reemplaza 'ruta_del_archivo.pdf' con la ubicación de tu archivo PDF

# Leer las tablas del PDF y almacenarlas en una lista de DataFrames
tablas = tabula.read_pdf(pdf_path, pages='all')

# Concatenar todos los DataFrames en uno solo
combined_dataframe = pd.concat(tablas)

# Exportar el DataFrame combinado a un archivo CSV
csv_file = "tabla_completa.csv"
combined_dataframe.to_csv(csv_file, index=False)

print(f"Tabla combinada exportada a '{csv_file}'")

