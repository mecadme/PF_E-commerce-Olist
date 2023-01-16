# **Proyecto Grupal: E-commerce Olist**

![img](https://github.com/mecadme/PF_E-commerce-Olist/blob/main/Images/olist%20principal.png?raw=true)

## **Tabla de contenidos**


## **Descripción del problema (Contexto y rol a desarrollar)**

Somos un grupo de 5 integrantes del Bootcamp de Henry, y éste es nuestro Proyecto Final.
- [Damián Buch GitHub](https://github.com/Damiano7)
- [Gisela Medina GitHub](https://github.com/GMDP)
- [Martin Menéndez GitHub](https://github.com/bigdatamartin)
- [Mauro Cadme GitHub](https://github.com/mecadme)
- [Miguel Salas GitHub](https://github.com/Emblask39)

### **Contexto**

>En 2021, las ventas minoristas a través de comercio electrónico significaron un saldo aproximado de 5,2 billones de dólares a nivel mundial y se dice que esta cifra aumentará un 56% en los próximos años, alcanzando los 8,1 billones en 2026.

>Olist es una empresa brasileña que brinda servicios de comercio electrónico para PYMES <i>(Pequeñas y Medianas Empresas)</i> que funciona como un mercado, es decir, funciona como una "tienda de tiendas" donde diferentes vendedores pueden ofrecer sus productos a los consumidores finales.

### **Rol a desarrollar**

Nuestro rol es el de una consultora internacional llamada "Alpha Insights" la cual está conformada por 5 integrantes, cada uno con una especialidad y un puesto de trabajo específico.

Con el objetivo principal de continuar conectando pequeñas empresas (*PYMES*) con mercados más grandes y mejorar la experiencia del usuario, Olist nos contrata como consultores externos para encontrar soluciones innovadoras que permitan a sus usuarios vender sus productos a un mayor número de clientes.
Para lograrlo, Olist nos ha proporcionado sus datos de 2016 a 2018, por lo que deberemos entregar un MVP (*Producto Mínimo Viable*).

![image](https://user-images.githubusercontent.com/112119779/212675644-ffa8096b-481f-403b-a853-b7922e65d2b5.png)

![image](https://user-images.githubusercontent.com/112119779/212659726-bac0895c-6bd2-420e-bf35-f8604591a387.png)


## **Propuesta de trabajo**  

Nuestra propuesta se basa primordialmente en:

- `Recopilar, depurar y disponibilizar la información:` 
    * Se realizó un Análisis Exploratorio de Datos (*EDA*) y se elabaoró un reporte de Calidad de Datos (datos faltantes, outliers, valores nulos), el criterio utilizado para su manejo, además de un diccionario de datos.
    * Se crearon Data Pipelines para el ETL (Proceso de Extracción, Transformación y Carga de datos).
    - Se generó la base de datos (*DataWarehouse*) de los diferentes csv provistos y las fuentes alternativas que fueren incorporadas. La misma se encuentra corriendo en un proveedor de servicios en la nube (*AWS*) y On-premise (de manera local).
    - Automatización del flujo de trabajo (*Airflow*). 

- `Reporte y análisis significativos:` 
    * El análisis cuenta con un **dashboard** que brinda información concisa para la toma de decisiones de negocio exponiendo métricas y **KPIs** claves para el buen desempeño y mejora del e-commerce.

- `Entrenamiento y puesta en producción de un modelo de machine learning`: 
    * Se implementó un **Modelo de Recomendación de Productos** y un modelo de **Análisis de Sentimiento** sobre reviews.

## **Datasets y fuentes complementarias** 

### **Fuente principal**  

- [Dataset Olist](https://drive.google.com/file/d/1YiZqsF_F4OIdjLCq4sba2XXjPxU7LlgE/view?usp=sharing)

## **Contáctanos**

[![image](https://user-images.githubusercontent.com/112119779/212675006-07de84ae-d004-4a08-979f-2d7bbc139290.png)](https://alphainsights.online/)
