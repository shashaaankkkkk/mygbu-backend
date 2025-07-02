from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_custom_user(user):
    refresh = RefreshToken()
    refresh['user_id'] = user.user_id
    refresh['email'] = user.email
    refresh['user_type'] = user.user_type  # optional, include anything else here
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
