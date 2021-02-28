from datetime import datetime


def color_negative_red(row) -> list[str]:
    return [
        "background-color: red"
        if row["Alert"] and index == datetime.now().strftime("%b")
        else "background-color: white"
        for index, val in row.items()
    ]


def render(df, name) -> str:
    df.index += 1
    df.columns.str.capitalize()

    props = [("border", "2px solid black")]

    styles = [
        {"selector": "table, th, td", "props": props},
    ]

    if name == "income":
        df = df[["Amount", "Monthly", "Jan", "Feb", "Mar", "Balance", "Alert"]]

        return (
            df.style.hide_columns(["Alert"])
            .set_properties(
                **{
                    "background-color": "white",
                    "color": "black",
                }
            )
            .apply(color_negative_red, axis=1)
            .format("₪ {}")
            .set_table_styles(styles)
            .render()
        )
    elif name == "fees":
        df = df[["Amount", "Jan", "Feb", "Mar", "Balance", "Alert"]]
        return (
            df.style.hide_columns(["Alert"])
            .set_properties(
                **{
                    "background-color": "white",
                    "color": "black",
                }
            )
            .apply(color_negative_red, axis=1)
            .format("₪ {}")
            .set_table_styles(styles)
            .render()
        )
    else:
        return (
            df.style.set_properties(
                **{
                    "background-color": "white",
                    "color": "black",
                }
            )
            .set_table_styles(styles)
            .render()
        )
