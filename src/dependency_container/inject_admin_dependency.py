from business_logic.users_business import UserBusiness
from controllers.users_controller import UsersController
from dependency_container.container import DependencyContainer
from views.users.admin.admin_dashboard import AdminDashboard


def inject_admin_user_dependency(user):
    DependencyContainer.users_business = UserBusiness()
    DependencyContainer.users_controller = UsersController(DependencyContainer.users_business)
    DependencyContainer.admin_dashboard = AdminDashboard(user, DependencyContainer.users_controller)
