import qrcodeT


name = "Elena Tenina"
telegram_account = "a_tenina"

application_msg = f"Привет, я {name} прошу добавить меня в Кодильню, мой телеграмм http://t.me/{telegram_account}"
qrcodeT.qrcodeT(application_msg)
