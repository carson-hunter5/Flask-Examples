from flask import Blueprint

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route('/customers')
def get_all_customers():
    return 'donatella VERSACE <3'