from platforms.models import Platform


def modify_data(data, total_count, page_number, total_page_number):
    modified_data = []

    for item in data:
        modified_item = dict(item)
        data_my = {
            "id": modified_item["id"],
            "title": modified_item["title"],
            "short_description": modified_item["short_description"],
            "full_description": modified_item["full_description"],
            "turnkey_solutions": modified_item["turnkey_solutions"],
            "price": modified_item["price"],
            "status": modified_item["status"],
            "created_at": modified_item["created_at"],
            "image": modified_item["image"],# if modified_item["image"] else "None",
            "link": modified_item["link"],
            "links_to_solution": modified_item["links_to_solution"],
            "tags": [],
        }

        for platform_tag in Platform.objects.get(
                id=modified_item["id"]).filter.all():
            tag_data = {
                "id": platform_tag.id,
                "tag": platform_tag.properties,
                "image_tag": platform_tag.image if platform_tag.image else "None",
                "status": platform_tag.status,
                "is_message": platform_tag.is_message,
            }

            data_my["tags"].append(tag_data)
        if data_my not in modified_data:
            modified_data.append(data_my)

    return {
        "total_count": total_count,
        "curent_count": len(modified_data),
        "curent_page_number": page_number,
        "total_page_number": total_page_number,
        "results": modified_data,
    }



def get_groups_with_filters(groups, filters):
    # groups = queryset_group
    # filters = PlatformFilter.objects.all()
    results = []
    # формирование списка групп
    for group in groups:
        group_data = {
            "group": group.title,
            "id": group.id,
            "count": 0,
            "status": group.status,
            "filters": [],
        }

        # формирование списка фильтров по группам
        for platform_filter in filters.filter(group=group):
            filter_data = {
                "filter": platform_filter.title,
                "id": platform_filter.id,
                "image": f"{platform_filter.image}"
                if platform_filter.image
                else "None",
                "status": platform_filter.status,
                "functionality": platform_filter.functionality,
                "integration": platform_filter.integration,
                "multiple": platform_filter.multiple,
            }

            group_data["filters"].append(filter_data)
            group_data["count"] += 1

        results.append(group_data)
    return results