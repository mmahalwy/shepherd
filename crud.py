"""CRUD operations"""

from model import db, Applications, FixedOption, FlexibleOption, connect_to_db

def create_fixed_option(company_name, contact_email, coverage_requested):
    """Create and return a fixed option."""
    fixed_option = FixedOption(company_name=company_name, 
                                    contact_email=contact_email, 
                                    coverage_requested=coverage_requested)

    db.session.add(fixed_option)
    db.session.commit()

    return fixed_option

def create_flexible_option(company_name, contact_email, project_type):
    """Create and return a flexible option."""
    flexible_option = FlexibleOption(company_name=company_name, 
                                    contact_email=contact_email, 
                                    project_type=project_type)

    db.session.add(flexible_option)
    db.session.commit()

    return flexible_option


def create_fixed_application(fixed):
    """Create and return a fixed application"""

    fixed_application = Applications(fixed=fixed)

    db.session.add(fixed_application)
    db.session.commit()

    return fixed_application

def create_flexible_application(flexible):
    """Create and return a flexible application"""

    flexible_application = Applications(flexible=flexible)

    db.session.add(flexible_application)
    db.session.commit()

    return flexible_application

def get_fixed_option_by_id(fixed_id):
    """Returns fixed option object by fixed_id."""

    return FixedOptions.query.get(fixed_id)

def get_flexible_option_by_id(flexible_id):
    """Returns flexible option object by flexible_id."""

    return FlexibleOption.query.get(flexible_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)