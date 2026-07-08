"""
============================================================
OptionForge
Repository Context Tests
============================================================
"""

from pathlib import Path

import pytest

from optionforge.repository import RepositoryContext


# ==========================================================
# Construction
# ==========================================================

def test_create_context(tmp_path):

    ctx = RepositoryContext(

        marketforge_root=tmp_path,

    )

    assert isinstance(
        ctx,
        RepositoryContext,
    )


# ==========================================================
# Root Path
# ==========================================================

def test_root_path(tmp_path):

    ctx = RepositoryContext(

        marketforge_root=tmp_path,

    )

    assert ctx.marketforge_root == tmp_path


# ==========================================================
# Defaults
# ==========================================================

def test_defaults(tmp_path):

    ctx = RepositoryContext(

        marketforge_root=tmp_path,

    )

    assert ctx.use_parquet is True

    assert ctx.use_cache is True

    assert ctx.validate_schema is True


# ==========================================================
# Missing Root
# ==========================================================

def test_invalid_root():

    with pytest.raises(
        FileNotFoundError,
    ):

        RepositoryContext(

            marketforge_root=Path(
                r"X:\THIS_PATH_DOES_NOT_EXIST"
            ),

        )


# ==========================================================
# Frozen
# ==========================================================

def test_context_is_frozen(tmp_path):

    ctx = RepositoryContext(

        marketforge_root=tmp_path,

    )

    with pytest.raises(
        Exception,
    ):

        ctx.use_cache = False