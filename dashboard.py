import streamlit as st
import pandas as pd

st.set_page_config(page_title="DAZI Paid Search Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');
    .stApp { font-family: 'DM Sans', sans-serif; }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid rgba(148,163,184,0.12); border-radius: 14px; padding: 18px 20px;
    }
    div[data-testid="stMetric"] label {
        color: #FCD34D !important; font-size: 12px !important; font-weight: 600 !important;
        text-transform: uppercase; letter-spacing: 0.06em;
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #f1f5f9 !important; font-size: 26px !important; font-weight: 700 !important;
    }
    .big-header { font-size: 28px; font-weight: 700; color: #FCD34D; letter-spacing: -0.02em; margin-bottom: 4px; }
    .sub-header { font-size: 14px; color: #94a3b8; margin-bottom: 24px; }
    .section-title { font-size: 18px; font-weight: 700; color: #FCD34D; margin: 16px 0 10px 0; }
    .ad-copy-box { background: #fff; border-radius: 12px; padding: 16px 20px; margin-bottom: 16px; border: 1px solid #e2e8f0; }
    .ad-label { font-size: 11px; color: #5f6368; font-weight: 600; display: inline-block; background: #f1f3f4; padding: 1px 6px; border-radius: 4px; margin-right: 6px; }
    .ad-headline { font-size: 18px; color: #1a0dab; font-weight: 400; margin-bottom: 4px; }
    .ad-description { font-size: 13px; color: #4d5156; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════

campaign_data = pd.DataFrame([
    {"Campaign": "Homepage", "Budget": 1000, "Impressions": 12133, "Top Imp. Rate": 0.94, "Clicks": 689, "Avg CPC": 0.63, "Total Cost": 434.07, "CTR": 0.0568, "Conversions": 42, "Conv. Rate": 0.0610, "Margin/Conv": 15, "CPA": 10.33, "ROAS": 0.4514},
    {"Campaign": "Floral tie", "Budget": 2000, "Impressions": 33485, "Top Imp. Rate": 0.88, "Clicks": 1110, "Avg CPC": 1.48, "Total Cost": 1642.80, "CTR": 0.0331, "Conversions": 101, "Conv. Rate": 0.0910, "Margin/Conv": 18, "CPA": 16.27, "ROAS": 0.1066},
    {"Campaign": "Classic tie", "Budget": 2000, "Impressions": 61263, "Top Imp. Rate": 0.57, "Clicks": 890, "Avg CPC": 1.70, "Total Cost": 1513.00, "CTR": 0.0145, "Conversions": 45, "Conv. Rate": 0.0506, "Margin/Conv": 16, "CPA": 33.62, "ROAS": -0.5241},
    {"Campaign": "Wedding tie", "Budget": 2000, "Impressions": 47528, "Top Imp. Rate": 0.34, "Clicks": 495, "Avg CPC": 4.00, "Total Cost": 1980.00, "CTR": 0.0104, "Conversions": 58, "Conv. Rate": 0.1172, "Margin/Conv": 75, "CPA": 34.14, "ROAS": 1.1970},
])

adgroup_data = pd.DataFrame([
    {"Campaign": "Homepage", "Ad Group": "Homepage", "Impressions": 12133, "Top Imp. Rate": 1.50, "Clicks": 689, "Avg CPC": 0.63, "Total Cost": 434.07, "CTR": 0.0568, "Conversions": 42, "Conv. Rate": 0.0610, "Margin/Conv": 15, "CPA": 10.33, "ROAS": 0.4514},
    {"Campaign": "Floral tie", "Ad Group": "Floral tie collection", "Impressions": 26619, "Top Imp. Rate": 3.70, "Clicks": 794, "Avg CPC": 1.408, "Total Cost": 1117.75, "CTR": 0.0298, "Conversions": 72, "Conv. Rate": 0.0907, "Margin/Conv": 18, "CPA": 15.52, "ROAS": 0.1595},
    {"Campaign": "Floral tie", "Ad Group": "Floral bow tie collection", "Impressions": 6866, "Top Imp. Rate": 1.50, "Clicks": 316, "Avg CPC": 1.52, "Total Cost": 480.32, "CTR": 0.0460, "Conversions": 29, "Conv. Rate": 0.0918, "Margin/Conv": 18, "CPA": 16.56, "ROAS": 0.0868},
    {"Campaign": "Classic tie", "Ad Group": "Skinny tie", "Impressions": 45301, "Top Imp. Rate": 2.80, "Clicks": 687, "Avg CPC": 1.01, "Total Cost": 693.87, "CTR": 0.0152, "Conversions": 32, "Conv. Rate": 0.0466, "Margin/Conv": 16, "CPA": 21.68, "ROAS": -0.2621},
    {"Campaign": "Classic tie", "Ad Group": "Dotted navy tie", "Impressions": 15962, "Top Imp. Rate": 2.30, "Clicks": 203, "Avg CPC": 0.82, "Total Cost": 166.46, "CTR": 0.0127, "Conversions": 13, "Conv. Rate": 0.0640, "Margin/Conv": 16, "CPA": 12.80, "ROAS": 0.2495},
    {"Campaign": "Wedding tie", "Ad Group": "Wedding tie", "Impressions": 47528, "Top Imp. Rate": 4.10, "Clicks": 495, "Avg CPC": 4.00, "Total Cost": 1980.00, "CTR": 0.0104, "Conversions": 58, "Conv. Rate": 0.1172, "Margin/Conv": 75, "CPA": 34.14, "ROAS": 1.1970},
])

keyword_report_data = pd.DataFrame([
    {"Keyword": "necktie", "Competition": "High", "Top Bid": 1.80, "Avg Monthly": 100000, "CPC Bid": 2.30, "Quality Score": 7, "Impressions": 40657, "Top Imp. Rate": 0.644, "Clicks": 566, "CTR": 0.0139, "Avg CPC": 2.30, "Total Cost": 1301.80, "Conversions": 25, "Conv. Rate": 0.0442, "CPA": 52.07},
    {"Keyword": "tie for suit", "Competition": "High", "Top Bid": 2.40, "Avg Monthly": 10000, "CPC Bid": 2.10, "Quality Score": 6, "Impressions": 2386, "Top Imp. Rate": 0.378, "Clicks": 19, "CTR": 0.0080, "Avg CPC": 2.10, "Total Cost": 39.90, "Conversions": 1, "Conv. Rate": 0.0526, "CPA": 39.90},
    {"Keyword": "floral tie", "Competition": "High", "Top Bid": 1.71, "Avg Monthly": 9500, "CPC Bid": 2.10, "Quality Score": 10, "Impressions": 5303, "Top Imp. Rate": 0.884, "Clicks": 675, "CTR": 0.1273, "Avg CPC": 2.10, "Total Cost": 1417.50, "Conversions": 89, "Conv. Rate": 0.1319, "CPA": 15.93},
    {"Keyword": "floral wedding tie", "Competition": "High", "Top Bid": 2.50, "Avg Monthly": 9000, "CPC Bid": 2.60, "Quality Score": 10, "Impressions": 4255, "Top Imp. Rate": 0.749, "Clicks": 459, "CTR": 0.1079, "Avg CPC": 2.60, "Total Cost": 1193.40, "Conversions": 83, "Conv. Rate": 0.1808, "CPA": 14.38},
    {"Keyword": "floral necktie", "Competition": "High", "Top Bid": 1.88, "Avg Monthly": 8700, "CPC Bid": 2.10, "Quality Score": 9, "Impressions": 3976, "Top Imp. Rate": 0.724, "Clicks": 138, "CTR": 0.0347, "Avg CPC": 2.10, "Total Cost": 289.80, "Conversions": 23, "Conv. Rate": 0.1667, "CPA": 12.60},
    {"Keyword": "pink floral tie", "Competition": "High", "Top Bid": 1.30, "Avg Monthly": 8500, "CPC Bid": 1.50, "Quality Score": 10, "Impressions": 4458, "Top Imp. Rate": 0.831, "Clicks": 533, "CTR": 0.1196, "Avg CPC": 1.50, "Total Cost": 799.50, "Conversions": 178, "Conv. Rate": 0.3340, "CPA": 4.49},
    {"Keyword": "blue floral tie", "Competition": "High", "Top Bid": 0.95, "Avg Monthly": 7500, "CPC Bid": 1.20, "Quality Score": 10, "Impressions": 4306, "Top Imp. Rate": 0.909, "Clicks": 564, "CTR": 0.1310, "Avg CPC": 1.20, "Total Cost": 676.80, "Conversions": 141, "Conv. Rate": 0.2500, "CPA": 4.80},
    {"Keyword": "tie for blue suit", "Competition": "High", "Top Bid": 1.80, "Avg Monthly": 980, "CPC Bid": 2.50, "Quality Score": 6, "Impressions": 371, "Top Imp. Rate": 0.600, "Clicks": 5, "CTR": 0.0135, "Avg CPC": 2.50, "Total Cost": 12.50, "Conversions": 0, "Conv. Rate": 0.0, "CPA": 0.0},
    {"Keyword": "floral tie for sale", "Competition": "High", "Top Bid": 2.40, "Avg Monthly": 880, "CPC Bid": 2.60, "Quality Score": 9, "Impressions": 390, "Top Imp. Rate": 0.702, "Clicks": 13, "CTR": 0.0333, "Avg CPC": 2.60, "Total Cost": 33.80, "Conversions": 6, "Conv. Rate": 0.4615, "CPA": 5.63},
    {"Keyword": "black and white floral tie", "Competition": "High", "Top Bid": 0.85, "Avg Monthly": 120, "CPC Bid": 0.90, "Quality Score": 8, "Impressions": 46, "Top Imp. Rate": 0.610, "Clicks": 1, "CTR": 0.0217, "Avg CPC": 0.90, "Total Cost": 0.90, "Conversions": 0, "Conv. Rate": 0.0, "CPA": 0.0},
    {"Keyword": "unique floral tie", "Competition": "Medium", "Top Bid": 0.95, "Avg Monthly": 700, "CPC Bid": 1.00, "Quality Score": 8, "Impressions": 268, "Top Imp. Rate": 0.758, "Clicks": 12, "CTR": 0.0448, "Avg CPC": 1.00, "Total Cost": 12.00, "Conversions": 0, "Conv. Rate": 0.0, "CPA": 0.0},
    {"Keyword": "red tie with black suit", "Competition": "Medium", "Top Bid": 0.65, "Avg Monthly": 550, "CPC Bid": 0.715, "Quality Score": 5, "Impressions": 138, "Top Imp. Rate": 0.495, "Clicks": 2, "CTR": 0.0145, "Avg CPC": 0.715, "Total Cost": 1.43, "Conversions": 0, "Conv. Rate": 0.0, "CPA": 0.0},
    {"Keyword": "tie and handkerchief set", "Competition": "Medium", "Top Bid": 0.50, "Avg Monthly": 550, "CPC Bid": 0.62, "Quality Score": 4, "Impressions": 124, "Top Imp. Rate": 0.446, "Clicks": 1, "CTR": 0.0081, "Avg CPC": 0.62, "Total Cost": 0.62, "Conversions": 0, "Conv. Rate": 0.0, "CPA": 0.0},
    {"Keyword": "how to tie a tie", "Competition": "Low", "Top Bid": 0.25, "Avg Monthly": 500000, "CPC Bid": 0.27, "Quality Score": 5, "Impressions": 122727, "Top Imp. Rate": 0.648, "Clicks": 2863, "CTR": 0.0233, "Avg CPC": 0.27, "Total Cost": 773.01, "Conversions": 14, "Conv. Rate": 0.0049, "CPA": 55.22},
    {"Keyword": "best tie knot", "Competition": "Low", "Top Bid": 0.10, "Avg Monthly": 9000, "CPC Bid": 0.10, "Quality Score": 4, "Impressions": 1636, "Top Imp. Rate": 0.480, "Clicks": 28, "CTR": 0.0171, "Avg CPC": 0.10, "Total Cost": 2.80, "Conversions": 1, "Conv. Rate": 0.0357, "CPA": 2.80},
])

keyword_research_data = pd.DataFrame([
    {"Keyword": "necktie", "Competition": "High", "Top of Page Bid": 1.80, "Avg Monthly Searches": 100000},
    {"Keyword": "tie for suit", "Competition": "High", "Top of Page Bid": 2.40, "Avg Monthly Searches": 10000},
    {"Keyword": "floral tie", "Competition": "High", "Top of Page Bid": 1.71, "Avg Monthly Searches": 9500},
    {"Keyword": "floral wedding tie", "Competition": "High", "Top of Page Bid": 2.50, "Avg Monthly Searches": 9000},
    {"Keyword": "floral necktie", "Competition": "High", "Top of Page Bid": 1.88, "Avg Monthly Searches": 8700},
    {"Keyword": "pink floral tie", "Competition": "High", "Top of Page Bid": 1.30, "Avg Monthly Searches": 8500},
    {"Keyword": "blue floral tie", "Competition": "High", "Top of Page Bid": 0.95, "Avg Monthly Searches": 7500},
    {"Keyword": "tie for blue suit", "Competition": "High", "Top of Page Bid": 1.80, "Avg Monthly Searches": 980},
    {"Keyword": "floral tie for sale", "Competition": "High", "Top of Page Bid": 2.40, "Avg Monthly Searches": 880},
    {"Keyword": "black and white floral tie", "Competition": "High", "Top of Page Bid": 0.85, "Avg Monthly Searches": 120},
    {"Keyword": "unique floral tie", "Competition": "Medium", "Top of Page Bid": 0.95, "Avg Monthly Searches": 700},
    {"Keyword": "red tie with black suit", "Competition": "Medium", "Top of Page Bid": 0.65, "Avg Monthly Searches": 550},
    {"Keyword": "tie and handkerchief set", "Competition": "Medium", "Top of Page Bid": 0.50, "Avg Monthly Searches": 550},
    {"Keyword": "how to tie a tie", "Competition": "Low", "Top of Page Bid": 0.25, "Avg Monthly Searches": 500000},
    {"Keyword": "best tie knot", "Competition": "Low", "Top of Page Bid": 0.10, "Avg Monthly Searches": 9000},
])


# ═══════════════════════════════════════════════════════
# HEADER & TABS
# ═══════════════════════════════════════════════════════

st.markdown('<div class="big-header">📊 DAZI Paid Search Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Floral Tie Campaign Performance — DAZI USA</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📈 Campaign Report", "🔑 Keyword Report", "🔍 Keyword Research", "📢 Ads & Landing Page"])


# ─── TAB 1: Campaign Report ───
with tab1:
    st.markdown('<div class="section-title">Campaign Overview</div>', unsafe_allow_html=True)
    total_budget = campaign_data["Budget"].sum()
    total_impressions = campaign_data["Impressions"].sum()
    total_clicks = campaign_data["Clicks"].sum()
    total_cost = campaign_data["Total Cost"].sum()
    total_conversions = campaign_data["Conversions"].sum()
    overall_cpa = total_cost / total_conversions if total_conversions > 0 else 0
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    m1.metric("Total Budget", f"${total_budget:,}")
    m2.metric("Impressions", f"{total_impressions:,}")
    m3.metric("Clicks", f"{total_clicks:,}")
    m4.metric("Total Cost", f"${total_cost:,.2f}")
    m5.metric("Conversions", f"{total_conversions:,}")
    m6.metric("Avg CPA", f"${overall_cpa:.2f}")
    st.markdown("")

    st.markdown('<div class="section-title">Campaign Report</div>', unsafe_allow_html=True)
    st.dataframe(campaign_data, use_container_width=True, hide_index=True,
        column_config={
            "Budget": st.column_config.NumberColumn(format="$%d"),
            "Impressions": st.column_config.NumberColumn(format="%d"),
            "Top Imp. Rate": st.column_config.NumberColumn(format="%.0f%%"),
            "Clicks": st.column_config.NumberColumn(format="%d"),
            "Avg CPC": st.column_config.NumberColumn(format="$%.2f"),
            "Total Cost": st.column_config.NumberColumn(format="$%,.0f"),
            "CTR": st.column_config.NumberColumn(format="%.1f%%"),
            "Conversions": st.column_config.NumberColumn(format="%d"),
            "Conv. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "Margin/Conv": st.column_config.NumberColumn(format="$%d"),
            "CPA": st.column_config.NumberColumn(format="$%.2f"),
            "ROAS": st.column_config.NumberColumn(format="%.1f%%"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Ad Group Report</div>', unsafe_allow_html=True)
    st.dataframe(adgroup_data, use_container_width=True, hide_index=True,
        column_config={
            "Impressions": st.column_config.NumberColumn(format="%d"),
            "Top Imp. Rate": st.column_config.NumberColumn(format="%.1f"),
            "Clicks": st.column_config.NumberColumn(format="%d"),
            "Avg CPC": st.column_config.NumberColumn(format="$%.2f"),
            "Total Cost": st.column_config.NumberColumn(format="$%,.0f"),
            "CTR": st.column_config.NumberColumn(format="%.1f%%"),
            "Conversions": st.column_config.NumberColumn(format="%d"),
            "Conv. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "Margin/Conv": st.column_config.NumberColumn(format="$%d"),
            "CPA": st.column_config.NumberColumn(format="$%.2f"),
            "ROAS": st.column_config.NumberColumn(format="%.0f%%"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Metric Definitions</div>', unsafe_allow_html=True)
    for term, defn in {
        "Budget": "The amount of money DAZI is willing to spend on their ads within a specific time period.",
        "Impressions": "The total number of times an ad appears.",
        "Search Top Impression Rate (%)": "The percentage of times an ad appears in the top positions of the search results.",
        "Clicks": "The number of times users clicked on the ad.",
        "CTR (Click-Through Rate)": "The likelihood of receiving a click per impression (Clicks / Impressions).",
        "Avg. CPC (Cost per Click)": "The average amount an advertiser actually pays per click.",
        "Total Cost": "The total advertising expenditure.",
        "Conversions": "The total number of desired actions (e.g., purchases, sign-ups) completed.",
        "Conversion Rate": "The percentage of users who take a desired action (Conversions / Clicks).",
        "CPA (Cost per Acquisition)": "The cost of acquiring a customer (Total Cost / Conversions).",
        "ROAS (Return on Ad Spend)": "Measures how profitable the ad campaign is.",
    }.items():
        with st.expander(f"**{term}**"):
            st.markdown(defn)


# ─── TAB 2: Keyword Report ───
with tab2:
    st.markdown('<div class="section-title">Ad Group: Floral Ties — Keyword Performance Report</div>', unsafe_allow_html=True)
    st.markdown("This report shows the performance of each keyword in the floral ties ad group.")
    st.markdown("")
    kr_impressions = keyword_report_data["Impressions"].sum()
    kr_clicks = keyword_report_data["Clicks"].sum()
    kr_cost = keyword_report_data["Total Cost"].sum()
    kr_conv = keyword_report_data["Conversions"].sum()
    kr_ctr = kr_clicks / kr_impressions if kr_impressions > 0 else 0
    kr_cpa = kr_cost / kr_conv if kr_conv > 0 else 0
    k1, k2, k3, k4, k5, k6 = st.columns(6)
    k1.metric("Impressions", f"{kr_impressions:,}")
    k2.metric("Clicks", f"{kr_clicks:,}")
    k3.metric("CTR", f"{kr_ctr:.2%}")
    k4.metric("Total Cost", f"${kr_cost:,.2f}")
    k5.metric("Conversions", f"{kr_conv:,}")
    k6.metric("Avg CPA", f"${kr_cpa:.2f}")
    st.markdown("")

    st.dataframe(keyword_report_data, use_container_width=True, hide_index=True, height=580,
        column_config={
            "Top Bid": st.column_config.NumberColumn(format="$%.2f"),
            "Avg Monthly": st.column_config.NumberColumn(format="%d"),
            "CPC Bid": st.column_config.NumberColumn(format="$%.2f"),
            "Quality Score": st.column_config.NumberColumn(format="%d"),
            "Impressions": st.column_config.NumberColumn(format="%d"),
            "Top Imp. Rate": st.column_config.NumberColumn(format="%.0f%%"),
            "Clicks": st.column_config.NumberColumn(format="%d"),
            "CTR": st.column_config.NumberColumn(format="%.1f%%"),
            "Avg CPC": st.column_config.NumberColumn(format="$%.2f"),
            "Total Cost": st.column_config.NumberColumn(format="$%,.0f"),
            "Conversions": st.column_config.NumberColumn(format="%d"),
            "Conv. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "CPA": st.column_config.NumberColumn(format="$%.1f"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Metric Definitions</div>', unsafe_allow_html=True)
    for term, defn in {
        "Competition": "The level of competition for a keyword based on the number of advertisers bidding on it.",
        "Top of Page Bid Estimate": "An estimated CPC bid required for your ad to appear at the top of the search results page.",
        "Avg. Monthly Searches": "The average monthly search volume for a keyword.",
        "CPC Bid": "The maximum amount DAZI is willing to pay per click on an ad.",
        "Ad Quality Score": "A quality score assigned by Google (1 = low; 10 = high) based on ad relevance, expected CTR, and landing page experience.",
        "Impressions": "The total number of times an ad appears for a keyword.",
        "Search Top Impression Rate (%)": "The percentage of times an ad appears in the top positions of the search results.",
        "Clicks": "The number of times users clicked on the ad.",
        "CTR (Click-Through Rate)": "The likelihood of receiving a click per impression (Clicks / Impressions).",
        "Avg. CPC (Cost per Click)": "The average amount an advertiser actually pays per click.",
        "Total Cost": "The total advertising expenditure.",
        "Conversions": "The total number of desired actions (e.g., purchases) completed.",
        "Conversion Rate": "The percentage of users who take a desired action (Conversions / Clicks).",
        "CPA (Cost per Acquisition)": "The cost of acquiring a customer (Total Cost / Conversions).",
    }.items():
        with st.expander(f"**{term}**"):
            st.markdown(defn)


# ─── TAB 3: Keyword Research ───
with tab3:
    st.markdown('<div class="section-title">Keyword Research</div>', unsafe_allow_html=True)
    st.markdown(f"**Landing page:** [www.daziusa.com/collections/floral](https://www.daziusa.com/collections/floral)")
    st.markdown("")

    st.dataframe(keyword_research_data, use_container_width=True, hide_index=True,
        column_config={
            "Top of Page Bid": st.column_config.NumberColumn(format="$%.2f"),
            "Avg Monthly Searches": st.column_config.NumberColumn(format="%d"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Discussion Questions</div>', unsafe_allow_html=True)
    st.info("**Which keywords will yield more impressions?**\n\nConsider both the monthly search volume and the competition level.")
    st.info("**Which keywords will yield higher conversion rates?**\n\nThink about search intent — keywords indicating purchase intent (e.g., 'floral tie for sale') tend to convert better than informational queries (e.g., 'how to tie a tie').")
    st.markdown("")

    st.markdown('<div class="section-title">Metric Definitions</div>', unsafe_allow_html=True)
    for term, defn in {
        "Competition": "Degree of competition for the keyword, estimated based on the number of advertisers bidding on the keyword.",
        "Top of Page Bid Estimate": "An estimate for the CPC bid required for your ad to show at the top of search results page.",
        "Avg Monthly Searches": "The average monthly search volume for each keyword. Indicates the popularity of keywords among searchers.",
    }.items():
        with st.expander(f"**{term}**"):
            st.markdown(defn)


# ─── TAB 4: Ads & Landing Page ───
with tab4:
    st.markdown('<div class="section-title">Ad Group: Floral Ties</div>', unsafe_allow_html=True)
    st.markdown(f"**Landing page:** [www.daziusa.com/collections/floral](https://www.daziusa.com/collections/floral)")
    st.markdown("")
    st.markdown('<div class="section-title">Ad Copy Examples</div>', unsafe_allow_html=True)
    col_ad1, col_ad2 = st.columns(2)
    with col_ad1:
        st.markdown("""<div class="ad-copy-box"><div><span class="ad-label">Ad</span> <span style="font-size:13px; color:#1a1a1a;">https://www.daziusa.com/neckties/floral</span></div><div class="ad-headline">Shop Floral Ties For Weddings - Free Shipping On Orders $40+</div><div class="ad-description">Browse Our Original <b>Floral Ties</b>, <b>Floral</b> Bow <b>Ties</b>, And Other Essentials. Shop DAZI® Today! Free Shipping Over $40. Best Quality. Great For <b>Weddings</b>. Styles: White <b>Floral</b>, Blue Bloom.</div></div>""", unsafe_allow_html=True)
    with col_ad2:
        st.markdown("""<div class="ad-copy-box"><div><span class="ad-label">Ad</span> <span style="font-size:13px; color:#1a1a1a;">https://www.daziusa.com/neckties/floral</span></div><div class="ad-headline">Shop Floral Ties - DAZI® Original Floral Ties - daziusa.com</div><div class="ad-description">Browse Our Original <b>Floral Ties</b>, <b>Floral</b> Bow <b>Ties</b>, And More. Shop & Save Today! Best Quality.</div></div>""", unsafe_allow_html=True)
    st.markdown("")
    st.markdown('<div class="section-title">Landing Page Preview</div>', unsafe_allow_html=True)
    st.markdown("The ads direct users to the DAZI floral ties collection page:")
    st.markdown("""
    <div style="background: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0;">
        <div style="background: #333; color: #fff; padding: 14px 24px; display: flex; align-items: center; gap: 24px; font-size: 13px;">
            <span style="font-size: 22px; font-weight: 700; letter-spacing: 0.05em; font-family: serif;">DAZI</span>
            <span>NECKTIES</span><span>BOW TIES</span><span>SWATCHES</span><span>ACCESSORIES</span><span>NEW ARRIVALS</span><span>WEDDINGS</span>
        </div>
        <div style="padding: 24px; text-align: center;">
            <div style="font-size: 12px; color: #888; margin-bottom: 8px;">Home > Floral > Page 1 of 2</div>
            <div style="font-size: 24px; font-weight: 700; color: #333; margin-bottom: 20px;">FLORAL</div>
            <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap;">
                <div style="text-align: center;"><div style="width: 180px; height: 180px; background: linear-gradient(135deg, #f5e6e0, #e8d5c8); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;"><span style="font-size: 40px;">🌸</span></div><div style="font-size: 14px; color: #333; font-weight: 600;">Quicksand Roses</div><div style="font-size: 12px; color: #f5a623;">★★★★★ <span style="color: #888;">68 reviews</span></div><div style="font-size: 16px; color: #333; font-weight: 700;">$32.00</div></div>
                <div style="text-align: center;"><div style="width: 180px; height: 180px; background: linear-gradient(135deg, #e0f0e0, #c8e8c8); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;"><span style="font-size: 40px;">🌿</span></div><div style="font-size: 14px; color: #333; font-weight: 600;">Hidden Garden</div><div style="font-size: 12px; color: #f5a623;">★★★★★ <span style="color: #888;">31 reviews</span></div><div style="font-size: 16px; color: #333; font-weight: 700;">$32.00</div></div>
                <div style="text-align: center;"><div style="width: 180px; height: 180px; background: linear-gradient(135deg, #e0e5f0, #c8d5e8); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;"><span style="font-size: 40px;">💐</span></div><div style="font-size: 14px; color: #333; font-weight: 600;">Scorpion Grass</div><div style="font-size: 12px; color: #f5a623;">★★★★★ <span style="color: #888;">2 reviews</span></div><div style="font-size: 16px; color: #333; font-weight: 700;">$32.00</div></div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown("")
    st.caption("Landing page: www.daziusa.com/collections/floral — Products priced at $32.00 each")