import json
def export_kpi_summary(summary_data, top_category, output_filepath):
    data = {"status": "SUCCESS",
            "top_category": top_category,
            "metrics": summary_data}
    with open(output_filepath, "w") as file:
        json.dump(data, file,indent=4)
    with open(output_filepath, "r") as file:
        result = json.load(file)
    return result
summary_list= [{"category": "Electronics", "total_revenue": 2650.0, "avg_revenue": 1325.0},
                {"category": "Furniture", "total_revenue": 300.0, "avg_revenue": 300.0}]
result = export_kpi_summary(summary_list,"Electronics","kpi_report.json")
print(result)