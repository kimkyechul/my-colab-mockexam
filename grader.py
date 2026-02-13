# grader.py
# =========================
# 채점기 (정답 공개형)
# =========================
ANSWER_KEY = {
    "Q1-1": "mean()",
    "Q1-2": "mode()[0]"
}
POINTS = {
    "Q1-1": 50,
    "Q1-2": 50
}
EXPLAIN = {
    "Q1-1": "수치형 변수 결측치는 평균(mean())으로 대체한다.",
    "Q1-2": "범주형 변수 결측치는 최빈값(mode()[0])으로 대체한다."
}
def _norm(x):
    return str(x).strip().replace(" ", "")
def grade(submission):
    earned = 0
    total = sum(POINTS.values())
    print("==== [자동채점 결과] ====\n")
    for qid, ans in ANSWER_KEY.items():
        user = submission.get(qid, "")
        ok = _norm(user) == _norm(ans)
        if ok:
            earned += POINTS[qid]
        print(f"- {qid} ({POINTS[qid]}점): {'정답' if ok else '오답'}")
        print(f"  · 제출: {user}")
        print(f"  · 정답: {ans}")
        print(f"  · 해설: {EXPLAIN[qid]}\n")
    print(f"총점: {earned}점 / {total}점")
