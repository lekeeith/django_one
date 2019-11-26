from django.db import models
from db.base_model import BaseModel

# Create your models here.
class User(BaseModel):
    name = models.CharField(max_length=20, unique=True, verbose_name="用户名")
    email = models.CharField(max_length=40, unique=True, verbose_name="用户邮箱")
    #addr = models.ForeignKey()
    phone = models.CharField(max_length=11,unique=True, verbose_name="手机号")
    password = models.CharField(max_length=True, verbose_name="用户密码")

    class Meta:
        db_table = "df_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class AddressManage(models.Manager):
    """地址模型管理类,修改默认查询集,输出更改过得查询"""
    def get_default_addr(self, user):
        try:
            address = self.get(name=user.name, is_default=True)
        except self.model.DoesNotExist:
            address = None
        return address



class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属账户")
    receiver = models.CharField(max_length=20, verbose_name="收件人")
    phone = models.CharField(max_length=11, verbose_name="收件人的联系电话")
    zip_code = models.CharField(max_length=6, null=True, blank=True, verbose_name="邮编")
    is_defalut = models.BooleanField(default=False, verbose_name="默认地址Flag")
    addr = models.CharField(max_length=256, verbose_name="收件地址")

    objects = AddressManage.as_manager()

    class Meta:
        db_table = "df_address"
        verbose_name = "地址"
        verbose_name_plural = verbose_name