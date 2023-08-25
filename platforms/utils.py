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
            "is_active": modified_item["is_active"],
            "created_at": modified_item["created_at"],
            "image": modified_item["image"] if modified_item["image"] else "None",
            "link": modified_item["link"],
            "tags": [],
        }

        for platform_tag in Platform.objects.get(
                id=modified_item["id"]).filter.all():
            tag_data = {
                "id": platform_tag.id,
                "tag": platform_tag.properties,
                "image_tag": platform_tag.image if platform_tag.image else "None",
                "is_active": platform_tag.is_active,
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
