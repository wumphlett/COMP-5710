import hvac


if __name__ == '__main__':
    hvc_client = hvac.Client(url='http://127.0.0.1:8200', token='TOKEN')

    secrets = {
        "username": "root_user",
        "password": "test_password",
        "github_pat": "ghp_ahAyHoRwoQ",
        "api_token": "MTIzANO=",
        "api_password": "t5f28U",
    }

    for secret, value in secrets.items():
        hvc_client.secrets.kv.v2.create_or_update_secret(path=secret, secret={'password': value})

    for secret in secrets:
        response = hvc_client.secrets.kv.read_secret_version(path=secret)
        print(f"Secret {secret}: {response['data']['data']['password']}")
