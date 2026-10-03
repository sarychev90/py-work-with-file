def create_report(data: str, report: str ) -> None:
    result = dict()
    with open(data, "r") as data_file:
        for line in data_file.readlines():
            line = line.strip()
            if not line:
                continue
            k,v = line.split(",")
            result[k] = result.get(k,0) + int(v)
        result["result"] = result.get("supply",0) - result.get("buy",0)

    with open(report, "w") as report_file:
        order = ["supply", "buy", "result"]
        report_file.writelines([f"{k},{result[k]}\n" for k in order])
