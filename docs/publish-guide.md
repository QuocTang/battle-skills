# Hướng Dẫn Cập Nhật & Publish NPM Package (battle-skills)

Khi bạn có thay đổi về code (thêm skill mới, sửa lỗi, cập nhật chức năng), bạn cần phát hành phiên bản mới lên NPM để người dùng có thể cập nhật qua lệnh `npx battle-skills`.

Vì NPM không cho phép ghi đè (publish over) lên một phiên bản đã tồn tại, bạn bắt buộc phải **tăng phiên bản (bump version)** trước khi publish.

---

## Quy trình 2 bước chuẩn

### Bước 1: Tăng phiên bản (Bump Version)

Sử dụng lệnh `npm version` để tự động tăng số phiên bản trong file `package.json` và tạo một Git commit/tag tương ứng. Có 3 cấp độ:

1. **Patch (Sửa lỗi nhỏ, cập nhật vặt):**
   _Dùng khi:_ Sửa typo trong `SKILL.md`, cập nhật file script nội bộ.
   _Lệnh:_

   ```bash
   npm version patch
   ```

   _(Ví dụ: `1.0.0` ➞ `1.0.1`)_

2. **Minor (Thêm tính năng / Skill mới):**
   _Dùng khi:_ Thêm mới một skill vào thư mục `skills/` (nhưng không làm hỏng các skill cũ).
   _Lệnh:_

   ```bash
   npm version minor
   ```

   _(Ví dụ: `1.0.1` ➞ `1.1.0`)_

3. **Major (Thay đổi lớn, có thể gây breaking changes):**
   _Dùng khi:_ Thay đổi hoàn toàn cấu trúc thư mục, đổi luồng hoạt động của `bin/install.js`.
   _Lệnh:_
   ```bash
   npm version major
   ```
   _(Ví dụ: `1.1.0` ➞ `2.0.0`)_

_(Lưu ý: Không tự sửa tay field `version` trong `package.json` vì sẽ không có tag Git đi kèm)._

### Bước 2: Publish lên NPM

Sau khi đã chạy lệnh tăng phiên bản ở Bước 1, bạn đẩy gói tin mới lên NPM bằng lệnh:

```bash
npm publish
```

> **Lưu ý về 2FA/OTP:** Nếu tài khoản NPM của bạn có bật bảo mật 2 lớp (2FA), lệnh `npm publish` sẽ yêu cầu bạn nhập luồng mã OTP (nhận qua Email hoặc ứng dụng Authenticator). Hãy nhập đúng mã để hoàn tất.

---

## Kịch bản ví dụ thực tế

Giả sử hôm nay bạn vừa thêm một skill mới có tên `advanced-python-testing`:

1. Code xong, chạy test, thấy ok.
2. Bạn commit code lên Git: `git commit -m "feat(skill): add advanced-python-testing"`
3. Bạn thấy đây là một tính năng mới (Minor update), bạn chạy:
   ```bash
   npm version minor
   ```
4. Cuối cùng, đẩy lên NPM:
   ```bash
   npm publish
   ```
5. Đẩy code và tag vừa tạo lên GitHub:
   ```bash
   git push origin main --tags
   ```

Người dùng lúc này chỉ cần chạy lại `npx battle-skills` là sẽ tải được bản mới nhất của bạn về máy.
