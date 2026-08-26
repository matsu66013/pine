import os
import base64
from PIL import Image, ImageDraw, ImageFont
from weasyprint import HTML

# Create a placeholder logo image if the specific screenshot file doesn't exist
image_path = 'スクリーンショット 2024-07-18 225705.png'

if not os.path.exists(image_path):
    img = Image.new('RGB', (180, 180), color='#ffffff')
    draw = ImageDraw.Draw(img)
    draw.rectangle([5, 5, 175, 175], outline='#3fae87', width=6)
    draw.text((30, 75), "WEEDS", fill='#3fae87')
    img.save(image_path)

# Load image and convert to base64
with open(image_path, 'rb') as f:
    logo_base64 = base64.b64encode(f.read()).decode('utf-8')

logo_data_url = f"data:image/png;base64,{logo_base64}"

# HTML for A4 recruitment poster
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  @page {{
    size: A4 portrait;
    margin: 10mm;
    background-color: #f4f8f6;
  }}
  
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Meiryo', 'TakaoPGothic', sans-serif;
  }}

  body {{
    color: #222222;
    background-color: #f4f8f6;
  }}

  /* Top Header / Company Section - Centered Layout */
  .header {{
    background-color: #ffffff;
    border: 3px solid #3fae87;
    border-radius: 16px;
    padding: 14px 20px;
    margin-bottom: 12px;
    width: 100%;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    text-align: center;
  }}

  .header-table {{
    margin: 0 auto;
    border-collapse: collapse;
  }}

  .header-logo-cell {{
    vertical-align: middle;
    padding-right: 15px;
  }}

  .header-logo-cell img {{
    width: 80px;
    height: 80px;
    object-fit: contain;
    display: block;
  }}

  .header-title-cell {{
    vertical-align: middle;
    text-align: center;
  }}

  .company-name {{
    font-size: 24pt;
    font-weight: 900;
    color: #3fae87;
    letter-spacing: 1px;
    line-height: 1.1;
  }}

  .store-name {{
    font-size: 17pt;
    font-weight: bold;
    color: #333333;
    margin-top: 3px;
  }}

  .location-badge {{
    display: inline-block;
    background-color: #3fae87;
    color: #ffffff;
    font-weight: bold;
    font-size: 10pt;
    padding: 3px 12px;
    border-radius: 20px;
    margin-top: 5px;
  }}

  /* Main Catchphrase */
  .catch-banner {{
    background: linear-gradient(135deg, #2b8c6a, #3fae87);
    color: #ffffff;
    text-align: center;
    padding: 12px 10px;
    border-radius: 12px;
    margin-bottom: 12px;
  }}

  .catch-banner h1 {{
    font-size: 24pt;
    font-weight: 900;
    letter-spacing: 2px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
  }}

  .catch-banner p {{
    font-size: 12pt;
    font-weight: bold;
    margin-top: 4px;
    color: #e8f7f1;
  }}

  /* Highlight Boxes for Salary and Hours */
  .highlight-container {{
    margin-bottom: 12px;
  }}

  .hero-box {{
    background-color: #ffffff;
    border-radius: 16px;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }}

  .salary-box {{
    border: 4px solid #e74c3c;
    background-color: #fff9f9;
  }}

  .salary-box .box-label {{
    background-color: #e74c3c;
    color: #ffffff;
    font-size: 15pt;
    font-weight: bold;
    display: inline-block;
    padding: 3px 16px;
    border-radius: 8px;
    margin-bottom: 6px;
  }}

  .salary-amount {{
    font-size: 34pt;
    font-weight: 900;
    color: #d63031;
    text-align: center;
    line-height: 1.2;
    margin: 4px 0;
  }}

  .salary-amount span {{
    font-size: 20pt;
  }}

  .salary-note {{
    text-align: center;
    font-size: 9.5pt;
    color: #666666;
    font-weight: bold;
  }}

  /* Hours Box - Centered Layout */
  .hours-box {{
    border: 4px solid #3fae87;
    background-color: #f0fdf8;
    text-align: center;
  }}

  .hours-box .box-label {{
    background-color: #3fae87;
    color: #ffffff;
    font-size: 15pt;
    font-weight: bold;
    display: inline-block;
    padding: 3px 16px;
    border-radius: 8px;
    margin-bottom: 10px;
  }}

  .hours-table {{
    width: 75%;
    margin: 0 auto 8px auto;
    border-collapse: separate;
    border-spacing: 0 5px;
  }}

  .hours-table td {{
    padding: 5px 14px;
    font-size: 14pt;
    font-weight: bold;
  }}

  .hours-table td.day {{
    width: 40%;
    color: #2b8c6a;
    background-color: #e1f5ed;
    border-radius: 6px 0 0 6px;
    text-align: center;
  }}

  .hours-table td.time {{
    width: 60%;
    color: #222222;
    font-size: 15pt;
    background-color: #ffffff;
    border-radius: 0 6px 6px 0;
    text-align: center;
    border: 1px solid #d0ebd8;
  }}

  .hours-note {{
    font-size: 9pt;
    color: #444444;
    line-height: 1.35;
    border-top: 1px stroke #c8e6d9;
    padding-top: 6px;
    margin-top: 4px;
    text-align: center;
  }}

  /* Appeal Features Section */
  .features-grid {{
    width: 100%;
    margin-bottom: 12px;
  }}

  .feature-card {{
    background-color: #ffffff;
    border-radius: 12px;
    padding: 10px 8px;
    text-align: center;
    border: 2px solid #a8e0cb;
    vertical-align: top;
  }}

  .feature-title {{
    font-size: 11pt;
    font-weight: bold;
    color: #2b8c6a;
    margin-bottom: 5px;
    border-bottom: 2px solid #2b8c6a;
    padding-bottom: 3px;
  }}

  .feature-desc {{
    font-size: 9pt;
    color: #333333;
    line-height: 1.3;
  }}

  /* Bottom Details & Contact Section */
  .footer-info {{
    background-color: #ffffff;
    border-radius: 14px;
    padding: 12px 16px;
    border: 2px solid #3fae87;
  }}

  .info-table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .info-table th {{
    width: 18%;
    background-color: #e1f5ed;
    color: #2b8c6a;
    font-size: 9.5pt;
    padding: 5px 6px;
    text-align: center;
    border-radius: 4px;
    font-weight: bold;
    vertical-align: middle;
  }}

  .info-table td {{
    width: 32%;
    font-size: 9.5pt;
    padding: 5px 8px;
    color: #333333;
    vertical-align: middle;
  }}

  .apply-call {{
    margin-top: 8px;
    background-color: #3fae87;
    color: #ffffff;
    text-align: center;
    padding: 8px;
    border-radius: 8px;
    font-size: 13pt;
    font-weight: bold;
    letter-spacing: 1px;
  }}
</style>
</head>
<body>

  <!-- Header with Company Logo and Name (Centered) -->
  <div class="header">
    <table class="header-table">
      <tr>
        <td class="header-logo-cell">
          <img src="{logo_data_url}" alt="株式会社ウィーズ ロゴ">
        </td>
        <td class="header-title-cell">
          <div class="company-name">株式会社ウィーズ</div>
          <div class="store-name">エコ薬局（大阪府泉大津市）</div>
          <div class="location-badge">南海本線「泉大津駅」より徒歩15分 / 通勤交通費全額支給</div>
        </td>
      </tr>
    </table>
  </div>

  <!-- Catchphrase Banner -->
  <div class="catch-banner">
    <h1>管理薬剤師 募集！</h1>
    <p>【処方箋枚数少なめ】落ち着いた環境で多彩なキャリアに挑戦できる成長企業！</p>
  </div>

  <!-- Key Info Highlight Section: Salary & Working Hours -->
  <div class="highlight-container">
    
    <!-- Salary Box -->
    <div class="hero-box salary-box">
      <div style="text-align: center;">
        <span class="box-label">給与</span>
      </div>
      <div class="salary-amount">
        年収 450<span>万円</span> ～ 550<span>万円</span>
      </div>
      <div class="salary-note">※経験・ご年齢・前職給与等を考慮の上、ご面接後に決定いたします。</div>
    </div>

    <!-- Hours Box (Centered) -->
    <div class="hero-box hours-box">
      <div style="text-align: center;">
        <span class="box-label">勤務時間</span>
      </div>
      <table class="hours-table">
        <tr>
          <td class="day">月・火・水</td>
          <td class="time">09：00 ～ 19：00</td>
        </tr>
        <tr>
          <td class="day">木 曜日</td>
          <td class="time">09：00 ～ 17：00</td>
        </tr>
        <tr>
          <td class="day">土 曜日</td>
          <td class="time">09：00 ～ 12：00</td>
        </tr>
      </table>
      <div class="hours-note">
        ※9:00～20:00の間で1日4～10時間、週40時間を上限とするシフト制（1ヶ月単位の変形労働時間制）<br>
        ※休日：日・祝日 ＋ 他シフト制（有給休暇あり）
      </div>
    </div>

  </div>

  <!-- Features Grid -->
  <div class="features-grid">
    <table style="width:100%; border-spacing: 8px 0; border-collapse: separate;">
      <tr>
        <td class="feature-card" style="width: 33%;">
          <div class="feature-title">落ち着いた業務環境</div>
          <div class="feature-desc">処方箋は内科・神経内科を中心に1日約30枚。ゆとりを持って服薬指導に専念できます。</div>
        </td>
        <td class="feature-card" style="width: 33%;">
          <div class="feature-title">最新システム導入</div>
          <div class="feature-desc">調剤監査システムやスピーディな薬歴入力システムを完備。安心・安全かつスムーズ。</div>
        </td>
        <td class="feature-card" style="width: 33%;">
          <div class="feature-title">多彩なキャリアパス</div>
          <div class="feature-desc">店舗業務に加え、新卒採用や新規店舗開発などやりたいことに挑戦できる社風です。</div>
        </td>
      </tr>
    </table>
  </div>

  <!-- Footer Information & Apply Call -->
  <div class="footer-info">
    <table class="info-table">
      <tr>
        <th>勤務地</th>
        <td>大阪府泉大津市戎町5-10</td>
        <th>応需科目</th>
        <td>内科・神経内科（約30枚/日）</td>
      </tr>
      <tr>
        <th>応募資格</th>
        <td>薬剤師免許をお持ちの方（取得見込み含む）</td>
        <th>福利厚生</th>
        <td>各種社会保険完備・薬剤師賠償責任保険 ほか</td>
      </tr>
    </table>
    <div class="apply-call">
      まずはお気軽にお問合せ・ご応募ください！【株式会社ウィーズ 採用担当】
    </div>
  </div>

</body>
</html>
"""

# Write HTML file
html_file_path = 'recruitment_poster.html'
pdf_file_path = 'recruitment_poster.pdf'

with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Render PDF using WeasyPrint
HTML(html_file_path).write_pdf(pdf_file_path)
print(f"Generated PDF successfully: {pdf_file_path}")