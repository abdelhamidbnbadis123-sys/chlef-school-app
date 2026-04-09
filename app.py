import streamlit as st

# إعدادات الواجهة الرسمية
st.set_page_config(page_title="نظام القيادة الإدارية - الشلف", layout="wide")

# العلم الجزائري يرفرف
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="120"></div>', unsafe_allow_html=True)

# الترويسة الوطنية
st.markdown("<h2 style='text-align:center; color: #1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)

# قائمة الصلاحيات الجانبية
menu = ["🏠 الرئيسية", "💰 فضاء المقتصد", "🔍 نظام الكودبار"]
choice = st.sidebar.selectbox("قائمة الخدمات", menu)

if choice == "🏠 الرئيسية":
    st.info("مرحباً بك في النظام الرقمي للمؤسسة")
    school = st.text_input("📍 أدخل اسم المؤسسة:")
    if school: st.success(f"تم التفعيل لـ: {school}")

elif choice == "💰 فضاء المقتصد":
    st.header("تسيير الميزانية والجرد الآلي")
    # فتح كاميرا الهاتف مباشرة
    img_file = st.camera_input("📸 صوّر الفاتورة الآن")
    if img_file:
        st.image(img_file, caption="تم التقاط الفاتورة بنجاح")
        st.warning("جاري تحليل البيانات...")

elif choice == "🔍 نظام الكودبار":
    st.header("توليد الكودبار")
    st.text_input("أدخل رمز التلميذ أو القسم:")
    st.button("توليد الصورة")
    
