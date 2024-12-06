from kivy.config import Config

# Definir a resolução para FHD (1080x1920) em modo retrato
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '1920')
Config.set('graphics', 'resizable', False)  # Desativa redimensionamento
from kivy.core.window import Window

# Ativar modo tela cheia
Window.fullscreen = 'auto'