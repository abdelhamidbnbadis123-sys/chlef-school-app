import streamlit as st

# إعدادات الواجهة الرسمية
st.set_page_config(page_title="نظام القيادة الإدارية - الشلف", layout="wide")

# العلم الجزائري يرفرف
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="120"></div>', unsafe_allow_html=True)

# الترويسة الوطنية
st.markdown("<h2 style='text-align:center; color: #1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)

# قائمة الصلاحيات
menu = ["🏠 الرئيسية", "💰 فضاء المقتصد", "🔍 نظام الكودبار", "📦 أمين المخزن"]
choice = st.sidebar.selectbox("قائمة الخدمات", menu)

if choice == "🏠 الرئيسية":
    st.info("مرحباً بك في النظام الرقمي المتكامل للمؤسسة التعليمية")
    school = st.text_input("📍 أدخل اسم المؤسسة لتفعيل النظام:")
    if school:
        st.success(f"تم تفعيل النظام لـ: {school}")

elif choice == "💰 فضاء المقتصد":
    st.header("تسيير الميزانية والجرد الآلي بالفواتير")
    # هذه هي الميزة التي سنبيعها: كاميرا الهاتف
    img_file = st.camera_input("📸 صوّر فاتورة المقتنيات الآن")
    if img_file:
        st.image(img_file, caption="جاري تحليل الفاتورة لاستخراج البيانات...")
        st.warning("تنبيه: سيقوم النظام بتحويل هذه الصورة إلى جدول بيانات تلقائياً.")

elif choice == "🔍 نظام الكودبار":
    st.header("توليد الكودبار للأرشيف والتلاميذ")
    id_code = st.text_input("أدخل رقم التلميذ أو رمز الملف:")
    if st.button("توليد الصورة"):
        st.success(f"تم إنشاء الرمز {id_code} بنجاح للطباعة")
