from settings import WG_API_MODE, WG_CORS_DOMAIN


def cors_header_value():
    return "*" if WG_API_MODE == "debug" else WG_CORS_DOMAIN
