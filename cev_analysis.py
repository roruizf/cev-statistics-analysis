import pandas as pd


class CEV:
    def cev_dataframe(self, file):
        # Creating dataframe
        df = pd.read_csv(file, encoding='utf-8')

        # Creating and applying categories for Identificación Vivienda
        df['Identificación Vivienda'] = df['Identificación Vivienda'].astype(
            "category")

        # Creating and applying categories for Proyecto
        df['Proyecto'] = df['Proyecto'].astype("category")

        # Creating and applying categories for Tipología
        df['Tipología'] = df['Tipología'].astype("category")

        # Creating and applying categories for Comuna
        df['Comuna'] = df['Comuna'].astype("category")

        # Creating and applying categories for regions
        region_trans = {'Región de Arica y Parinacota': "Arica y Parinacota",
                        'Región de Tarapacá': 'Tarapacá',
                        'Región de Antofagasta': 'Antofagasta',
                        'Región de Atacama': 'Atacama',
                        'Región de Coquimbo': 'Coquimbo',
                        'Región de Valparaíso': 'Valparaíso',
                        'Región Metropolitana de Santiago': 'Metropolitana',
                        "Región del Libertador Gral. Bernardo O'Higgins": "O'Higgins",
                        'Región del Maule': 'Maule',
                        'Región de Ñuble': "Ñuble",
                        'Región del Biobío': "Biobío",
                        'Región de la Araucanía': "Araucanía",
                        'Región de Los Ríos': "Los Ríos",
                        'Región de Los Lagos': "Los Lagos",
                        'Región Aysén del Gral. Carlos Ibáñez del Campo': "Aysén",
                        'Región de Magallanes y de la Antártica Chilena': "Magallanes"}
        df['Región'] = df['Región'].replace(region_trans)
        region_category = pd.CategoricalDtype(categories=['Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaíso', 'Metropolitana',
                                                          "O'Higgins", 'Maule', 'Ñuble', 'Biobío', 'Araucanía', 'Los Ríos', 'Los Lagos', 'Aysén', 'Magallanes'], ordered=True)
        df['Región'] = df['Región'].astype(region_category)

        # Creating and applying categories for status
        status_category = pd.CategoricalDtype(
            categories=['Pre-calificación', 'Calificación'], ordered=True)
        df['Status'] = df['Status'].astype(status_category)

        # Creating and applying categories for CE and CEE
        my_categories = pd.CategoricalDtype(
            categories=['A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I'], ordered=True)
        df['CE'] = df['CE'].astype(my_categories)
        df['CEE'] = df['CEE'].str.replace('--', 'N/A')
        my_categories = pd.CategoricalDtype(
            categories=['A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'N/A'], ordered=True)
        df['CEE'] = df['CEE'].astype(my_categories)

        print(
            f"A dia de hoy, {df.shape[0]} viviendas han participado de este proceso, las cuales pertenecen a {df['Proyecto'].unique().shape[0]} proyectos diferentes.")
        print(
            f"  - Número de viviendas PRE-calificadas: {df[df['Status']=='Pre-calificación'].shape[0]} viviendas")
        print(
            f"  - Número de viviendas Calificadas: {df[df['Status']=='Calificación'].shape[0]} viviendas")
        print(
            f"Las viviendas se encuentran repartidas en {df['Comuna'].unique().shape[0]} comunas y {df['Región'].unique().shape[0]} regiones del pais.")
        return df


# ahorro_energetico = {"A+": ">85%",
#                     "A": ">70% & <=85%",
#                     "B": ">55% & <=70%",
#                     "C": ">40% & <=55%",
#                     "D": ">20% & <=40%",
#                     "E": ">-10% & <=20%",
#                     "F": ">-35% & <=10%",
#                     "G": "<=35%"
#                     }
