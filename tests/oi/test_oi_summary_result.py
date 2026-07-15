from optionforge.oi.oi_summary_result import OISummaryResult


def test_result_creation():

    result = OISummaryResult(
        call_oi=100,
        put_oi=200,
        total_oi=300,
        call_volume=50,
        put_volume=60,
        total_volume=110,
        call_share=0.33,
        put_share=0.67,
        pcr=2.0,
        strikes=5,
        dominant_side="PUT",
    )

    assert result.call_oi == 100
    assert result.put_oi == 200
    assert result.pcr == 2.0
