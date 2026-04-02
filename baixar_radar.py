import requests

# URL do radar que o seu TI odeia
url_radar = "https://tilecache.rainviewer.com/v2/radar/nowcast_5/256/1/1/1/2/1_1.png"

try:
    # O GitHub vai baixar a imagem (ele tem acesso livre à internet)
    response = requests.get(url_radar, timeout=15)
    if response.status_code == 200:
        with open("radar_atual.png", "wb") as f:
            f.write(response.content)
        print("Radar baixado com sucesso!")
except Exception as e:
    print(f"Erro no contrabando: {e}")
