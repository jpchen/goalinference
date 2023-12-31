import pytest

from doors_keys_gems.dkg_domain import DKGDomain

from doors_keys_gems.parser import parse

from planner.astar import AstarPlanner

from planner.planner import get_plan_from_actions

from planner.stoch_astar import (
    StochasticAstarPlanner,
)

from utils import manhattan_gem_heuristic


@pytest.fixture(scope="module")
def dkg_domain():
    return DKGDomain()


@pytest.fixture(scope="module")
def dkg_state_one():
    return parse(
        "goal_inference/doors_keys_gems/test_problems/problem-1.pddl"
    )


@pytest.fixture(scope="module")
def dkg_state_two():
    return parse(
        "goal_inference/doors_keys_gems/test_problems/problem-2.pddl"
    )


@pytest.fixture(scope="module")
def dkg_state_three():
    return parse(
        "goal_inference/doors_keys_gems/test_problems/problem-3.pddl"
    )


@pytest.fixture(scope="module")
def dkg_state_four():
    return parse(
        "goal_inference/doors_keys_gems/test_problems/problem-4.pddl"
    )


@pytest.fixture(scope="function")
def dkg_astar_planner(dkg_domain):
    return AstarPlanner(dkg_domain, manhattan_gem_heuristic)


@pytest.fixture(scope="function")
def dkg_stoch_astar_planner(dkg_domain):
    return StochasticAstarPlanner(dkg_domain, manhattan_gem_heuristic, 0.1)


@pytest.fixture(scope="function")
def dkg_observation_set(dkg_domain, dkg_state_three):
    actions = [
        ["right"],
        ["right"],
        ["right"],
        ["up"],
        ["up"],
        ["left"],
        ["left"],
        ["left"],
        ["up"],
        ["up"],
        ["up"],
        ["up"],
        ["pickup", "key1"],
        ["right"],
        ["right"],
        ["unlock", "key1", "right"],
        ["right"],
        ["right"],
        ["up"],
    ]
    observed_plan = get_plan_from_actions(dkg_domain, dkg_state_three, actions)
    return observed_plan.states
