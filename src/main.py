from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client, Client
import base64
from datetime import datetime
from yolo_processamento import Processamento

#URL
url = 'https://ggztsxcacwzichpigsgv.supabase.co'

#Chave
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdnenRzeGNhY3d6aWNocGlnc2d2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njc3MzEyMywiZXhwIjoyMDAyMzQ5MTIzfQ.n6u7944WigvWvcaz6k410gH9_0krTLSIAyA6gKeY964'

#Criando um cliente
client: Client = create_client(url, key)

#Nome do Banco
banco = 'Ponderada'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salvar-imagem', methods=['POST'])
def salvar_imagem():
    print("Entrou na API")
    imagem_data = request.data.decode('utf-8')
    yolo_processada = Processamento(imagem_data)
    # _, imagem_base64 = yolo_processada.split(',', 1)
    imagem_bytes = base64.b64decode(yolo_processada)
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client.storage.from_(banco).upload(data_hora_atual, imagem_bytes)
    return redirect('/')

app.run(host="0.0.0.0", port=3000, debug=True)