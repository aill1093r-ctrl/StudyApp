import time
from plyer import notification

# كود يعمل في الخلفية بشكل مستمر لإرسال التنبيهات
def main():
    while True:
        # هنا يمكنك إضافة منطق الفحص الدائم أو التوقيت
        time.sleep(3600)  # فحص أو تنبيه كل ساعة مثلاً

if __name__ == '__main__':
    main()
