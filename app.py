from flask import Flask, render_template
import folium
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Coordenadas para exibir no mapa (latitude, longitude)
    latitude = -12.720755
    longitude = -38.938436  # Salvador - BA, por exemplo
    return render_template('index.html', lat=latitude, lon=longitude)

@app.route('/mapa')
def mapa():
    localizacao = [-12.720755,-38.938436]
    
    mapa = folium.Map(location=localizacao, zoom_start=18)

    folium.Marker(location=localizacao,
                  popup='Coqueiros - Ba',
                  tooltip='ANA MARIA DE SOUZA',
                  icon=folium.Icon(color='blue', icon='info-sign')
                  ).add_to(mapa)
    
    mapa_html = mapa._repr_html_()
    
    return render_template('mapa.html', mapa=mapa_html)

if __name__ == '__main__':
    app.run(debug=True)
