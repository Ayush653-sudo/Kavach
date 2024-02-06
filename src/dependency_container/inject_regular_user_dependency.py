from business_logic.password_business import PasswordBusiness
from controllers.password_controller import PasswordController
from dependency_container.container import DependencyContainer
from models.users import User
from views.users.regular.regular_user_dashboard import RegularUserDashboard


def inject_regular_user_dependency(user: User):
    DependencyContainer.password_business = PasswordBusiness()
    DependencyContainer.password_controller = PasswordController(DependencyContainer.password_business,DependencyContainer.audit_business)
    DependencyContainer.regular_user_dashboard = RegularUserDashboard(user, DependencyContainer.password_controller)