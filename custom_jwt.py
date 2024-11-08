import json
import base64
import hmac
import hashlib


def base64url_encode(data):
    # Кодируем в Base64, затем удаляем символы "=", заменяем "+" на "-", "/" на "_"
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')


def create_jwt(header, payload, secret):
    # 1. Кодируем заголовок
    encoded_header = base64url_encode(json.dumps(header).encode('utf-8'))

    # 2. Кодируем полезную нагрузку
    encoded_payload = base64url_encode(json.dumps(payload).encode('utf-8'))

    # 3. Формируем строку "header.payload"
    unsigned_token = f'{encoded_header}.{encoded_payload}'

    # 4. Создаем подпись с использованием HMAC-SHA256
    signature = hmac.new(secret.encode('utf-8'), unsigned_token.encode('utf-8'), hashlib.sha256).digest()

    # 5. Кодируем подпись
    encoded_signature = base64url_encode(signature)

    # 6. Собираем JWT: "header.payload.signature"
    jwt_token = f'{unsigned_token}.{encoded_signature}'

    return jwt_token


# Пример использования:
header = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
}

secret = '14238473274832874872349fdsf23osfisodofisdfdsoif23'

jwt_token = create_jwt(header, payload, secret)
print(jwt_token)
