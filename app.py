import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==========================================
# داده‌های واقعی ۶ ماه اول سال (استخراج شده از فاکتورها)
# ==========================================
historical_data = pd.DataFrame(
    {
        "ماه": [
            "فروردین",
            "اردیبهشت",
            "خرداد",
            "تیر",
            "مرداد",
            "شهریور",
        ],
        "حجم_فروش_MWh": [166.0, 166.0, 148.0, 163.68, 174.84, 178.56],
        "نرخ_میانگین_تومان": [3500, 4777, 7500, 9500, 14269, 7475],
        "درآمد_میلیون_تومان": [581.0, 793.0, 1110.0, 1554.96, 2494.85, 1334.73],
        "خریداران_عمده": [
            "فولاد / سیمان",
            "فولاد سیرجان",
            "صنایع معدنی",
            "فولاد سیرجان ایرانیان",
            "صبا فولاد / پاسارگاد / سیمان شمال",
            "کروز / تجارت مهراز صفا",
        ],
    }
)


def render_financial_strategy_tab():
    st.markdown(
        "## 📈 دستیار تصمیم‌گیری عرضه و استراتژی مالی بورس انرژی (مهر ماه)"
    )

    # 1. بخش کارت‌های کلیدی ۶ ماهه
    col1, col2, col3, col4 = st.columns(4)
    total_energy = historical_data["حجم_فروش_MWh"].sum()
    total_revenue = historical_data["درآمد_میلیون_تومان"].sum()
    avg_price = (
        historical_data["درآمد_میلیون_تومان"].sum()
        * 1000
        / (total_energy * 1000)
    ) * 1000

    col1.metric("مجموع حجم عرضه ۶ ماهه", f"{total_energy:,.1f} MWh")
    col2.metric(
        "مجموع درآمد ناخالص", f"{total_revenue / 1000:,.2f} میلیارد تومان"
    )
    col3.metric("میانگین موزون نرخ ۶ ماهه", f"{avg_price:,.0f} تومان/kWh")
    col4.metric("بالاترین نرخ کشف‌شده (مرداد)", "۱۴,۵۰۰ تومان")

    st.markdown("---")

    # 2. نمودار روند تحولات قیمت و درآمد
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        fig_price = px.line(
            historical_data,
            x="ماه",
            y="نرخ_میانگین_تومان",
            markers=True,
            title="روند کشف نرخ بورس سبز (تومان بر کیلووات‌ساعت)",
            color_discrete_sequence=["#FBBF24"],
        )
        fig_price.update_layout(
            template="plotly_dark",
            font_family="Vazirmatn",
            yaxis_title="نرخ (تومان)",
        )
        st.plotly_chart(fig_price, use_container_width=True)

    with col_chart2:
        fig_rev = px.bar(
            historical_data,
            x="ماه",
            y="درآمد_میلیون_تومان",
            title="درآمد ماهانه حاصل از فروش برق (میلیون تومان)",
            color="درآمد_میلیون_تومان",
            color_continuous_scale="Viridis",
        )
        fig_rev.update_layout(
            template="plotly_dark",
            font_family="Vazirmatn",
            yaxis_title="میلیون تومان",
        )
        st.plotly_chart(fig_rev, use_container_width=True)

    # 3. شبیه‌ساز و استراتژیست فروش مهر ماه
    st.markdown("### 🎯 شبیه‌ساز استراتژی عرضه در مهر ماه")

    sim_col1, sim_col2 = st.columns([1, 2])

    with sim_col1:
        st.info("⚙️ تنظیمات سناریو عرضه مهر")
        est_production = st.slider(
            "پیش‌بینی حجم تولید مهر (MWh):",
            min_value=100.0,
            max_value=170.0,
            value=138.0,
            step=1.0,
        )

        strategy_mode = st.selectbox(
            "استراتژی قیمت‌گذاری:",
            [
                "سناریوی محافظه‌کارانه (فروش قطعی و سریع)",
                "سناریوی متعادل و متناسب با بازار (پیشنهادی)",
                "سناریوی تهاجمی (حداکثرسازی سود)",
                "سفارشی (دستی)",
            ],
        )

        if "محافظه‌کارانه" in strategy_mode:
            target_price = 5800
        elif "متعادل" in strategy_mode:
            target_price = 6900
        elif "تهاجمی" in strategy_mode:
            target_price = 8200
        else:
            target_price = st.number_input(
                "نرخ پیشنهادی مدنظر (تومان):", value=7000, step=100
            )

    with sim_col2:
        # محاسبات شبیه‌سازی
        est_revenue_toman = (est_production * 1000) * target_price
        est_revenue_million = est_revenue_toman / 1_000_000

        st.markdown(f"""
        <div style="background-color: #1E293B; border-radius: 12px; padding: 20px; border-left: 5px solid #FBBF24;">
            <h4 style="color: #FBBF24; margin-top: 0;">📊 نتیجه شبیه‌سازی مهر ماه:</h4>
            <ul style="line-height: 2;">
                <li>حجم برآوردی عرضه: <b>{est_production:,.1f} MWh</b> ({est_production * 1000:,.0f} kWh)</li>
                <li>نرخ مفروض هر کیلووات‌ساعت: <b>{target_price:,.0f} تومان</b></li>
                <li>درآمد برآوردی مهر ماه: <b style="color: #34D399; font-size: 1.2rem;">{est_revenue_million:,.1f} میلیون تومان</b> ({est_revenue_million / 1000:,.2f} میلیارد تومان)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 💡 پیشنهاد استراتژی عرضه پلکانی به کارگزاری:")
        p1_vol = est_production * 0.50
        p2_vol = est_production * 0.30
        p3_vol = est_production * 0.20

        st.write(
            f"🔹 **پله اول (پایه - ۵۰٪):** `{p1_vol:.1f} MWh` با نرخ **۶,۲۰۰ تومان** (تضمین فروش)"
        )
        st.write(
            f"🔹 **پله دوم (هدف - ۳۰٪):** `{p2_vol:.1f} MWh` با نرخ **۷,۲۰۰ تومان** (خریداران عمده فولادی)"
        )
        st.write(
            f"🔹 **پله سوم (حداکثری - ۲۰٪):** `{p3_vol:.1f} MWh` با نرخ **۸,۱۰۰ تومان** (پیک تقاضای اواخر ماه)"
        )
