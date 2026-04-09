import streamlit as st
from PIL import Image

st.set_page_config(page_title="نظام القيادة الإدارية - الشلف", layout="wide")

# الواجهة الرسمية مع العلم يرفرف
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="120"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)

# قائمة المهام الجانبية
menu = ["الرئيسية", "💰 فضاء المقتصد", "📦 أمين المخزن", "🔍 نظام الكودبار"]
choice = st.sidebar.selectbox("القائمة الرئيسية", menu)

if choice == "الرئيسية":
    st.info("مرحباً بك في نظام تسيير المؤسسات التربوية")
    st.write("استخدم القائمة الجانبية للتنقل بين الأقسام")

elif choice == "💰 فضاء المقتصد":
    st.header("تسيير الميزانية والجرد الآلي")
    
    # ميزة تصوير الفاتورة
    st.subheader("📸 تصوير فاتورة جديدة")
    img_file = st.camera_input("التقط صورة للفاتورة بالجوال")
    
    if img_file:
        st.image(img_file, caption="تم التقاط الفاتورة")
        st.warning("جاري استخراج النص وتحويله إلى جرد تلقائي... (هذه الميزة تجريبية)")
        # هنا سنضيف لاحقاً كود EasyOCR لقراءة الأسعار والكميات

elif choice == "🔍 نظام الكودبار":
    st.header("توليد الكودبار للتلاميذ والأقسام")
    name = st.text_input("اسم التلميذ أو رقم القسم:")
    if st.button("توليد كودبار"):
        st.success(f"تم إنشاء كود خاص بـ {name}")
        # هنا سنضيف كود توليد صورة الكودبار للطباعة
