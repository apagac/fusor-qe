# QCI-130

# description

from lib.deployment_runner import UIDeploymentRunner
from pages.wizard.satellite.insights import Insights

def test_many_envs(new_deployment_pg):
    runner = UIDeploymentRunner()
    deployment_name_pg = runner.product_selection(new_deployment_pg)
    update_availability_pg = runner.deployment_name(deployment_name_pg)
    access_insights_pg = runner.update_availability(update_availability_pg)
    assert isinstance(access_insights_pg, Insights)
