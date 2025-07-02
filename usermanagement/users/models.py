from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=256)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    role_name = models.CharField(max_length=100)
    permissions = models.JSONField()
    is_active = models.BooleanField(default=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.role_name}"

class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    file_url = models.URLField()
    file_hash = models.CharField(max_length=128)
    file_size = models.DecimalField(max_digits=12, decimal_places=2)
    mime_type = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SystemLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="logs")
    action = models.CharField(max_length=255)
    module = models.CharField(max_length=100)
    metadata = models.JSONField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.user.email if self.user else 'Unknown'}"
