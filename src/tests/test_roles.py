"""Tests for the Roles module."""

from src.core.cards.roles import Role, get_all_roles, get_random_roles


def test_get_all_roles() -> None:
    """Test that get_all_roles returns the correct number of roles."""
    all_roles = get_all_roles()
    assert len(all_roles) == 15
    role_names = [role.NAME for role in all_roles]
    assert role_names.count("SabOOter") == 3
    assert role_names.count("Profiteur") == 1
    assert set(role_names) == {
        "SabOOter",
        "Profiteur",
        "GreenDwarf",
        "BlueDwarf",
        "Boss",
        "Geologist",
    }


def test_get_random_roles() -> None:
    """Test that get_random_roles returns the correct number of random roles."""
    num_players = 5
    random_roles = get_random_roles(num_players)
    assert len(random_roles) == num_players
    role_names = [role.NAME for role in random_roles]
    assert all(
        role in {"SabOOter", "Profiteur", "GreenDwarf", "BlueDwarf", "Boss", "Geologist"}
        for role in role_names
    )


def test_roles_initialization() -> None:
    """Test the initialization of Role instances."""
    role = Role()
    role.NAME = "A"
    role.DESCRIPTION = "B"
    role.TEAM = "C"
    assert isinstance(role.NAME, str)
    assert isinstance(role.DESCRIPTION, str)
    assert isinstance(role.TEAM, str)


def test_role_equality() -> None:
    """Test the equality comparison of Role instances."""
    role1 = Role()
    role1.NAME = "SabOOter"
    role1.TEAM = "SabOOter"

    role2 = Role()
    role2.NAME = "SabOOter"
    role2.TEAM = "SabOOter"

    role3 = Role()
    role3.NAME = "Profiteur"
    role3.TEAM = "Neutral"

    assert role1 == role2
    assert role1 != role3
