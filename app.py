import streamlit as st

# إعداد الصفحة الرسمية
st.set_page_config(page_title="نظام الإدارة المدرسية - الشلف", layout="wide")

# 1. العلم الجزائري يرفرف
st.markdown('<div style="display: flex; justify-content: center;"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)

# 2. العناوين الرسمية
st.markdown("<h2 style='text-align: center; color: #1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1e5631;'>وزارة التربية الوطنية - مديرية التربية لولاية الشلف</h3>", unsafe_allow_html=True)

st.write("---")

# 3. إدخال اسم المؤسسة
school_name = st.text_input("📍 يرجى إدخال اسم المؤسسة التعليمية للدخول:")

if school_name:
    st.success(f"مرحباً بك في النظام الرقمي لـ: {school_name}")
    
    # 4. شبكة الأزرار بنظام الصلاحيات
    st.markdown("### لوحة التحكم المركزية:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.button("💰 فضاء المقتصد", use_container_width=True)
        st.button("📝 نائب المدير", use_container_width=True)
        st.button("📦 أمين المخزن", use_container_width=True)
        st.button("👨‍🏫 فضاء الأستاذ", use_container_width=True)

    with col2:
        st.button("🏢 مدير المؤسسة", use_container_width=True)
        st.button("👷 الإدارة والعمال", use_container_width=True)
        st.button("📚 المكتبة المدرسية", use_container_width=True)
        st.button("🔍 نظام الكودبار", use_container_width=True)
