from business_logic.auth_business import AuthBusiness
from controllers.auth_controller import AuthController
from dependency_container.container import DependencyContainer
from views.auth_dashboard import AuthDashboard


def inject_auth_dependency():
    DependencyContainer.auth_business = AuthBusiness()
    DependencyContainer.auth_controller = AuthController(DependencyContainer.auth_business)
    DependencyContainer.auth_dashboard = AuthDashboard(DependencyContainer.auth_controller)

