h1 = """
      *
      * *
      * * *
* * * * * * *
  * * *
    * *
      *
"""

h2 = """
      *
      * *
      *   *
* * * * * * *
  *   *
    * *
      *
"""

h3 = """
      * * * *
      * * *
      * *
      *
      *
    * *
  * * *
* * * *
"""

h4 = """
      * * * *
      *   *
      * *
      *
      *
    * *
  *   *
* * * *
"""

shapes = [h1, h2, h3, h4]

# 1) tách giữ nguyên khoảng trắng đầu dòng
split_shapes = [s.splitlines() for s in shapes]

# 2) số dòng lớn nhất (để bottom-align)
max_lines = max(len(s) for s in split_shapes)

# 3) chiều rộng tối đa của từng hình (theo kí tự)
widths = [max((len(line) for line in s), default=0) for s in split_shapes]

# 4) thêm dòng trống ở trên cùng để tất cả có cùng số dòng (dùng width riêng của từng hình)
for i, s in enumerate(split_shapes):
    while len(s) < max_lines:
        s.insert(0, " " * widths[i])

# 5) right-pad (ljust) mỗi dòng theo chiều rộng hình tương ứng
padded = []
for i, s in enumerate(split_shapes):
    padded.append([line.ljust(widths[i]) for line in s])

# 6) in từng bước: 1 hình, 2 hình cạnh nhau, 3, rồi 4
sep = "   "  # khoảng cách giữa các hình — bạn có thể tăng/giảm
for step in range(1, len(padded) + 1):
    print("\n" * 2)
    print(f"In {step} hình ngang:")
    for row_idx in range(max_lines):
        row = sep.join(padded[j][row_idx] for j in range(step))
        print(row)
    time.sleep(5)

print("\nHoàn thành 4 hình ngang.")