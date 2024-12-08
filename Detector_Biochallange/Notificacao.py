from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    "AVISO DE NOTIFICACAO",
    "body",
    duration = 20,
    icon_path = "icon.ico",
    threaded = True,
)