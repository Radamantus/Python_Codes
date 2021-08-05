# Importar as bibliotecas necessárias
from win10toast import ToastNotifier

# Inicializar
toaster = ToastNotifier()

# Configurar
toaster.show_toast(
    'Notificação',
    'Seu computador explodirá em 5 segundos.',
    threaded = True,
    icon_path = None,
    duration = 10 # em segundos
);