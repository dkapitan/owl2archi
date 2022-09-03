from csv import QUOTE_ALL
import pandas as pd


ONZ = ["onz-org", "onz-pers", "onz-zorg", "onz-g"]
ARCHI = {"elements": ["ID","Type","Name","Documentation"],
         "relations": ["ID","Type","Name","Documentation","Source","Target"],
         "properties": ["ID", "Key", "Value"]}


def strip_uri(column):
    return column.split("/")[-1]


def concat_documentation(row):
    "Concatenates all properties that are not null into one documentation text"
    
    properties = [col for col in row.index if "#" in col]
    return "\n\n".join([f"{key:}: {value}" for key,value in row[properties].dropna().to_dict().items()])


def parse_csv(path):
    "Parse exported Protege csv"
    
    df = (pd.read_csv(path)
            .rename(columns=strip_uri)
            .rename(columns={"Entity": "ID", "rdf-schema#label": "Name"})
            .assign(Type="BusinessObject")
         )
    df["ID"] = df.ID.apply(lambda x: x.split("#")[-1])
    df["Documentation"] = df.apply(concat_documentation, axis=1)
    return df


if __name__ == "__main__":
    for onz in ONZ:
        print(f"Processing: {onz}")
        (parse_csv(f"./owl-export/{onz}.csv")
        .loc[:, ARCHI['elements']]
        .dropna()
        .applymap(lambda x: x.replace("'",""))
        .to_csv(f"./archi-import/{onz}/elements.csv", index=False, quoting=QUOTE_ALL)
        )

        # onz-fin is incomplete, parsing manually
        print("Processing: onz-fin")
        fin = parse_csv("./owl-export/onz-fin.csv")
        fin["Name"] = fin.ID
        fin.loc[:,ARCHI["elements"]].to_csv(f"./archi-import/onz-fin/elements.csv", index=False, quoting=QUOTE_ALL) 
