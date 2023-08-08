

# class Notification(Model):
#     # Defining `id` field is optional, it will be defined automatically
#     # if you haven't done it yourself
#     id = fields.IntField(pk=True)

#     notification_type = fields.CharField(null=True, max_length=50)
#     status = fields.CharField(deafult="unread", max_length=50)
#     content = fields.TextField(null=True)
#     model_name = fields.CharField(null=True, max_length=200)
#     model_id = fields.CharField(null=True, max_length=200)
    
#     account_id = fields.IntField()

#     # Defining ``__str__`` is also optional, but gives you pretty
#     # represent of model in debugger and interpreter
#     def __str__(self):
#         return f"{self.id} {self.notification_type} {self.status}"

#     class Meta:
#         table = "api_notification"


# class Account(Model):
#     id = fields.IntField(pk=True)
#     status = fields.CharField(max_length=3)
#     country = fields.CharField(max_length=3)
#     web_page = fields.CharField(
#         max_length=500,
#         null=True
#     )
#     company = fields.CharField(
#         max_length=500,
#         null=True,
#     )
#     contact_email = fields.CharField(
#         max_length=500,
#         null=True,
#     )
#     contact_phone = fields.CharField(
#         max_length=500,
#         null=True,
#     )

#     user_id = fields.IntField()

#     can_read = fields.BooleanField(default=True)
#     can_write = fields.BooleanField(default=True)

#     primary_account_id = fields.IntField()
#     is_active = fields.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.id} {self.user_id}"

#     class Meta:
#         table = "api_account"