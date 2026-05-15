import requests
from DrissionPage import ChromiumPage
import re
import os
from datetime import datetime

# 1. 创建文件夹
if not os.path.exists("video"):
    os.makedirs("video")

google = ChromiumPage()

# 保持你原有的 headers 配置
headers = {
    "cookie": "enter_pc_once=1; UIFID_TEMP=3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b5e2a9f991bcec5116bbf9a5018258c39b156d7c6c43617544fd684c7a308242d42c58160465a6a5571b5256fd0c170c5f; s_v_web_id=verify_mofexl31_EHurH1hU_R51U_4gfd_A8MR_x7xCHZJSRSLX; hevc_supported=true; dy_swidth=1536; dy_sheight=864; fpk1=U2FsdGVkX19ogBssyWiIYC9UfjGeEn8r17aB6EhA9vY0bjPusgyuqDvvVfqNsPVExE2956gZW/qbfUd3+ezBzQ==; fpk2=4238b62bcd3c1a9c24ccf656e6ace824; passport_csrf_token=40add91a3bf8eb09727117c5626609e4; passport_csrf_token_default=40add91a3bf8eb09727117c5626609e4; bd_ticket_guard_client_web_domain=2; d_ticket=cd73212455b28cffa1ac19ab3979fc18a5f6a; passport_mfa_token=CjembyTKM6Bp8vMUrt9O85RHZUlRqLyUNrSLEbw%2FBovSKfgpqPEajLwR4RDrH15x%2Bjf%2Bx2OCW5JeGkoKPAAAAAAAAAAAAABQWVhYgfPLv96me%2FI75ioD1FFFPW7rUCoshFSreynXfq1e9yicgJ%2FRKnKE6iPuXsXuQBD5648OGPax0WwgAiIBAy4kfOo%3D; passport_assist_user=CkFNGIqdByxQw3R5ItiU5ckij5azkRo1D-fcqmDo-g_sN2hmHeMY7mS0_b2nfp6T27-gXpUh3mDoXA-hf4H7vfUP7xpKCjwAAAAAAAAAAAAAUFl_-8cxJrmoyHU2LORqDK6JN6UT3O-X6RCLvqHrU5znvCm0gDwdMjkMthTSnNA2wR8QjeuPDhiJr9ZUIAEiAQPjQTJy; n_mh=otWVaIR8uINvVc645ORHRBNIVU7TGJU-xIzCn__nePo; passport_auth_status=22e2bc02e9649ceebfccd04b6ad7414e%2C; passport_auth_status_ss=22e2bc02e9649ceebfccd04b6ad7414e%2C; sid_guard=86d834fb6bd4735ab4f56447de7048f2%7C1777186557%7C5183999%7CThu%2C+25-Jun-2026+06%3A55%3A56+GMT; uid_tt=92bffcd2508db9a165481265ff0ad32e; uid_tt_ss=92bffcd2508db9a165481265ff0ad32e; sid_tt=86d834fb6bd4735ab4f56447de7048f2; sessionid=86d834fb6bd4735ab4f56447de7048f2; sessionid_ss=86d834fb6bd4735ab4f56447de7048f2; session_tlb_tag=sttt%7C7%7Chtg0-2vUc1q09WRH3nBI8v_________LiMr9hFRX76OWWK5FSxS-JHZkyYUp26Jayq1QPLXY-Wk%3D; is_staff_user=false; has_biz_token=false; sid_ucp_v1=1.0.0-KGY5MjYyMjMyMTYxMjQ0YjNjMzRhM2VhODFiZjY0NWM4ZTc1MzdiMzEKIQj0vJDzhfTOBhD97bbPBhjvMSAMMNTOl-gFOAJA8QdIBBoCbHEiIDg2ZDgzNGZiNmJkNDczNWFiNGY1NjQ0N2RlNzA0OGYy; ssid_ucp_v1=1.0.0-KGY5MjYyMjMyMTYxMjQ0YjNjMzRhM2VhODFiZjY0NWM4ZTc1MzdiMzEKIQj0vJDzhfTOBhD97bbPBhjvMSAMMNTOl-gFOAJA8QdIBBoCbHEiIDg2ZDgzNGZiNmJkNDczNWFiNGY1NjQ0N2RlNzA0OGYy; _bd_ticket_crypt_cookie=64ad9dbd0d12c3955654a4c90c753121; __security_mc_1_s_sdk_sign_data_key_web_protect=9e0181a5-4bf7-8fd0; __security_mc_1_s_sdk_cert_key=d2c6123e-4477-8b96; __security_mc_1_s_sdk_crypt_sdk=43d9aabe-46ce-a298; __security_server_data_status=1; login_time=1777186561239; publish_badge_show_info=%220%2C0%2C0%2C1777186561587%22; DiscoverFeedExposedAd=%7B%7D; UIFID=3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b5f884fccda817be3385a86cf9dea946b9cdbb0f84c9a753bd63ab14e3728cfee03650f60a60d8756af78199b37666085e07a85fef2e3593a8c14454fdc3324838c719f498c3d7cef0a602474a9482bf5c45f99c31f475f24372703a56f8353c1cef37c1f8db89ab6de501bf09146c7ac7da0f4d770575fa13f351062824822815; is_dash_user=1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; SEARCH_RESULT_LIST_TYPE=%22single%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAKO-qQ687vMaNDNDKn1uipEeYbEhTs5Q3ClYmuV279edYEksVzG6XoUwoJDWFaS8V%2F1777219200000%2F0%2F1777186982918%2F0%22; download_guide=%223%2F20260426%2F0%22; my_rd=2; playRecommendGuideTagCount=4; totalRecommendGuideTagCount=4; __ac_nonce=069f2ffd400af4839a197; __ac_signature=_02B4Z6wo00f01QFpxLgAAIDCjMF9Ml5lK7kBScAAACmr76; is_support_rtm_web_ts=1; SelfTabRedDotControl=%5B%7B%22id%22%3A%227392925021036873747%22%2C%22u%22%3A38%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227585111909272127522%22%2C%22u%22%3A139%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227278623374111148047%22%2C%22u%22%3A128%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227577246595121416202%22%2C%22u%22%3A202%2C%22c%22%3A193%7D%2C%7B%22id%22%3A%227625651082902898707%22%2C%22u%22%3A12%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227404328820649510938%22%2C%22u%22%3A294%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227471867636853606441%22%2C%22u%22%3A71%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227610702797641615423%22%2C%22u%22%3A46%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227578983064794040363%22%2C%22u%22%3A351%2C%22c%22%3A326%7D%2C%7B%22id%22%3A%227200786431399987258%22%2C%22u%22%3A180%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227482718601045084195%22%2C%22u%22%3A36%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227092972917335525389%22%2C%22u%22%3A130%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227586648327328892947%22%2C%22u%22%3A160%2C%22c%22%3A154%7D%2C%7B%22id%22%3A%227578465775779612681%22%2C%22u%22%3A86%2C%22c%22%3A0%7D%2C%7B%22id%22%3A%227580689420651923508%22%2C%22u%22%3A36%2C%22c%22%3A0%7D%5D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAKO-qQ687vMaNDNDKn1uipEeYbEhTs5Q3ClYmuV279edYEksVzG6XoUwoJDWFaS8V%2F1777564800000%2F0%2F1777532889424%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUGRJTzkyWkxyWDIvOE1raHJndGdVQ0dITDZuQjdWUFFvWlFPalU2K1lhK3RJYmtjWkJhM3crYWFVM29XV2NHd3k1cVZIU01DL1BMUlZaa0h0L1JFWVk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; strategyABtestKey=%221777532890.224%22; ttwid=1%7C8aqO9VXUdR5y6m3aS7GASWHordLQzGyOOUB2F5nL8AQ%7C1777532890%7C6caafbc2ee828418982d7748d5d272ae17c440db316c46eceab436f5ecf3b4d2; biz_trace_id=6386a4af; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f2771777060272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2733303635353c37363032323234272927676c715a75776a716a666a69273f2763646976602778; bit_env=2K1Uts67ws8HMkHvWB-VhPpQnwOFI92RAskbgfwa_a39TI7ocqeUMfnfJdKu4RLoOTTdB5im-w531iCgwgdlbBa9t3HUozn3yl1p14hNUjizHEIWgsjQ_91ojFsC__LoKlvbiBBw8f9AD875z5bAOKXp3r5WXPtFX7a9bOH4f6k2RbXisZFuUS96JYZEv9UPVJnRRpwJyMsrUHsxUKbJAEoFT_FIw0nPOuYd7xhuwq8HJJcBy-k6dpZwQ8cBHyPi525iitwFf-vIyZoAwKD90J-BCEfeVlMOa3mSBpRMgWwFzrzF-hAJoU1Co8MM4Lh0BpUhlkuZAr_pK_DFRWzlYT8RFGP9WBR5YNvQOtopX7PzNcEcJxIpAYblojMKp6rZMLdguqUx13a_cHFwwdmF7m2ZsaGmQJp4YDqB0eBnApmCDQ7gmw-6vBkS7sIoDibIMztF3lgB5MB4VICpGbtRABwIrGshhGRj0B6ZMIaBY5oKKwO2P-OuoTSFKsS3Bx3bC-1Y-uQvW62AlDe1O8CPA_vSgOB1QVoeyDguz0Zdyv0%3D; gulu_source_res=eyJwX2luIjoiYzA3ZDQzMmJmM2E3YmU5Mjc0ZjBmODA2OGQwZjQ3N2M1Y2I2Mzc2NjNlZTdhOTBiMjlhZWNjZWE3YzQxMjgxYSJ9; passport_auth_mix_state=brnq9s29merabrdiv2zcly6nijdmawsfiqp7o5bl59jemxxj; bd_ticket_guard_client_data_v2=eyJyZWVfcHVibGljX2tleSI6IkJQZElPOTJaTHJYMi84TWtocmd0Z1VDR0hMNm5CN1ZQUW9aUU9qVTYrWWErdElia2NaQmEzdythYVUzb1dXY0d3eTVxVkhTTUMvUExSVlprSHQvUkVZWT0iLCJ0c19zaWduIjoidHMuMi5hMDkxNTFkOWRiMmYwOWNiYjE5OGJkNzJkN2Y1ODVjYTliMWQ1Nzc2ZTM0Y2QxOTk1MjdiZmM2M2M3NjFiMDAyYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJUekdHZnlYRU5sRWhmL2tuVyt3dnNvUkFXQ2JYdklLd0J6dWttOWJyTTNJPSIsInNlY190cyI6IiNSdzV3eDBWNmxJZUlEU3JqUCs5aWhDTVVyS1dPa01pNVNNNTlqK3hPbGNqZ0Q4YnZuRllhQTVDTThCU00ifQ%3D%3D; mp_851392464b60e8cc1948a193642f793b_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A19dc8915a3af23-09273b628c1b698-4c657b58-144000-19dc8915a3af23%22%2C%22%24device_id%22%3A%20%2219dc8915a3af23-09273b628c1b698-4c657b58-144000-19dc8915a3af23%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.douyin.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.douyin.com%22%2C%22%24search_engine%22%3A%20%22bing%22%7D; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A16%2C%5C%22downlink%5C%22%3A9.1%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; odin_tt=867c5ff5fab609739bd2049fb15aa43cdcf37587f9a50faf4ed0f04ee5cd2f03290c65e30d881f61f801a9da5632bc3cb8cc02eb33eec24e1efc3a079b9092f1",
    "Referer": "https://www.douyin.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 2. 开启监听并访问页面
google.listen.start("aweme/post")
google.get("https://www.douyin.com/user/MS4wLjABAAAAYHEthwq24dIsfVrI9UgBOH3wcIa1dzPd9Ounl8UDAxA?from_tab_name=main")

print("正在等待拦截数据包...")
shujubao = google.listen.wait()

# 3. 获取并解析 JSON
res_json = shujubao.response.body
data = res_json.get("aweme_list", [])
total_count = len(data)

print(f"解析成功！共检测到 {total_count} 个视频，准备开始下载...\n" + "-"*50)

# 4. 循环下载（添加了 enumerate 来实现计数）
for index, i in enumerate(data, start=1):
    try:
        # 获取视频地址和描述
        video_url = i["video"]["play_addr"]["url_list"][0]
        desc = i.get("desc", "").strip()
        
        # 5. 正则过滤文件名非法字符（防止报错）
        title_re = re.sub(r'[\\/:*?"<>|]', '', desc)
        if not title_re:
            title_re = f"video_{index}" # 如果描述为空，用序号命名

        # 6. 获取下载时间
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 打印下载状态：完成进度 / 名称 / 时间
        print(f"进度: [{index}/{total_count}]")
        print(f"名称: {title_re}")
        print(f"时间: {now_time}")

        # 7. 采用流式下载（stream=True）解决 IncompleteRead 报错，提高稳定性
        with requests.get(url=video_url, headers=headers, stream=True, timeout=30) as r:
            r.raise_for_status() # 检查请求是否成功
            # 拼接保存路径
            file_path = os.path.join("video", f"{title_re}.mp4")
            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024*1024): # 每块 1MB
                    if chunk:
                        f.write(chunk)
        
        print(f"状态: ✅ 下载成功\n" + "-"*30)

    except Exception as e:
        print(f"状态: ❌ 下载失败 (第{index}个)，原因: {e}\n" + "-"*30)

print(f"任务结束：共尝试下载 {total_count} 个视频。")