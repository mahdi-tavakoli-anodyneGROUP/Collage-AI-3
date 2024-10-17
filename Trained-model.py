from ultralytics import YOLO

# بارگذاری مدل آموزش‌دیده
model = YOLO('YOUR best.pt LOCATION')

# اجرای پیش‌بینی بر روی داده‌های تست
results = model.predict(source='YOUR TEST IMAGES DIRECTORY', save=True)

# نمایش نتایج
for result in results:
    print(result.boxes)  # نمایش جعبه‌های تشخیص یافته
