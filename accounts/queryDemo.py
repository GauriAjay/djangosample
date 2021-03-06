customers = Customer.objects.all()
firstCustomer = Customer.objects.first()
lastCustomer = Customer.objects.last()
customerByName = Customer.objects.get(name='gauri')
customerById = Customer.objects.get(id=4)
firstCustomer.order_set.all()
order = Order.objects.first() 
parentName = order.customer.name
products = Product.objects.filter(category="Out Door")
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 
productsFiltered = Product.objects.filter(tags__name="Sports")
glovesOrders = firstCustomer.order_set.filter(product__name="gloves").count()


allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
parent.childmodel_set.all()