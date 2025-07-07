from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update

# 🪖 الكلمات المحظورة (طلقات محظورة)
banned_words = [
    "قاسم سليماني", "ابو مهدي المهندس", "حسن نصرالله", "عماد مغنية", "جهاد مغنية",
    "اسماعيل قاآني", "ابو علي العسكري", "ابو فدك", "ابو ولاء الولائي", "السيد هاشم صفي الدين",
    "حزب الله", "كتائب حزب الله", "عصائب اهل الحق", "سرايا السلام", "الجهاد الاسلامي",
    "سرايا القدس", "كتائب القسام", "حماس", "داعش", "القاعدة", "تنظيم الدولة", "طالبان",
    "انصار الله", "مقاومة", "مجاهد", "مجاهدين", "قتال", "قتل", "جهاد", "استشهاد",
    "شهيد", "شهداء", "تفجير", "انفجار", "عبوة", "عبوات", "مسلحة", "سلاح", "اسلحة",
    "صاروخ", "صواريخ", "قنبلة", "قنابل", "عملية استشهادية", "مفخخة", "عملية نوعية",
    "عملية جهادية", "طائرة مسيرة", "مسيرة", "قنص", "قناص", "اطلاق نار", "اشتباك",
    "الاجهزة الامنية", "الارهاب", "ارهابي", "متفجرات", "دم", "دماء", "مذبوح", "ذبيح",
    "جريمة", "قتل جماعي", "مجزرة", "اغتيال", "تصفية", "اعدام", "الاحتلال", "الصهاينة",
    "صهيوني", "الشيطان الاكبر", "العدو الصهيوني", "الكيان الصهيوني", "الكيان المحتل",
    "العدو الامريكي", "احراق العلم"
]

# 🪄 دالة فلترة ذكية تقطع الكلمات تلقائياً
def smart_censor(text):
    for word in banned_words:
        if word in text:
            parts = word.split()
            modified_parts = []
            for part in parts:
                if len(part) > 1:
                    modified_part = part[0] + "ـ.ـ" + part[1:]
                else:
                    modified_part = part
                modified_parts.append(modified_part)
            modified_word = ' '.join(modified_parts)
            text = text.replace(word, modified_word)
    return text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    cleaned_text = smart_censor(text)
    await update.message.reply_text(cleaned_text)

def main():
    app = ApplicationBuilder().token("8001794158:AAHSB4-RXsOIhfUEABeal1M4cMHmRlnHk7A").build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()
