import requests
import json

BASE_URL = "https://api.vk.com/method/"
API_VERSION = "5.131"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Вставьте свой токен здесь


def get_user_info(user_id):
    url = f"{BASE_URL}users.get"
    params = {
        "user_ids": user_id,
        "fields": "followers_count",
        "access_token": ACCESS_TOKEN,
        "v": API_VERSION
    }
    response = requests.get(url, params=params).json()
    return response.get("response", [])[0] if response.get("response") else None


def get_followers(user_id):
    url = f"{BASE_URL}users.getFollowers"
    params = {
        "user_id": user_id,
        "count": 100,
        "access_token": ACCESS_TOKEN,
        "v": API_VERSION
    }
    response = requests.get(url, params=params).json()
    return response.get("response", {}).get("items", [])


def get_subscriptions(user_id):
    url = f"{BASE_URL}users.getSubscriptions"
    params = {
        "user_id": user_id,
        "extended": 1,
        "count": 100,
        "access_token": ACCESS_TOKEN,
        "v": API_VERSION
    }
    response = requests.get(url, params=params).json()
    return response.get("response", {}).get("items", [])


def save_to_json(data, filename="vk_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    user_id = "USER_ID"  # Укажите ID пользователя

    user_info = get_user_info(user_id)
    if user_info and user_info.get("followers_count", 0) > 0:
        followers = get_followers(user_id)
        subscriptions = get_subscriptions(user_id)

        user_info.update({"followers": followers, "subscriptions": subscriptions})

        save_to_json(user_info)
        print("Данные сохранены в vk_data.json")
    else:
        print("У пользователя нет подписчиков или подписок.")


if __name__ == "__main__":
    main()
