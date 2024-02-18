from solutions.models import Solution


def modify_data(data, total_count, page_number, total_page_number):
    modified_data = []

    for item in data:
        modified_item = dict(item)
        data_my = {
            "id": modified_item["id"],
            "title": modified_item["title"],
            # "business_model": modified_item["business_model"],
            # "business_area": modified_item["business_area"],
            # "business_niche": modified_item["business_niche"],
            # "objective": modified_item["objective"],
            # "solution_type": modified_item["solution_type"],
            "short_description": modified_item["short_description"],
            # "platform": modified_item["platform"],
            # "platform_title": modified_item["platform_title"],
            # "platform_image": modified_item["platform_image"],
            # "messengers": modified_item["messengers"],
            # "integration_with_CRM": modified_item["integration_with_CRM"],
            # "integration_with_payment_systems": modified_item["integration_with_payment_systems"],
            "tasks": modified_item["tasks"],
            # "actions_to_complete_tasks": modified_item["actions_to_complete_tasks"],
            "image": modified_item["image"],
            "price": modified_item["price"],
            "filter": modified_item["filter"],
            # "is_active": modified_item["is_active"],
            "status": modified_item["status"],
            "created_at": modified_item["created_at"],
            "image": modified_item["image"] if modified_item["image"] else "None",
            # "turnkey_platform": modified_item["turnkey_platform"],
            "link": modified_item["link"],
            "links_to_platform": modified_item["links_to_platform"],
            "dignities": modified_item["dignities"],
            "full_description": modified_item["full_description"],
            "tags": [],
        }

        for solution_tag in Solution.objects.get(
                id=modified_item["id"]).filter.all():
            tag_data = {
                "id": solution_tag.id,
                "tag": solution_tag.properties,
                "image_tag": solution_tag.image if solution_tag.image else "None",
                "is_active": solution_tag.is_active,
                "is_message": solution_tag.is_message,
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
        for solution_filter in filters.filter(group=group):
            filter_data = {
                "filter": solution_filter.title,
                "id": solution_filter.id,
                "image": f"{solution_filter.image}"
                if solution_filter.image
                else "None",
                "status": solution_filter.status,
                "functionality": solution_filter.functionality,
                "integration": solution_filter.integration,
                "multiple": solution_filter.multiple,
                "is_active": solution_filter.is_active
            }

            group_data["filters"].append(filter_data)
            group_data["count"] += 1

        results.append(group_data)
    return results