import datetime

from django.db import models


# Create your models here.
class Product(models.Model):
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Xtra Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    """
    choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로 
    해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다. 
    변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름 됩니다.
    """

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        # 생성될 때 stock quantity를 0으로 초기화 로직
        if not self.id:  # 새로운 인스턴스인 경우에만 stock_quantity를 초기화합니다.
            self.stock_quantity = 0
        super().save(*args, **kwargs)


class Inbound(models.Model):
    """
    입고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3, decimal_places=0)
    inbound_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.amount}"

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.product.price
        super().save(*args, **kwargs)


class Outbound(models.Model):
    """
    입고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3, decimal_places=0)
    outbound_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.amount}"

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.product.price
        super().save(*args, **kwargs)


class Inventory(models.Model):

    """
    창고의 제품과 수량 정보를 담는 모델입니다.
    상품, 수량 필드를 작성합니다.
    작성한 Product 모델을 OneToOne 관계로 작성합시다.
    """

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)
    #
    # def save(self, *args, **kwargs):
    #     self.stock_quantity = self.product.stock_quantity
    #     super().save(*args, **kwargs)
