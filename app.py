import streamlit as st
import datetime
import requests
import ephem

API_KEY = "bdd87f6b4000fd30748692be412821d9"  # Thay bằng API key OpenWeatherMap

# ========================
# Xác định cung hoàng đạo
# ========================
def get_zodiac_sign(day, month):
    zodiacs = [
        ((1, 20), (2, 18), "Bảo Bình"),
        ((2, 19), (3, 20), "Song Ngư"),
        ((3, 21), (4, 19), "Bạch Dương"),
        ((4, 20), (5, 20), "Kim Ngưu"),
        ((5, 21), (6, 20), "Song Tử"),
        ((6, 21), (7, 22), "Cự Giải"),
        ((7, 23), (8, 22), "Sư Tử"),
        ((8, 23), (9, 22), "Xử Nữ"),
        ((9, 23), (10, 22), "Thiên Bình"),
        ((10, 23), (11, 21), "Bọ Cạp"),
        ((11, 22), (12, 21), "Nhân Mã"),
        ((12, 22), (1, 19), "Ma Kết"),
    ]
    for start, end, sign in zodiacs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return None

# ========================
# Lấy thời tiết
# ========================
def get_weather(city="Hanoi"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},VN&appid={API_KEY}&lang=vi&units=metric"
    data = requests.get(url).json()
    desc = data["weather"][0]["main"].lower()
    temp = data["main"]["temp"]

    if "rain" in desc:
        weather = "mưa"
    elif "cloud" in desc:
        weather = "mây"
    else:
        weather = "nắng"

    temp_type = "cao" if temp >= 30 else "thấp"

    return weather, temp_type, temp

# ========================
# Pha mặt trăng
# ========================
def get_moon_phase():
    moon = ephem.Moon()
    moon.compute()
    phase = moon.phase
    if phase < 7:
        return "new"
    elif phase < 14:
        return "half"
    else:
        return "full"

# ========================
# Dữ liệu dự đoán
# ========================
predictions = {
    "Bạch Dương": {
        "weather": {
            "nắng": "Nắng ấm tiếp thêm lửa cho Bạch Dương, hãy bắt đầu dự án bạn còn dang dở.",
            "mưa": "Mưa khiến tinh thần dễ chùng xuống, hãy tập trung làm việc nhỏ và chắc chắn.",
            "mây": "Trời nhiều mây nhắc bạn bình tĩnh, đừng vội vàng đưa quyết định."
        },
        "temp": {
            "cao": "Nhiệt độ cao khiến bạn nóng nảy, hãy vận động để giải tỏa năng lượng.",
            "thấp": "Trời lạnh là lúc thích hợp để bạn suy nghĩ chiến lược lâu dài."
        },
        "moon": {
            "new": "Trăng mới đem đến cơ hội khởi đầu, hãy mạnh dạn tiến lên.",
            "half": "Trăng bán nguyệt nhắc bạn cân bằng công việc và nghỉ ngơi.",
            "full": "Trăng tròn làm cảm xúc dâng cao, hãy thận trọng trong giao tiếp."
        }
    },
    "Kim Ngưu": {
        "weather": {
            "nắng": "Ngày nắng giúp Kim Ngưu tập trung phát triển sự nghiệp và tài chính.",
            "mưa": "Mưa mang lại sự lãng mạn, hãy gần gũi hơn với người thân yêu.",
            "mây": "Ngày nhiều mây thích hợp để bạn nghỉ ngơi và tiết kiệm năng lượng."
        },
        "temp": {
            "cao": "Trời nóng dễ làm bạn mệt mỏi, đừng đưa ra quyết định tài chính vội vàng.",
            "thấp": "Không khí lạnh giúp bạn tỉnh táo, thích hợp lên kế hoạch đầu tư."
        },
        "moon": {
            "new": "Trăng mới khuyến khích bạn xây nền tảng vững chắc cho tương lai.",
            "half": "Trăng bán nguyệt giúp bạn nhìn nhận sự việc từ nhiều góc độ.",
            "full": "Trăng tròn là lúc tốt để bạn chia sẻ cảm xúc và tìm sự đồng cảm."
        }
    },
    "Song Tử": {
        "weather": {
            "nắng": "Trời nắng khiến Song Tử trở nên hoạt bát, hãy gặp gỡ và kết nối bạn bè.",
            "mưa": "Mưa nhắc bạn dành thời gian lắng nghe bản thân thay vì chạy theo nhịp sống.",
            "mây": "Ngày u ám khuyến khích bạn đọc sách và học điều mới."
        },
        "temp": {
            "cao": "Nhiệt độ cao khiến bạn dễ xao nhãng, hãy giữ tập trung bằng danh sách việc cần làm.",
            "thấp": "Trời lạnh làm bạn muốn ở nhà, đây là cơ hội tuyệt vời để nghiên cứu ý tưởng mới."
        },
        "moon": {
            "new": "Trăng mới mang lại hứng khởi để bắt đầu mối quan hệ hoặc dự án.",
            "half": "Trăng bán nguyệt nhắc bạn xem xét cả hai mặt của vấn đề.",
            "full": "Trăng tròn thúc đẩy bạn nói ra những điều đã giữ trong lòng."
        }
    },
    "Cự Giải": {
        "weather": {
            "nắng": "Nắng ấm giúp Cự Giải thêm niềm tin vào bản thân và gia đình.",
            "mưa": "Mưa gợi sự hoài niệm, hãy gọi điện cho người thân để cảm thấy ấm áp.",
            "mây": "Ngày nhiều mây thích hợp để bạn nghỉ ngơi và chăm sóc bản thân."
        },
        "temp": {
            "cao": "Nhiệt độ cao dễ làm bạn bực bội, hãy tìm đến không gian yên tĩnh.",
            "thấp": "Thời tiết lạnh khuyến khích bạn gắn kết với gia đình nhiều hơn."
        },
        "moon": {
            "new": "Trăng mới mở ra cơ hội xây dựng tình cảm mới.",
            "half": "Trăng bán nguyệt giúp bạn cân bằng nhu cầu cá nhân và gia đình.",
            "full": "Trăng tròn làm cảm xúc dâng trào, hãy chia sẻ điều bạn suy nghĩ."
        }
    },
    "Sư Tử": {
        "weather": {
            "nắng": "Ngày nắng là sân khấu lý tưởng để Sư Tử tỏa sáng.",
            "mưa": "Mưa khiến bạn dịu lại, hãy dùng thời gian này để lập kế hoạch tương lai.",
            "mây": "Bầu trời nhiều mây nhắc bạn khiêm tốn và lắng nghe nhiều hơn."
        },
        "temp": {
            "cao": "Nhiệt độ cao khuyến khích bạn vận động ngoài trời để giải phóng năng lượng.",
            "thấp": "Không khí lạnh khiến bạn hướng nội, hãy tập trung cải thiện kỹ năng cá nhân."
        },
        "moon": {
            "new": "Trăng mới thôi thúc bạn khởi động dự án đầy tham vọng.",
            "half": "Trăng bán nguyệt nhắc bạn cân bằng giữa tham vọng và thực tế.",
            "full": "Trăng tròn là lúc bạn dễ thu hút sự chú ý và công nhận."
        }
    },
    "Xử Nữ": {
        "weather": {
            "nắng": "Ngày nắng giúp Xử Nữ hoàn thành công việc hiệu quả.",
            "mưa": "Mưa gợi nhắc bạn nghỉ ngơi thay vì cố gắng quá mức.",
            "mây": "Ngày nhiều mây thích hợp để bạn phân tích và lên kế hoạch."
        },
        "temp": {
            "cao": "Trời nóng làm bạn dễ mất kiên nhẫn, hãy chậm rãi kiểm tra chi tiết.",
            "thấp": "Không khí lạnh tăng sự tập trung, thích hợp cho nghiên cứu."
        },
        "moon": {
            "new": "Trăng mới khuyến khích bạn bắt đầu thói quen tích cực.",
            "half": "Trăng bán nguyệt nhắc bạn tìm sự cân bằng giữa lý trí và cảm xúc.",
            "full": "Trăng tròn cho thấy bạn nên tự hào với những gì đã đạt được."
        }
    },
    "Thiên Bình": {
        "weather": {
            "nắng": "Ngày nắng giúp Thiên Bình dễ kết nối và tìm sự hài hòa.",
            "mưa": "Mưa khiến bạn có cơ hội nhìn sâu vào cảm xúc bản thân.",
            "mây": "Ngày nhiều mây nhắc bạn duy trì sự cân bằng trong quan điểm."
        },
        "temp": {
            "cao": "Nhiệt độ cao dễ làm bạn mất cân bằng, hãy hít thở sâu và giữ bình tĩnh.",
            "thấp": "Không khí lạnh khuyến khích bạn suy nghĩ thực tế và công bằng."
        },
        "moon": {
            "new": "Trăng mới tạo điều kiện để bạn khởi đầu mối quan hệ mới.",
            "half": "Trăng bán nguyệt nhắc bạn cân bằng giữa nhu cầu bản thân và người khác.",
            "full": "Trăng tròn làm rõ những mối quan hệ quan trọng trong đời bạn."
        }
    },
    "Bọ Cạp": {
        "weather": {
            "nắng": "Ngày nắng giúp Bọ Cạp bộc lộ sự quyết đoán mạnh mẽ.",
            "mưa": "Mưa mang đến cho bạn thời gian chiêm nghiệm nội tâm.",
            "mây": "Ngày nhiều mây nhắc bạn giữ bí mật cho riêng mình."
        },
        "temp": {
            "cao": "Trời nóng dễ làm bạn căng thẳng, hãy tập trung thiền hoặc thể dục.",
            "thấp": "Thời tiết lạnh khuyến khích bạn suy nghĩ sâu sắc hơn."
        },
        "moon": {
            "new": "Trăng mới khuyến khích bạn bắt đầu hành trình biến đổi bản thân.",
            "half": "Trăng bán nguyệt nhắc bạn kiềm chế và tính toán kỹ lưỡng.",
            "full": "Trăng tròn làm bạn cảm thấy quyền lực, nhưng hãy dùng nó khôn ngoan."
        }
    },
    "Nhân Mã": {
        "weather": {
            "nắng": "Ngày nắng giúp Nhân Mã tràn đầy tinh thần phiêu lưu.",
            "mưa": "Mưa nhắc bạn tạm dừng để lên kế hoạch cho chuyến đi tiếp theo.",
            "mây": "Ngày nhiều mây thích hợp để bạn suy nghĩ về mục tiêu xa hơn."
        },
        "temp": {
            "cao": "Nhiệt độ cao tiếp thêm năng lượng, nhưng đừng hấp tấp.",
            "thấp": "Thời tiết lạnh khuyến khích bạn tìm tri thức và sự thật."
        },
        "moon": {
            "new": "Trăng mới là thời điểm tốt để mở rộng kiến thức.",
            "half": "Trăng bán nguyệt nhắc bạn xem xét lại niềm tin cá nhân.",
            "full": "Trăng tròn thúc đẩy bạn chia sẻ tầm nhìn với người khác."
        }
    },
    "Ma Kết": {
        "weather": {
            "nắng": "Nắng giúp Ma Kết tập trung xây dựng sự nghiệp vững chắc.",
            "mưa": "Mưa khuyến khích bạn suy ngẫm và điều chỉnh kế hoạch dài hạn.",
            "mây": "Ngày nhiều mây thích hợp để bạn làm việc kiên nhẫn và bền bỉ."
        },
        "temp": {
            "cao": "Nhiệt độ cao nhắc bạn tránh ôm đồm quá nhiều việc.",
            "thấp": "Không khí lạnh mang lại sự tập trung cần thiết cho mục tiêu lớn."
        },
        "moon": {
            "new": "Trăng mới mang lại cơ hội khởi động dự án sự nghiệp.",
            "half": "Trăng bán nguyệt nhắc bạn cân bằng giữa trách nhiệm và nghỉ ngơi.",
            "full": "Trăng tròn cho thấy thành quả xứng đáng từ nỗ lực của bạn."
        }
    },
    "Bảo Bình": {
        "weather": {
            "nắng": "Ngày nắng giúp Bảo Bình sáng tạo vượt giới hạn.",
            "mưa": "Mưa mang lại cho bạn cái nhìn độc đáo về vấn đề cũ.",
            "mây": "Ngày nhiều mây khuyến khích bạn tư duy trừu tượng."
        },
        "temp": {
            "cao": "Nhiệt độ cao khiến bạn dễ bốc đồng, hãy kiềm chế.",
            "thấp": "Không khí lạnh khuyến khích bạn suy nghĩ sáng suốt và đổi mới."
        },
        "moon": {
            "new": "Trăng mới mở đường cho sáng kiến táo bạo.",
            "half": "Trăng bán nguyệt nhắc bạn dung hòa sáng tạo và thực tế.",
            "full": "Trăng tròn khiến bạn dễ truyền cảm hứng cho người khác."
        }
    },
    "Song Ngư": {
        "weather": {
            "nắng": "Nắng giúp Song Ngư lạc quan và dễ mơ mộng tích cực.",
            "mưa": "Mưa khiến bạn nhạy cảm hơn, hãy tận dụng để sáng tác.",
            "mây": "Ngày nhiều mây thích hợp để bạn lắng nghe trực giác."
        },
        "temp": {
            "cao": "Trời nóng dễ làm bạn thiếu kiên nhẫn, hãy tìm chỗ yên bình.",
            "thấp": "Không khí lạnh khuyến khích bạn đào sâu vào cảm xúc nội tâm."
        },
        "moon": {
            "new": "Trăng mới khơi nguồn cảm hứng nghệ thuật.",
            "half": "Trăng bán nguyệt giúp bạn cân bằng mơ mộng và thực tế.",
            "full": "Trăng tròn khuếch đại trực giác, tin tưởng vào cảm giác của bạn."
        }
    }
}

# ========================
# App Streamlit
# ========================
st.title("🔮 Tử vi & dự đoán hôm nay")

dob = st.date_input("Ngày sinh của bạn:", datetime.date(2000, 1, 1))

cities_vn = [
    "Hanoi", "Ho Chi Minh City", "Da Nang", "Hai Phong", "Can Tho", 
    "Hue", "Nha Trang", "Vinh", "Quy Nhon", "Da Lat"
]
city = st.selectbox("Chọn thành phố:", cities_vn)

if st.button("Xem tử vi hôm nay"):
    zodiac = get_zodiac_sign(dob.day, dob.month)

    if zodiac is None:
        st.error("Không xác định được cung hoàng đạo.")
    else:
        weather, temp_type, temp = get_weather(city)
        moon_phase = get_moon_phase()

        advice_weather = predictions[zodiac]["weather"].get(weather, "")
        advice_temp = predictions[zodiac]["temp"].get(temp_type, "")
        advice_moon = predictions[zodiac]["moon"].get(moon_phase, "")

        st.subheader(f"♈ Cung hoàng đạo của bạn: {zodiac}")
        st.write(f"🌤️ Thời tiết tại {city}: {weather}, {temp}°C")
        st.write(f"🌙 Pha mặt trăng: {moon_phase}")

        st.markdown("### 🔑 Lời khuyên hôm nay:")
        st.write(f"- {advice_weather}")
        st.write(f"- {advice_temp}")
        st.write(f"- {advice_moon}")
