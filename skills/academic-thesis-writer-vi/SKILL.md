---
name: academic-thesis-writer-vi
description: "Kỹ năng viết tiểu luận / luận văn bậc thạc sĩ bằng tiếng Việt theo phong cách học thuật chuyên nghiệp. Bao gồm cấu trúc chương, giọng văn trang trọng, trích dẫn IEEE, song ngữ Việt-Anh cho thuật ngữ kỹ thuật, và các quy tắc trình bày chuẩn."
category: academic-writing
risk: safe
source: personal
date_added: "2026-02-28"
---

# Kỹ Năng Viết Tiểu Luận / Luận Văn Thạc Sĩ (Tiếng Việt)

## Tổng Quan

Skill này hướng dẫn viết các chương tiểu luận, luận văn, khóa luận bậc thạc sĩ bằng tiếng Việt theo phong cách học thuật chuyên nghiệp, trang trọng, có trích dẫn tài liệu tham khảo đúng chuẩn.

## Khi Nào Sử Dụng

Kích hoạt skill này khi người dùng yêu cầu viết nội dung học thuật tiếng Việt bậc thạc sĩ, bao gồm nhưng không giới hạn:

- Viết **một chương cụ thể** (ví dụ: "viết Chương 2 cơ sở lý thuyết")
- Viết **một mục/tiểu mục** trong chương (ví dụ: "viết phần 3.2 kiến trúc hệ thống")
- Viết **một phần nội dung** theo yêu cầu tùy chỉnh (ví dụ: "viết phần so sánh TF-IDF và BM25")
- **Chỉnh sửa / cải thiện** nội dung học thuật đã có sẵn
- Tạo hoặc sửa **danh mục tài liệu tham khảo**
- Viết báo cáo nghiên cứu, đồ án tốt nghiệp theo chuẩn học thuật

## Nguyên tắc hoạt động

> **QUAN TRỌNG**: Skill này viết **chính xác theo yêu cầu cụ thể** của người dùng.
> KHÔNG tự ý viết toàn bộ luận văn hoặc viết thêm các phần mà người dùng không yêu cầu.

**Quy trình:**

1. **Xác định yêu cầu**: Người dùng nói rõ muốn viết chương nào, mục nào, hoặc nội dung gì.
2. **Quét ngữ cảnh các chương đã viết** ⚠️: Nếu đã có các chương trước đó, **BẮT BUỘC đọc chúng** để:
   - Xác định **số trích dẫn cuối cùng `[M]`** trong danh mục tài liệu tham khảo → chương mới bắt đầu từ `[M+1]`.
   - Nắm các thuật ngữ đã giới thiệu song ngữ → không cần giới thiệu lại, dùng viết tắt.
   - Đảm bảo giọng văn, phong cách nhất quán với các chương trước.
3. **Thu thập ngữ cảnh kỹ thuật**: Đọc PRD, tài liệu kỹ thuật, source code liên quan (nếu có) để nắm chính xác nội dung cần viết.
4. **Viết đúng phần được yêu cầu**: Chỉ viết phần mà người dùng chỉ định, áp dụng tất cả quy tắc bên dưới.
5. **Rà soát**: Chạy checklist trước khi trả kết quả.

## Từ khóa kích hoạt

`tiểu luận`, `luận văn`, `thạc sĩ`, `khóa luận`, `chương`, `tổng quan`, `cơ sở lý thuyết`, `phương pháp nghiên cứu`, `academic`, `thesis`, `dissertation`, `báo cáo nghiên cứu`, `đồ án tốt nghiệp`, `viết chương`, `viết mục`, `viết phần`

---

## QUY TẮC BẮT BUỘC

### Quy tắc 1: Ngôn ngữ và Giọng văn

**BẮT BUỘC tuân thủ tuyệt đối các nguyên tắc sau:**

1. **Ngôi viết**: Sử dụng ngôi thứ ba hoặc câu bị động. **TUYỆT ĐỐI KHÔNG** dùng ngôi thứ nhất ("tôi", "chúng tôi", "em", "nhóm tác giả"). Thay vào đó dùng: "đề tài", "hệ thống", "nghiên cứu này", "tác giả".

2. **Giọng văn trang trọng**: Sử dụng ngôn ngữ khoa học, chính xác, tránh dùng từ ngữ thông tục, khẩu ngữ hoặc biểu cảm cá nhân.

3. **Song ngữ Việt-Anh cho thuật ngữ kỹ thuật**: Khi đề cập thuật ngữ chuyên môn lần đầu, LUÔN viết cả tiếng Việt kèm thuật ngữ tiếng Anh trong ngoặc đơn, kèm viết tắt nếu có.

**Mẫu chuẩn:**

```
Truy hồi thông tin (Information Retrieval — IR)
Xử lý Ngôn ngữ Tự nhiên (Natural Language Processing — NLP)
Mô hình Không gian Vector (Vector Space Model — VSM)
Tần suất thuật ngữ — Tần suất nghịch đảo tài liệu (Term Frequency — Inverse Document Frequency, TF-IDF)
Độ tương đồng cosine (Cosine Similarity)
Tách từ (word segmentation)
Từ dừng (stopwords)
```

4. **Các lần đề cập sau**: Có thể dùng viết tắt đã giới thiệu ở lần đầu.

**Ví dụ ĐÚNG:**

```
Truy hồi thông tin (Information Retrieval — IR) là lĩnh vực nghiên cứu...
Trong phạm vi đề tài, hệ thống IR được thiết kế dựa trên...
```

**Ví dụ SAI:**

```
❌ "Tôi sẽ xây dựng hệ thống tìm kiếm..."
❌ "Chúng ta cần phải sử dụng TF-IDF..." (chưa giới thiệu)
❌ "Cái này rất quan trọng vì..."
```

---

### Quy tắc 2: Cấu trúc Chương

Mỗi chương PHẢI tuân theo hệ thống đánh số phân cấp:

```
# CHƯƠNG N. TÊN CHƯƠNG (VIẾT HOA)

## N.1. Tiêu đề mục cấp 1

### N.1.1. Tiêu đề mục cấp 2

#### N.1.1.1. Tiêu đề mục cấp 3 (nếu cần)
```

**Quy tắc đánh số:**

- Chương: `CHƯƠNG 1`, `CHƯƠNG 2`, ...
- Mục cấp 1: `1.1.`, `1.2.`, `1.3.`, ...
- Mục cấp 2: `1.1.1.`, `1.1.2.`, ...
- Mục cấp 3: `1.1.1.1.` (hạn chế, chỉ dùng khi thật sự cần thiết)

**Tiêu đề chương**: VIẾT HOA toàn bộ.  
**Tiêu đề mục**: Viết hoa chữ cái đầu, còn lại viết thường.

---

### Quy tắc 3: Trích dẫn và Tài liệu tham khảo

**Sử dụng kiểu trích dẫn IEEE (số trong ngoặc vuông):**

1. **Trong văn bản**: Đánh số `[1]`, `[2]`, `[3]`, ... theo thứ tự xuất hiện lần đầu trong văn bản.

2. **Đặt vị trí trích dẫn**: Ngay sau nội dung được trích dẫn, trước dấu chấm câu.

**Mẫu trích dẫn trong văn bản:**

```
Theo nghiên cứu của Manning và cộng sự [2], bài toán truy hồi thông tin...
Mô hình Vector Space Model được đề xuất bởi Salton (1975) [3].
Tách từ tiếng Việt là bước tiền xử lý bắt buộc [7].
```

3. **Danh mục tài liệu tham khảo** đặt cuối mỗi chương (hoặc cuối toàn bộ tài liệu), theo format IEEE:

**Format cho bài báo hội nghị / tạp chí:**

```
[N] Tên_Tác_Giả, "Tên bài báo," _Tên Tạp chí/Hội nghị_, vol. X, no. Y, pp. ZZ–ZZ, Năm.
```

**Format cho sách:**

```
[N] Tên_Tác_Giả, _Tên Sách_, Nhà xuất bản, Năm.
```

**Format cho white paper / báo cáo:**

```
[N] Tên_Tác_Giả, "Tên báo cáo," _Tên Tổ chức_, Năm.
```

4. **QUAN TRỌNG**: Số thứ tự trích dẫn `[N]` trong văn bản PHẢI khớp CHÍNH XÁC với `[N]` trong danh mục tham khảo. Khi hoàn thành, rà soát lại toàn bộ để đảm bảo tính nhất quán.

5. **⚠️ TÍNH LIÊN TỤC GIỮA CÁC CHƯƠNG** (Quy tắc quan trọng nhất):

   Khi viết chương N mà **đã có các chương trước đó**, trích dẫn PHẢI tiếp tục đánh số từ chương trước, KHÔNG được bắt đầu lại từ `[1]`.

   **Quy trình bắt buộc:**
   - **Bước 1**: Đọc tất cả các file chương đã viết trước đó (ví dụ cùng thư mục `docs/report/` hoặc yêu cầu người dùng cung cấp nếu chưa có).
   - **Bước 2**: Tìm số trích dẫn cuối cùng `[M]` trong danh mục tài liệu tham khảo của chương gần nhất.
   - **Bước 3**: Chương mới bắt đầu đánh số từ `[M+1]`.

   **Ví dụ:**

   ```
   Chương 1 kết thúc với tài liệu tham khảo [1] đến [7]
   → Chương 2 bắt đầu trích dẫn từ [8]
   → Chương 3 tiếp tục từ số cuối cùng của Chương 2
   ```

   **Nếu KHÔNG tìm thấy chương trước đó** (ví dụ: viết chương đầu tiên, hoặc người dùng muốn đánh số độc lập mỗi chương), thì bắt đầu từ `[1]`.

   **Ngoài ra**, cũng kiểm tra xem tài liệu từ chương trước có được trích dẫn lại ở chương hiện tại không — nếu có, **dùng lại cùng số `[N]`** đã gán, KHÔNG tạo mục mới.

---

### Quy tắc 4: Đoạn văn và Cách lập luận

1. **Đoạn văn tối thiểu 3-5 câu**. Mỗi đoạn nên tập trung vào MỘT ý chính.

2. **Cấu trúc lập luận trong đoạn**:
   - Câu chủ đề (topic sentence) → Câu phát triển / dẫn chứng → Câu kết luận / chuyển tiếp

3. **Liên kết đoạn**: Sử dụng các từ/cụm từ chuyển tiếp trang trọng:

```
- Mở đầu: "Trong bối cảnh...", "Với sự phát triển của..."
- Bổ sung: "Bên cạnh đó,", "Ngoài ra,", "Hơn nữa,"
- Đối lập: "Tuy nhiên,", "Mặc dù vậy,", "Ngược lại,"
- Kết quả: "Do đó,", "Vì vậy,", "Từ đó,"
- Liệt kê: "Thứ nhất,", "Thứ hai,", "Cuối cùng,"
- Ví dụ: "Cụ thể,", "Chẳng hạn,", "Ví dụ,"
```

4. **Khi liệt kê nhiều điểm**: Sử dụng pattern **"Thứ nhất, ... Thứ hai, ... Thứ ba, ..."** với mỗi phần bắt đầu bằng **in đậm** và theo sau là giải thích chi tiết.

---

### Quy tắc 5: Bảng biểu và Ký hiệu toán học

1. **Bảng**: Sử dụng bảng Markdown cho dữ liệu so sánh, thông số kỹ thuật.

2. **Ký hiệu toán học**: Sử dụng ký tự Unicode khi viết trong Markdown:

```
Ký hiệu tập hợp: D = {d₁, d₂, ..., dₙ}
Tập con: R ⊆ D
Phép tính: w(t,d) = tf(t,d) × log(N/df(t))
```

3. **Công thức phức tạp**: Trình bày riêng thành dòng, giải thích rõ từng ký hiệu.

---

### Quy tắc 6: Phạm vi & Giới hạn

Khi viết phần phạm vi và giới hạn đề tài, PHẢI:

1. **Phân loại rõ ràng** theo các khía cạnh: ngôn ngữ, dữ liệu, thuật toán, kiến trúc, đánh giá, bảo mật.

2. **Phạm vi**: Nêu rõ CÁI GÌ nằm trong phạm vi, dùng bullet points.

3. **Giới hạn**: Trình bày thẳng thắn CÁI GÌ KHÔNG làm và lý do, thể hiện sự tự nhận thức học thuật. Đây **không phải** điểm yếu mà là sự trung thực khoa học.

---

## CẤU TRÚC CÁC CHƯƠNG CHUẨN

### Chương 1: TỔNG QUAN

```
1.1. Giới thiệu đề tài
  1.1.1. Bối cảnh nghiên cứu (tại sao đề tài này quan trọng?)
  1.1.2. Phát biểu bài toán (bài toán cụ thể là gì?)
  1.1.3. Thách thức (khó khăn đặc thù?)
  1.1.4. Xu hướng hiện đại và vị trí đề tài
1.2. Mục tiêu đề tài
  1.2.1. Mục tiêu tổng quát (1 câu súc tích)
  1.2.2. Mục tiêu cụ thể (3-5 mục tiêu con, đánh số)
1.3. Phạm vi và giới hạn đề tài
  1.3.1. Phạm vi nghiên cứu
  1.3.2. Giới hạn đề tài
```

### Chương 2: CƠ SỞ LÝ THUYẾT

```
2.1. Khái niệm nền tảng (định nghĩa chính thức)
2.2. Các mô hình / thuật toán liên quan
  2.2.1. Mô hình A (trình bày lý thuyết + công thức)
  2.2.2. Mô hình B
2.3. Công nghệ sử dụng
  2.3.1. Framework / Thư viện A
  2.3.2. Framework / Thư viện B
2.4. Các nghiên cứu liên quan (related work)
```

### Chương 3: PHƯƠNG PHÁP NGHIÊN CỨU / THIẾT KẾ HỆ THỐNG

```
3.1. Phương pháp nghiên cứu tổng quan
3.2. Kiến trúc hệ thống (sơ đồ tổng quan)
3.3. Thiết kế chi tiết
  3.3.1. Module A
  3.3.2. Module B
3.4. Luồng xử lý dữ liệu (data flow)
3.5. Thiết kế API / Giao diện
```

### Chương 4: THỰC NGHIỆM VÀ KẾT QUẢ

```
4.1. Môi trường thực nghiệm
4.2. Bộ dữ liệu
4.3. Phương pháp đánh giá
4.4. Kết quả thực nghiệm
  4.4.1. Kết quả định lượng (bảng, biểu đồ)
  4.4.2. Kết quả định tính (phân tích, nhận xét)
4.5. So sánh và thảo luận
```

### Chương 5: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

```
5.1. Kết luận
5.2. Đóng góp của đề tài
5.3. Hạn chế
5.4. Hướng phát triển
```

---

## MẪU THAM KHẢO (Reference Example)

Dưới đây là mẫu viết chuẩn cho một đoạn trong chương Tổng quan. Hãy sử dụng đây làm phong cách mẫu:

```markdown
### 1.1.1. Bối cảnh nghiên cứu

Trong bối cảnh bùng nổ thông tin số hiện nay, lượng dữ liệu phi cấu trúc
— đặc biệt là văn bản — đang tăng trưởng với tốc độ chưa từng có. Theo ước
tính của International Data Corporation (IDC), tổng lượng dữ liệu toàn cầu
đã đạt hơn 120 Zettabyte vào năm 2023 và được dự báo sẽ tiếp tục tăng gấp
đôi sau mỗi hai năm [1]. Trong đó, dữ liệu văn bản chiếm một tỷ trọng đáng
kể, bao gồm các bài báo trực tuyến, bài đăng trên mạng xã hội, blog, tài
liệu kỹ thuật và nhiều nguồn nội dung số khác.

Truy hồi thông tin (Information Retrieval — IR) là lĩnh vực nghiên cứu về
các phương pháp tìm kiếm, trích xuất và xếp hạng các tài liệu có liên quan
đến nhu cầu thông tin của người dùng từ một tập hợp tài liệu lớn [2].
```

**Lưu ý các đặc trưng của mẫu:**

- Bắt đầu bằng bối cảnh rộng, thu hẹp dần
- Dẫn chứng số liệu cụ thể + trích dẫn `[1]`
- Thuật ngữ song ngữ: "Truy hồi thông tin (Information Retrieval — IR)"
- Giọng văn khoa học, trang trọng, không cảm xúc cá nhân
- Câu dài nhưng mạch lạc, không rối

---

## CHECKLIST TRƯỚC KHI HOÀN THÀNH

Sau khi viết xong mỗi chương, RÀ SOÁT theo checklist:

- [ ] **Số thứ tự trích dẫn `[N]`** trong văn bản khớp với danh mục tài liệu tham khảo
- [ ] **Thuật ngữ kỹ thuật** lần đầu xuất hiện có kèm tiếng Anh + viết tắt
- [ ] **Không có ngôi thứ nhất** (tôi, chúng tôi, em, nhóm tác giả)
- [ ] **Đánh số mục** đúng hệ thống phân cấp (N.N.N.)
- [ ] **Mỗi đoạn** ít nhất 3 câu, tập trung 1 ý chính
- [ ] **Bảng biểu** có tiêu đề rõ ràng
- [ ] **Không có lỗi chính tả** tiếng Việt (đặc biệt dấu hỏi/ngã)
- [ ] **Giọng văn** nhất quán, trang trọng từ đầu đến cuối
- [ ] **Phần phạm vi/giới hạn** trình bày trung thực, không giấu nhược điểm
- [ ] **Câu chuyển tiếp** giữa các đoạn, các mục mượt mà

---

## CÁC LỖI THƯỜNG GẶP CẦN TRÁNH

| #   | Lỗi                        | Ví dụ SAI                                   | Cách sửa                                               |
| --- | -------------------------- | ------------------------------------------- | ------------------------------------------------------ |
| 1   | Dùng ngôi thứ nhất         | "Tôi sẽ xây dựng hệ thống..."               | "Đề tài xây dựng hệ thống..."                          |
| 2   | Thuật ngữ không có Anh văn | "Mô hình không gian vector"                 | "Mô hình Không gian Vector (Vector Space Model — VSM)" |
| 3   | Trích dẫn sai số           | `[5]` trong văn bản ≠ `[5]` trong danh mục  | Rà soát lại toàn bộ                                    |
| 4   | Đoạn văn 1 câu             | "TF-IDF là sơ đồ trọng số quan trọng."      | Phát triển thêm 2-4 câu giải thích, dẫn chứng          |
| 5   | Viết tắt không giới thiệu  | "Hệ thống IR sử dụng VSM" (chưa giải thích) | Giới thiệu đầy đủ ở lần đầu                            |
| 6   | Liệt kê không giải thích   | "Ưu điểm: nhanh, chính xác, dễ dùng"        | Phát triển từng ưu điểm thành đoạn ngắn                |
| 7   | Kết luận mơ hồ             | "Hệ thống hoạt động tốt"                    | Nêu metric cụ thể: "Thời gian phản hồi dưới 500ms"     |

---

## GHI CHÚ CUỐI

- Skill này áp dụng cho **tiểu luận, luận văn, khóa luận bậc thạc sĩ** tại các trường đại học Việt Nam.
- Phong cách viết được rút trích từ mẫu thực tế đã được đánh giá chất lượng cao.
- Có thể kết hợp với các skill khác (ví dụ: `api-documentation`, `architecture`) để viết các chương kỹ thuật chi tiết.
