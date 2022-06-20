from service.rec_methods import calculateSimilarItems, getRecommendedItems, getRecommendations
from dto import ItemUserDto


def get_recs(itemUserDto: ItemUserDto, products, user: str):
    itemsim = calculateSimilarItems(itemUserDto, n=5)

    rec_items = getRecommendedItems(itemUserDto, itemsim, user, products)


    items = []
    for cort in rec_items:
        for item in cort:
            if isinstance(item, str):
                items.append(item)
    firstThree = items[0:3]
    return firstThree


def get_cart_recs(itemUserDto: ItemUserDto):
    itemsim = calculateSimilarItems(itemUserDto, n=5)

    return itemsim