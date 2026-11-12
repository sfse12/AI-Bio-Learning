"""第 1 周练习：FASTA / CSV 读写工具。

规则：**只实现下面 4 个函数**，不许改函数名和参数，不许改 tests/ 里的断言。
先跑 `pytest -q`，看着失败变绿，一个一个来。

提示：
- 用 `pathlib.Path` 处理路径，不要用字符串拼接
- 读文件统一 `encoding="utf-8"`
- 自己先手算一遍样例数据的预期值，再写代码
"""

from pathlib import Path


def read_fasta(path: str | Path) -> dict[str, str]:
    """读取 FASTA 文件，返回 {序列ID: 序列}。

    规则：
    1. 以 `>` 开头的行是标题，ID 取 `>` 之后、第一个空白字符之前的部分
    2. 其余非空行拼接为该记录的序列
    3. 序列统一转大写，去掉所有空白字符
    4. 空序列跳过（并记录一条 warning 日志）
    5. 文件里一条序列都没有 → 抛 ValueError("FASTA 中没有读到任何序列")
    6. 出现重复 ID → 抛 ValueError，信息里要带上重复的 ID

    返回的 dict 要**保持文件中的原始顺序**（Python 3.7+ 的 dict 天然有序）。
    """
    raise NotImplementedError("实现 read_fasta")


def write_fasta(records: dict[str, str], path: str | Path) -> None:
    """把 {ID: 序列} 写成 FASTA 文件。

    格式：每条记录两行，第一行 `>{ID}`，第二行序列（大写、不换行）。
    记录之间不要空行。
    """
    raise NotImplementedError("实现 write_fasta")


def read_feature_csv(path: str | Path) -> tuple[list[str], list[int], list[list[float]]]:
    """读取特征 CSV（**没有表头**），格式为：label,name,f1,f2,...,fN。

    返回 (names, labels, features)：
    - names:   list[str]，第 2 列
    - labels:  list[int]，第 1 列
    - features: list[list[float]]，第 3 列起，每行 N 个浮点数

    行数与三个返回值的长度必须一致。
    """
    raise NotImplementedError("实现 read_feature_csv")


def summarize(records: dict[str, str]) -> dict:
    """统计序列概况，返回 dict，键为：

    - n:         序列条数
    - min_len:   最短长度
    - max_len:   最长长度
    - mean_len:  平均长度（保留 1 位小数）
    - n_with_x:  含字母 X 的序列条数

    空 dict 输入 → 抛 ValueError。
    """
    raise NotImplementedError("实现 summarize")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    data_dir = Path(__file__).parent / "data"

    recs = read_fasta(data_dir / "sample.fasta")
    print("条数:", len(recs))
    print("前 3 条 ID:", list(recs)[:3])
    print("统计:", summarize(recs))

    names, labels, feats = read_feature_csv(data_dir / "sample.csv")
    print("CSV 行数:", len(names), "特征维度:", len(feats[0]))
    print("正样本数:", sum(labels))
