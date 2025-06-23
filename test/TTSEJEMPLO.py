import pvorca
import wave
import os
import numpy as np
# PARA CREAR AUDIO, CAMBIAR EL TEXTO QUE DICE MAMARRE MAMARRE MAMARRE POR LO QUE QUIERES QUE EL BOT DIGA!!!!!!!
# Configuración de rutas
output_dir = r'C:\Users\tente\OneDrive\Escritorio\BOCETO 1 MIKUMPANION\audios_generados'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'output.wav')

try:
    # 1. Sintetizar audio
    orca = pvorca.create(access_key='n+CCrhVyfkit8YOgXnzsljdJBzODewBg3pDaMEWvtpWf6zhMOeN/EQ==')
    result = orca.synthesize(text='mamarre mamarre mamarre')
    
    # 2. Extraer el componente de audio correctamente
    if isinstance(result, tuple) and len(result) >= 1:
        audio_component = result[0]  # Primer elemento es el audio
        
        # Convertir a bytes seguro
        if isinstance(audio_component, list):
            audio_array = np.array(audio_component, dtype=np.int16)
            audio_data = audio_array.tobytes()
        else:
            audio_data = bytes(audio_component)
    else:
        audio_data = bytes(result)
    
    # 3. Guardar como WAV
    with wave.open(output_path, 'wb') as f:
        f.setnchannels(1)      # Mono
        f.setsampwidth(2)      # 16-bit
        f.setframerate(22050)   # Standard sample rate
        f.writeframes(audio_data)
    
    print(f"✅ Audio guardado correctamente en: {output_path}")

except Exception as e:
    print(f"❌ Error: {str(e)}")
    if 'result' in locals():
        print("Tipo de resultado:", type(result))
        print("Estructura completa:", str(result)[:200] + "...")
