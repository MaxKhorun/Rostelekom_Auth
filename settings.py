import os
# from dotenv import load_dotenv
# load_dotenv()

login_email_1 = os.getenv(r"EMAIL_1")
login_1 = os.getenv("LOGIN_FOR_EMAIL_1")
passw_email_1 = os.getenv("PASSW_EMAIL_1")

login_email_2 = os.getenv("EMAIL_2")
login_2 = os.getenv("LOGIN_FOR_EMAIL_2")
passw_email_2 = os.getenv("PASSW_EMAIL_2")

phone_1 = os.getenv("PHONE_1")
login_phone_1 = os.getenv("LOGIN_FOR_PHONE_1")
pass_phone_1 = os.getenv("PASSW_PHONE_1")

phone_2 = os.getenv("PHONE_2")
pass_phone_2 = os.getenv("PASSW_PHONE_2")




# пароли_для_проверки_сценария_восстановления
pass_for_check_1 = os.getenv("PASSW_1_1")
pass_for_check_2 = os.getenv("PASSW_1_2")
pass_for_check_3 = os.getenv("PASSW_1_3")

# URLS to check:
elk_web, elk_check_part = "https://lk.rt.ru/", "lk.rt.ru" # ЕЛК Web
onlime_web, online_check_part = "https://my.rt.ru/", "my.rt.ru" # Онлайм Web
start_web, start_check_part = "https://start.rt.ru/", "start.rt.ru" # Старт Web
smart_hone_web, smart_check_part = "https://lk.smarthome.rt.ru/", "lk.smarthome.rt.ru" # Умный дом Web
keys_web, keys_check_part = "https://key.rt.ru/", "key.rt.ru" # Ключ Web


# test_neg_data

long_email = 'ecvbaejkrbfvbaervbjhasdvcjarfvhgbaeruigbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbvyualerbvalebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhebhaerbvaerbvbaerkvbjkaerbvjkaerbvjkeabv@ghjkruoiwerhhfaowerhgivaololololololololololololololololol.ru'
long_name = 'Ишмухостирунеканаданадридагуфолекуил'