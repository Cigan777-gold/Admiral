![alt text](https://github.com/RaiTeR228/_project_photo_gitHub/blob/main/Admiral/prewie.png)

Admiral - херня для анализа и сбора инфы мониторинга и безопасности



создание ключа(запрос под win10)
    curl -X POST http://localhost:8080/api/register/ -H "Content-Type: application/json" -d "{\"name\": \"server-1\", \"install_token\": \"SUPER_SECRET_123\"}"
результат:
    {"api_key":"93da3443602f0437585814477d9fbd9d69a63a0c2c82c5693bc93b6c9411ac0c","server_id":1}