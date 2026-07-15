"""
==============================================================
OptionForge
Confidence Classifier
--------------------------------------------------------------

Converts a normalized institutional score into a confidence
level.

Confidence is always expressed as a percentage (0-100).

==============================================================
"""

from __future__ import annotations


class ConfidenceClassifier:
    """
    Institutional confidence classifier.
    """

    @staticmethod
    def classify(score: float) -> int:
        """
        Convert normalized score to confidence percentage.

        Parameters
        ----------
        score
            Expected range: -1.0 ... +1.0

        Returns
        -------
        int
            Confidence between 0 and 100.
        """

        score = max(-1.0, min(1.0, score))

        confidence = int(abs(score) * 100)

        return confidence