
# Geri bildirim analiz edən
Bu layihə, Django , MongoDB , Nginx və Docker ilə çalışan feedback analiz edən appdır.

## İstifadə olunan Texnologiyalar

- **Django** - Python web framework
- **MongoDB** - NoSQL database
- **Nginx** - Web server 
- **Docker** - Container
- **Docker Compose** - Container-lərin kontrolu üçün


### Lazım olan şey şüylər :))

- Docker
- Docker Compose
- Git

### Layihənin Qurulması

1. **Reponu clone edin:**

```bash
git clone https://github.com/alvinkhalil/feedback.git
cd feedback-analyzer
```

2. **Docker konteynerlərini işə salın:**

```bash
docker-compose up -d
```

3. **Proyektə-yə daxil olmaq:**

Proyekt `http://localhost:80` url və portunda çalışır.

## Qeydlər

- db folderində feedback.json var, Mongo containeri qalxanda avtomatik entrypoint ilə database, collection yaradılır və həmin json inteqrasiya edilir, əgər varsa skip edilir
- Yəni data görmək üçün nəsə inteqrasiya etməyə yaratmağa ehtiyyac yoxdur


