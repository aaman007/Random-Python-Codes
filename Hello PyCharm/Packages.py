import ecommerce.shipping
from ecommerce import shipping   # now we can call shipping.calc_shipping() directly
from ecommerce.shipping import calc_shipping # now we can call calc_shipping() directly

# To import multiple functions
from ecommerce.shipping import calc_tax , calc_wages

ecommerce.shipping.calc_shipping()
shipping.calc_shipping()
calc_shipping()


calc_tax()
calc_wages()
