
from celery import shared_task
from .models import Task
from .coinmarketcap import CoinMarketCap

@shared_task
def scrape_coin_data(task_id):
    task = Task.objects.get(id=task_id)
    coin_scraper = CoinMarketCap()
    data = coin_scraper.scrape(task.coin)
    task.output = data
    task.save()
