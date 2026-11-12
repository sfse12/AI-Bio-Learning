"""第 1 周的验收测试。**不要修改这个文件。**

跑法（在 week1-starter 目录下）：
    pytest -q
"""

import sys
from pathlib import Path

import pytest

# 保证无论从哪里启动 pytest，都能 import 到上级目录的 io_utils
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from io_utils import read_fasta, read_feature_csv, summarize, write_fasta

DATA = Path(__file__).parent.parent / "data"


def test_read_fasta_count():
    recs = read_fasta(DATA / "sample.fasta")
    assert len(recs) == 10


def test_read_fasta_id_is_first_token():
    recs = read_fasta(DATA / "sample.fasta")
    assert "bac_0001" in recs
    # 带描述的标题：ID 只取到第一个空格
    assert "bac_0002" in recs
    assert "bac_0003|fragment" in recs
    assert all(" " not in rid for rid in recs)


def test_read_fasta_uppercases_and_strips(tmp_path):
    p = tmp_path / "lower.fasta"
    p.write_text(">seq1\nacg t\nTT\n", encoding="utf-8")
    recs = read_fasta(p)
    assert recs["seq1"] == "ACGTTT"


def test_read_fasta_keeps_x():
    recs = read_fasta(DATA / "sample.fasta")
    assert "X" in recs["bac_0004"]


def test_read_fasta_empty_file_raises(tmp_path):
    p = tmp_path / "empty.fasta"
    p.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        read_fasta(p)


def test_read_fasta_duplicate_id_raises(tmp_path, caplog):
    p = tmp_path / "dup.fasta"
    p.write_text(">a\nMKV\n>a\nGGG\n", encoding="utf-8")
    with pytest.raises(ValueError) as exc:
        read_fasta(p)
    assert "a" in str(exc.value)


def test_write_fasta_roundtrip(tmp_path):
    recs = {"s1": "MKV", "s2": "GGGAA"}
    out = tmp_path / "out.fasta"
    write_fasta(recs, out)
    assert read_fasta(out) == recs


def test_read_feature_csv():
    names, labels, feats = read_feature_csv(DATA / "sample.csv")
    assert len(names) == len(labels) == len(feats) == 20
    assert names[0] == "bac_0001"
    assert set(labels) == {0, 1}
    assert len(feats[0]) == 3
    assert all(isinstance(v, float) for v in feats[0])


def test_summarize():
    recs = read_fasta(DATA / "sample.fasta")
    s = summarize(recs)
    assert s["n"] == 10
    assert s["min_len"] == 7
    assert s["max_len"] == 116
    assert s["mean_len"] == pytest.approx(39.9, abs=0.05)
    assert s["n_with_x"] == 1
