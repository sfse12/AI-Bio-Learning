# 第 1 周练习包：FASTA / CSV 工具

## 这是什么

4 个函数 + 9 个测试。**测试已经写好了，你的任务是让它们从红变绿。**
这不是"照着抄"的练习——测试只规定行为，不告诉你怎么实现。

## 文件

```
week1-starter/
├── io_utils.py          ← 你要改的只有这个文件
├── conftest.py           ← 已经配好，别动
├── data/
│   ├── sample.fasta      10 条细菌素候选（含 1 条带 X、1 条极短 7aa、1 条带描述）
│   └── sample.csv        20 行，格式 label,name,f1,f2,f3
└── tests/
    └── test_io_utils.py  ← 验收测试，**不许改**
```

## 怎么跑

```powershell
cd week1-starter
pytest -q
```

第一次跑会看到 9 个失败（`NotImplementedError`），这是对的。

## 推荐顺序（每天一个，正好一周）

| 天 | 实现 | 跑通后应该看到 |
|---|---|---|
| 周一 | `read_fasta` 基础版（能读 sample.fasta 的正常记录） | 4 个变绿（count/id/大写/X） |
| 周二 | `read_fasta` 边界（空文件、重复 ID） | 6 个 |
| 周三 | `write_fasta`（写完能读回来一样） | 7 个 |
| 周四 | `read_feature_csv` | 8 个 |
| 周五 | `summarize` | **9 个全绿** |
| 周六 | 把 `if __name__ == "__main__"` 那段跑通，输出对 | — |
| 周日 | 提交 + 复盘：这周哪个 bug 卡你最久、为什么 | — |

## 提交要求

```powershell
git add io_utils.py
git commit -m "feat: implement fasta/csv io utils"
git push
```

然后把 `pytest -q` 的最后一行（`9 passed`）和 `git log --oneline` 截图发我。

## 规则（违反就不批改）

1. **不许改 `tests/` 里的任何断言**
2. **不许用 BioPython**、不许 `pip install` 新库——标准库 + pathlib 足够
3. **不许让 AI 直接生成整个函数**：可以问"`str.strip()` 会去掉换行吗"，不许问"帮我写 read_fasta"
4. 卡住超过 30 分钟，把**报错原文**和**你试过的两种写法**一起发我

## 卡住时的三步法

1. 先写 3 行中文伪代码（读文件 → 判断 `>` → 拼接序列），写不出来说明你没想清楚，先别敲键盘
2. 用 `print()` 把中间变量打出来，看它长什么样
3. 单独写 3 行小脚本验证一个假设（比如"`line[1:].split()[0]` 对 `>abc def` 返回什么"）

## 隐藏考点（做完再回来读）

- 为什么 ID 要取第一个空格前的部分？因为 UniProt 的 `sp|P03044|RPC3_LAMBD` 后面常跟描述，不切开后续匹配全错——**你上次踩过这个坑**
- 为什么空序列要跳过而不是保留？因为下游特征提取会把它当有效样本
- 为什么重复 ID 要报错而不是覆盖？因为覆盖会静默丢数据，你在日志里遇到过 129 vs 133 的错位

