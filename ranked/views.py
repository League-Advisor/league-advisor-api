import pandas as pd
import json
import difflib as diff
from collections import Counter
from django.http import JsonResponse


def data_analyzer(request):
    # For recommended build
    user_input = request.GET.get("composition")
    response = user_input.split(",")

    response_title = []
    for character in response:
        response_title.append(character.title())

    champion = response[10].title()

    team1 = response_title[:5]
    team2 = response_title[5:10]

    with open("static/match_data_analysis.csv") as f:
        df = pd.read_csv(f)
        champion_input = df[df.values == champion]
        champ_col = ""
        df_for_winners = pd.DataFrame()
        for i in champion_input.columns:
            helper_df = champion_input.loc[
                lambda champion_input: champion_input[i] == champion
            ]
            if not helper_df.empty:
                champ_col = i
                for (j, row) in helper_df.iterrows():
                    if "team1" in champ_col and row["team1.win"]:
                        df_for_winners = df_for_winners.append(row, ignore_index=True)
                    elif "team2" in champ_col and row["team2.win"]:
                        df_for_winners = df_for_winners.append(row, ignore_index=True)
            teams_winners_list = []
            for row in df_for_winners.itertuples():
                if row[1] == True:
                    for i in range(2, 11, 2):
                        teams_winners_list.append(row[i])
                if row[12] == True:
                    for i in range(13, 23, 2):
                        teams_winners_list.append(row[i])
            items_for_winners_list = []
            for row in df_for_winners.itertuples():
                for i in range(23):
                    if row[i] == champion:
                        items_for_winners_list.append(row[i + 1])
        with open("static/items.json", "r") as f:
            items_names_list = []
            data = json.load(f)
            data = data["data"]
            for i in range(len(items_for_winners_list)):
                result = items_for_winners_list[i].strip("][").split(", ")
                for item in range(len(result)):
                    string_item = result[item]
                    if string_item in data:
                        items_names_list.append(data[string_item]["name"])
        recommended_build = []
        count_items = Counter(items_names_list)
        most_common_items_used = count_items.most_common()
        for i in range(5):
            recommended_build.append(most_common_items_used[i][0])

        # For most common items used

        team_1_champions_winner = []
        team_2_champions_winner = []
        winner_items = []

        for index, row in df_for_winners.iterrows():
            team_1_champions_winner.append(row["team1.composition.champion1"])
            team_1_champions_winner.append(row["team1.composition.champion2"])
            team_1_champions_winner.append(row["team1.composition.champion3"])
            team_1_champions_winner.append(row["team1.composition.champion4"])
            team_1_champions_winner.append(row["team1.composition.champion5"])

            if row["team1.win"] == True and champion in team_1_champions_winner:
                team_1_champions_winner = []
                team_1_champions_winner.append(index)
                team_1_champions_winner.append(row["team1.composition.champion1"])
                team_1_champions_winner.append(row["team1.composition.champion2"])
                team_1_champions_winner.append(row["team1.composition.champion3"])
                team_1_champions_winner.append(row["team1.composition.champion4"])
                team_1_champions_winner.append(row["team1.composition.champion5"])

                winner_items.append(team_1_champions_winner)
                team_1_champions_winner = []

            team_2_champions_winner.append(row["team2.composition.champion6"])
            team_2_champions_winner.append(row["team2.composition.champion7"])
            team_2_champions_winner.append(row["team2.composition.champion8"])
            team_2_champions_winner.append(row["team2.composition.champion9"])
            team_2_champions_winner.append(row["team2.composition.champion10"])

            if row["team2.win"] == True and champion in team_2_champions_winner:
                team_2_champions_winner = []
                team_2_champions_winner.append(index)
                team_2_champions_winner.append(row["team2.composition.champion6"])
                team_2_champions_winner.append(row["team2.composition.champion7"])
                team_2_champions_winner.append(row["team2.composition.champion8"])
                team_2_champions_winner.append(row["team2.composition.champion9"])
                team_2_champions_winner.append(row["team2.composition.champion10"])

                winner_items.append(team_2_champions_winner)
                team_2_champions_winner = []

        threshold = 0.3
        data_normalyzed_str = ""
        data_normalyzed_items = []
        for i in winner_items:
            sm = diff.SequenceMatcher(None, i, team1)
            ratio = sm.ratio()
            if ratio > threshold:
                idx = i[0]
                for index, row in df_for_winners.iterrows():
                    if index == idx:
                        col_name = row.iloc[row.values == champion]
                        col_name = col_name.to_string()
                        data_normalyzed_str = idx
                        data_normalyzed_items.append(data_normalyzed_str)
                        data_normalyzed_str = f"{col_name}_items".replace(
                            f"    {champion}", ""
                        )
                        data_normalyzed_items.append(data_normalyzed_str)

        try:
            counter = 0
            dif_item = []
            for i in range(int((len(data_normalyzed_items) - 1) / 2) + 1):
                row_ = int(data_normalyzed_items[counter])

                col_ = data_normalyzed_items[counter + 1]

                counter += 2

                dif_item.append(df_for_winners[col_].iloc[row_])

        except:

            return JsonResponse(
                {
                    "Error": "No data matched for champion items within your collection",
                    "recommended_build": recommended_build,
                }
            )

        modified_dif_items = []
        for i in range(len(dif_item)):
            array = items_for_winners_list[i].strip("][").split(", ")
            modified_dif_items.append(array)

        analysis_item_names = []
        with open("static/items.json") as f:
            data = json.load(f)
            data = data["data"]

            for item in modified_dif_items:

                for i in item:
                    if i != "0":
                        analysis_item_names.append(data[f"{i}"]["name"])

        return JsonResponse(
            {
                "common items": analysis_item_names[:10],
                "recommended_build": recommended_build,
            }
        )
