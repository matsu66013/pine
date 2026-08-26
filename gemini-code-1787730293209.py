from weasyprint import HTML

# HTML for A4 recruitment poster
html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: A4 portrait;
    margin: 10mm;
    background-color: #f4f8f6;
  }
  
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Meiryo', 'TakaoPGothic', sans-serif;
  }

  body {
    color: #222222;
    background-color: #f4f8f6;
  }

  /* Top Header / Company Section */
  .header {
    background-color: #ffffff;
    border: 3px solid #3fae87;
    border-radius: 16px;
    padding: 16px 20px;
    margin-bottom: 12px;
    width: 100%;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    text-align: center;
  }

  /* 上部の「募集」デザイン */
  .recruitment-badge {
    display: inline-block;
    background-color: #e74c3c;
    color: #ffffff;
    font-size: 28pt;
    font-weight: 900;
    padding: 2px 32px;
    border-radius: 30px;
    letter-spacing: 4px;
    margin-bottom: 8px;
    box-shadow: 0 2px 6px rgba(231, 76, 60, 0.3);
  }

  /* 「薬剤師」「事務スタッフ」デザイン */
  .target-positions {
    font-size: 22pt;
    font-weight: 900;
    color: #2c3e50;
    margin-bottom: 10px;
    letter-spacing: 2px;
  }

  .target-positions span {
    color: #3fae87;
    margin: 0 8px;
  }

  .company-name {
    font-size: 16pt;
    font-weight: bold;
    color: #3fae87;
    letter-spacing: 1px;
    line-height: 1.2;
    border-top: 1px dashed #a8e0cb;
    padding-top: 8px;
    margin-top: 4px;
  }

  .store-name {
    font-size: 14pt;
    font-weight: bold;
    color: #333333;
    margin-top: 2px;
  }

  .location-badge {
    display: inline-block;
    background-color: #3fae87;
    color: #ffffff;
    font-weight: bold;
    font-size: 9.5pt;
    padding: 3px 12px;
    border-radius: 20px;
    margin-top: 6px;
  }

  /* Main Catchphrase */
  .catch-banner {
    background: linear-gradient(135deg, #2b8c6a, #3fae87);
    color: #ffffff;
    text-align: center;
    padding: 12px 10px;
    border-radius: 12px;
    margin-bottom: 12px;
  }

  .catch-banner h1 {
    font-size: 22pt;
    font-weight: 900;
    letter-spacing: 2px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
  }

  .catch-banner p {
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 4px;
    color: #e8f7f1;
  }

  /* Highlight Boxes for Salary and Hours */
  .highlight-container {
    margin-bottom: 12px;
  }

  .hero-box {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }

  .salary-box {
    border: 4px solid #e74c3c;
    background-color: #fff9f9;
  }

  .salary-box .box-label {
    background-color: #e74c3c;
    color: #ffffff;
    font-size: 15pt;
    font-weight: bold;
    display: inline-block;
    padding: 3px 16px;
    border-radius: 8px;
    margin-bottom: 6px;
  }

  .salary-amount {
    font-size: 34pt;
    font-weight: 900;
    color: #d63031;
    text-align: center;
    line-height: 1.2;
    margin: 4px 0;
  }

  .salary-amount span {
    font-size: 20pt;
  }

  .salary-note {
    text-align: center;
    font-size: 9.5pt;
    color: #666666;
    font-weight: bold;
  }

  /* Hours Box - Centered Layout */
  .hours-box {
    border: 4px solid #3fae87;
    background-color: #f0fdf8;
    text-align: center;
  }

  .hours-box .box-label {
    background-color: #3fae87;
    color: #ffffff;
    font-size: 15pt;
    font-weight: bold;
    display: inline-block;
    padding: 3px 16px;
    border-radius: 8px;
    margin-bottom: 10px;
  }

  .hours-table {
    width: 75%;
    margin: 0 auto 8px auto;
    border-collapse: separate;
    border-spacing: 0 5px;
  }

  .hours-table td {
    padding: 5px 14px;
    font-size: 14pt;
    font-weight: bold;
  }

  .hours-table td.day {
    width: 40%;
    color: #2b8c6a;
    background-color: #e1f5ed;
    border-radius: 6px 0 0 6px;
    text-align: center;
  }

  .hours-table td.time {
    width: 60%;
    color: #222222;
    font-size: 15pt;
    background-color: #ffffff;
    border-radius: 0 6px 6px 0;
    text-align: center;
    border: 1px solid #d0ebd8;
  }

  .hours-note {
    font-size: 9pt;
    color: #444444;
    line-height: 1.35;
    border-top: 1px stroke #c8e6d9;
    padding-top: 6px;
    margin-top: 4px;
    text-align: center;
  }

  /* Appeal Features Section */
  .features-grid {
    width: 100%;
    margin-bottom: 12px;
  }

  .feature-card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 10px 8px;
    text-align: center;
    border: 2px solid #a8e0cb;
    vertical-align: top;
  }

  .feature-title {
    font-size: 11pt;
    font-weight: bold;
    color: #2b8c6a;
    margin-bottom: 5px;
    border-bottom: 2px solid #2b8c6a;
    padding-bottom: 3px;
  }

  .feature-desc {
    font-size: 9pt;
    color: #333333;
    line-height: 1.3;
  }

  /* Bottom Details & Contact Section */
  .footer-info {
    background-color: #ffffff;
    border-radius: 14px;
    padding: 12px 16px;
    border: 2px solid #3fae87;
  }

  .info-table {
    width: 100%;
    border-collapse: collapse;
  }

  .info-table th {
    width: 18%;
    background-color: #e1f5ed;
    color: #2b8c6a;
    font-size: 9.5pt;
    padding: 5px 6px;
    text-align: center;
    border-radius: 4px;
    font-weight: bold;
    vertical-align: middle;
  }

  .info-table td {
    width: 32%;
    font-size: 9.5pt;
    padding: 5px 8px;
    color: #333333;
    vertical-align: middle;
  }

  .apply-call {
    margin-top: 8px;
    background-color: #3fae87;
    color: #ffffff;
    text-align: center;
    padding: 8px;
    border-radius: 8px;
    font-size: 13pt;
    font-weight: bold;
    letter-spacing: 1px;
  }
</style>
</head>
<body>

  <!-- Header Section without Logo -->
  <div class="header">
    <div class="recruitment-badge">募 集</div>
    <div class="target-positions">薬剤師 <span>/</span> 事務スタッフ</div>
    <div class="company-name">株式会社ウィーズ</div>
    <div class="store-name">エコ薬局（大阪府泉大津市）</div>
    <div class="location-badge">南海本線「泉大津駅」より徒歩15分 / 通勤交通費全額支給</div>
  </div>

  <!-- Catchphrase Banner -->
  <div class="catch-banner">
    <h1>【処方箋枚数少なめ】落ち着いた環境で働けます</h1>
    <p>多彩なキャリアに挑戦できる成長企業で一緒に働きませんか？</p>
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
          <div class="feature-desc">処方箋は内科・神経内科を中心に1日約30枚。ゆとりを持って業務に専念できます。</div>
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
        <td>資格保持者・経験者優遇（未経験の方も歓迎）</td>
        <th>福利厚生</th>
        <td>各種社会保険完備・交通費全額支給 ほか</td>
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