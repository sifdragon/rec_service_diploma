from service.rec_methods import calculateSimilarItems, getRecommendedItems, getRecommendations
from dto import ItemUserDto


def get_recs(itemUserDto: ItemUserDto, user: str):
    itemsim = calculateSimilarItems(itemUserDto, n=5)

    rec_items = getRecommendedItems(itemUserDto, itemsim, user)


    items = []
    for cort in rec_items:
        for item in cort:
            if isinstance(item, str):
                items.append(item)
    return items


def get_cart_recs(itemUserDto: ItemUserDto):
    itemsim = calculateSimilarItems(itemUserDto, n=5)

    return itemsim