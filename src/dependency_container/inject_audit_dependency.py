


from dependency_container.container import DependencyContainer
from business_logic.audit_business import AuditBusiness
from controllers.audit_controller import AuditController
from views.users.regular.password_audit_dashboard import PasswordAuditDashboard


def injecting_audit_dependency(user):
    DependencyContainer.audit_business = AuditBusiness()
    DependencyContainer.audit_controller = AuditController(DependencyContainer.audit_business)
    DependencyContainer.audit_dashboard = PasswordAuditDashboard(user, DependencyContainer.audit_controller)