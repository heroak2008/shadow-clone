from digital_human.processing.chunker import Chunker


def test_chunker_handles_overlap_not_less_than_size() -> None:
    text = "abcdefghij"
    chunks = Chunker.chunk(text, size=3, overlap=3)
    assert chunks
    assert "".join(chunks).startswith("abc")
