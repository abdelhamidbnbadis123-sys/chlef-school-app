import streamlit as st

# 1. إعدادات الصفحة الرسمية
st.set_page_config(page_title="نظام القيادة الإدارية - الشلف", layout="wide")

# 2. العلم الجزائري يرفرف
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)

# 3. الترويسة الوطنية
st.markdown("<h2 style='text-align:center; color: #1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)

st.sidebar.title("🛡️ بوابة التحكم")
menu = ["🏠 الرئيسية", "💰 فضاء المقتصد", "🔍 نظام الكودبار", "📦 أمين المخزن", "📚 المكتبة المدرسية", "👨‍🏫 فضاء الأستاذ"]
choice = st.sidebar.radio("اختر القسم:", menu)

# --- منطق الأقسام ---

if choice == "🏠 الرئيسية":
    st.info("مرحباً بك في النظام الرقمي المتكامل للقيادة الإدارية")
    school = st.text_input("📍 يرجى إدخال اسم المؤسسة التعليمية لتفعيل النظام:")
    if school:
        st.success(f"تم تفعيل النظام بنجاح لـ: {school}")
        st.balloons()

elif choice == "💰 فضاء المقتصد":
    st.header("💵 تسيير الميزانية والجرد الآلي")
    st.subheader("📸 ميزة الجرد السريع (تصوير الفاتورة)")
    img_file = st.camera_input("التقط صورة للفاتورة بالجوال للمُعالجة:")
    if img_file:
        st.image(img_file, caption="تم استلام الفاتورة")
        st.warning("جاري تحليل البيانات وتحويلها إلى جدول مصاريف تلقائياً...")

elif choice == "🔍 نظام الكودبار":
    st.header("🏷️ نظام الأرشفة بالكودبار")
    st.write("استخدم هذا القسم لتوليد رموز للأقسام أو التلاميذ.")
    code_text = st.text_input("أدخل النص أو الرقم لتحويله لكودبار:")
    if st.button("توليد الكودبار الآن"):
        st.success(f"تم إنشاء الرمز الرقمي لـ {code_text} جاهز للطباعة.")

else:
    st.warning(f"قسم {choice} قيد التطوير البرمجي حالياً.")

# تذييل احترافي للبيع
st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v1.0 | جميع الحقوق محفوظة لصاحب الفكرة</p>", unsafe_allow_html=True)
